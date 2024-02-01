"""
This code creates a spase database in terminus-db, fetches example data and fixes errors to insert data into db 
"""


from terminusdb_client import WOQLClient


from spase_to_schema_json import (
    create_and_save_json,
    read_json_file,
    create_terminus_db_from_schema,
)
import os
from json_schema_validation_code import (
    get_all_errors_for_spase,
    convert_frame_to_schema,
    setFromDict,
    getFromDict,
)
import dotenv
import requests
import pandas as pd


# TODO: below is an example, but allow user defined if-else rules to fix data
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


def example_detect_errors():
    dotenv.load_dotenv()

    # Create schema json:
    schema_file = create_and_save_json()
    schema = read_json_file(schema_file)

    # Connect & create schema:
    team = os.getenv("TEAM")
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    dbid = os.getenv("DATABASE_ID")

    # uri = f"http://{host}:{port}"
    client, results = create_terminus_db_from_schema(
        schema, dbid, team, host, port, on_exists_delete=True
    )
    assert client.get_existing_classes().keys() == set(
        results
    ), "The classes created are not the same as the classes in the schema."

    example_urls = [
        "https://hpde.io/ASWS/DisplayData/Solar_Image/Clg_Solar_Image.json",
        "https://hpde.io/ASWS/DisplayData/Imaging_Riometer/Dav_Imaging_Riometer.json",
        "https://hpde.io/CCMC/Model/IRI-2016.json",
    ]
    all_errors = []
    for url in example_urls:
        frame_type = url.split("/")[4]
        frame = client.get_class_frame(frame_type)
        json_schema = convert_frame_to_schema(frame, client)

        # get data:
        response = requests.get(url)
        assert response.status_code == 200, f"Status code: {response.status_code}"

        data = response.json()["Spase"][frame_type]

        # validate data:
        errors = get_all_errors_for_spase(json_schema, data)
        all_errors.extend(
            [
                (
                    frame_type,
                    url,
                    error.message,
                    error.path,
                    error.instance,
                    error.validator,
                    error.validator_value,
                )
                for error in errors
            ]
        )
    columns = [
        "frame_type",
        "url",
        "message",
        "path",
        "instance",
        "validator",
        "validator_value",
    ]
    errors_df = pd.DataFrame(all_errors, columns=columns)
    return errors_df


def example_insert_data():
    dotenv.load_dotenv()

    team = os.getenv("TEAM")
    dbid = os.getenv("DATABASE_ID")
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    uri = f"http://{host}:{port}"
    client = WOQLClient(uri)
    client.connect(team=team, db=dbid)

    # get displaydata_schema:
    frame_type = "DisplayData"
    DisplayData_frame = client.get_class_frame(frame_type)
    json_schema = convert_frame_to_schema(DisplayData_frame, client)

    example_urls = [
        "https://hpde.io/ASWS/DisplayData/Solar_Image/Clg_Solar_Image.json",
        "https://hpde.io/ASWS/DisplayData/Imaging_Riometer/Dav_Imaging_Riometer.json",
        "https://hpde.io/CCMC/Model/IRI-2016.json",
    ]

    # get data:
    example_display_data = requests.get(example_urls[0]).json()["Spase"][frame_type]

    print(example_display_data)

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
    data_in_client = client.get_all_documents()
    print(data_in_client)


if __name__ == "__main__":
    errors_df = example_detect_errors()
    print(errors_df)
    example_insert_data()
