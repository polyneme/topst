"""
This contains code for converting spase json schema in terminus db to json schema 
& validation tools for incoming data.
The json schema as is more widely accepeted has more support for open source tools
Read More: https://json-schema.org/
"""
import jsonschema
from terminusdb_client import WOQLClient
import requests
import isodate
import os
import dotenv

def is_duration(duration_string):
    """
    Parse a ISO 8601 duration string into a datetime.timedelta object.
    """
    try:
        duration = isodate.parse_duration(duration_string)
    except isodate.isoerror.ISO8601Error as e:
        raise ValueError(f"Invalid ISO 8601 duration string: {duration_string}") from e
    return {"type": "string"}


def handle_type(value)->dict:
    """
    Handle the type of the value and return the json schema type.
    Parameters
    ----------
    value : The type of the element specified in spase.

    Returns
    -------
    Dict
        The json schema type.
    """
    spase_to_json_schema_types = {
        "xsd:string": {"type": "string"},
        "xsd:dateTime": {"type": "string", "format": "date-time"},
        "xsd:float": {"type": "number"},
        "xsd:duration": {
            #TODO: This isn't currently defined in format checker, implement
            "type": "string",
            "format": "duration"
        },
        "xsd:integer":  {"type": "integer"},
    }
    if isinstance(value, dict):
        return {"type": "string", "enum": value["@values"]}
    if spase_to_json_schema_types.get(value):
        return spase_to_json_schema_types.get(value)

    return {"$ref": f"#/definations/{value}"}


def convert_frame_to_schema(frame, definations={}, return_definations=True):
    """
    Convert a frame into a schema.

    # this should return a dict with keys: type, properties, required
    """
    elements = frame["@documentation"]["@properties"]

    required = []  
    arrays = []
    properties = {}

    is_required = lambda x: not isinstance(x, dict) or x["@type"] == "List"
    is_array = lambda x: isinstance(x, dict) and (
        x["@type"] == "List" or x["@type"] == "Set"
    )
    is_subclass = lambda x: x.get("$ref")
    type_ = lambda x: x["@class"] if (isinstance(x, dict) and x.get("@class")) else x

    for element in elements:
        object = handle_type(type_(frame[element]))

        if is_required(frame[element]):
            required.append(element)
        if is_subclass(object):
            # if value doesn't exists in defination add it:
            if definations.get(element) is None:
                # get the frame for the element:
                element_frame = client.get_class_frame(element)
                element_defination = convert_frame_to_schema(element_frame, definations)
                # add the definations in the above to definatons
                if element_defination.get("definations"):
                    definations.update(element_defination["definations"])
                    element_defination.pop("definations")
                # add the defination to the definations:
                definations[element] = element_defination
        if is_array(frame[element]):
            object = {"type": "array", "items": object}
            arrays.append(element)

        properties[element] = object
    return {
        "definations": definations,
        "type": "object",
        "properties": properties,
        "required": required,
        "additionalProperties": False,
    }




def get_all_errors_for_spase(json_schema, data):
    validator = jsonschema.Draft7Validator(json_schema, format_checker=jsonschema.Draft201909Validator.FORMAT_CHECKER)
    errors = validator.iter_errors(data)
    return errors


def getFromDict(dataDict, mapList):
    tempDict = dataDict
    for element in mapList:
        tempDict = tempDict[element]
    return tempDict


def setFromDict(dataDict, mapList, value):
    # Note: to access the last element without the copy, it needs to be accessed by one level above:s
    element_to_modify = getFromDict(dataDict, mapList[:-1])
    element_to_modify[mapList[-1]] = value


#TODO: below is an example, but allow user defined if-else rules to fix data
def fix_errors_rule(errors, data):
    data_manipulated = 0
    for error in errors:
        # if the type is expected to be array, just enclose the given instance in an array:

        if error.validator == "type" and error.validator_value == "array":
            setFromDict(data, list(error.path), [error.instance])
            assert [error.instance] == getFromDict(data, list(error.path))
            data_manipulated = 1

        if (
            error.validator == "required"
            and error.message == "'StopDate' is a required property"
        ):
            new_instance = error.instance
            new_instance["StopDate"] = error.instance["StartDate"]
            setFromDict(data, list(error.path), new_instance)
            assert new_instance == getFromDict(data, list(error.path))
            assert new_instance.get("StopDate") is not None
            data_manipulated = 1
        
        if error.validator == "format" and error.validator_value == "date-time":
            new_instance = error.instance + "Z"
            setFromDict(data, list(error.path), new_instance)
            assert new_instance == getFromDict(data, list(error.path))
            data_manipulated = 1

        if error.validator == "type" and error.validator_value == "string":
            setFromDict(data, list(error.path), str(error.instance[0]))
            assert str(error.instance[0]) == getFromDict(data, list(error.path))
            data_manipulated = 1

    return data, data_manipulated


# TODO: change below function by extending the validation class for specifically terminusdb & add rules based insertion
def recursive_dict(current_element, parent_key):
    new_dictonary = {}

    # if current element is not a iter:
    if not isinstance(current_element, dict) and not isinstance(current_element, list):
        return current_element
    for key in current_element:
        if isinstance(current_element[key], dict):
            new_dictonary[key] = recursive_dict(current_element[key], key)
        elif isinstance(current_element[key], list):
            # check if elements are dict:
            new_dictonary[key] = [
                recursive_dict(current_element[key][i], key)
                for i in range(len(current_element[key]))
            ]
        else:
            new_dictonary[key] = current_element[key]

    new_dictonary["@type"] = parent_key
    return new_dictonary


#
if __name__ == "__main__":
    dotenv.load_dotenv()

    team = os.getenv("TEAM")
    dbid = os.getenv("DATABASE_ID")
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    uri =f"http://{host}:{port}"
    client = WOQLClient(uri)
    client.connect(team=team, db=dbid)


    # get displaydata_schema:
    frame_type = "Model"
    DisplayData_frame = client.get_class_frame(frame_type)
    json_schema = convert_frame_to_schema(DisplayData_frame)

    example_urls = [
        "https://hpde.io/ASWS/DisplayData/Solar_Image/Clg_Solar_Image.json",
        "https://hpde.io/ASWS/DisplayData/Imaging_Riometer/Dav_Imaging_Riometer.json",
        "https://hpde.io/CCMC/Model/IRI-2016.json",
    ]

    # get data:
    example_display_data = requests.get(example_urls[2]).json()["Spase"][frame_type]



    errors = get_all_errors_for_spase(json_schema, example_display_data)
    errors = list(errors)
    fixed_data, data_manipulated = fix_errors_rule(errors, example_display_data)

    while data_manipulated and len(list(errors)) > 0:
        errors = get_all_errors_for_spase(json_schema, fixed_data)
        errors = list(errors)
        fixed_data, data_manipulated = fix_errors_rule(errors, fixed_data)

    assert len(errors) == 0, f"Errors: {errors}"
    data_to_insert = recursive_dict(fixed_data, frame_type)

    # save the above data:
    data_inserted = client.insert_document(data_to_insert)
    print(data_inserted)
