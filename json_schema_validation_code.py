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


def handle_type(value) -> dict:
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
            # TODO: This isn't currently defined in format checker, implement
            "type": "string",
            "format": "duration",
        },
        "xsd:integer": {"type": "integer"},
    }
    if isinstance(value, dict):
        return {"type": "string", "enum": value["@values"]}
    if spase_to_json_schema_types.get(value):
        return spase_to_json_schema_types.get(value)

    return {"$ref": f"#/definations/{value}"}


def convert_frame_to_schema(frame, client, definations={}, return_definations=True):
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
                element_defination = convert_frame_to_schema(
                    element_frame, client, definations
                )
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
    validator = jsonschema.Draft7Validator(
        json_schema, format_checker=jsonschema.Draft201909Validator.FORMAT_CHECKER
    )
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
