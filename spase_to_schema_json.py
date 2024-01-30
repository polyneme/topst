import json
import requests
from typing import List, Dict, Tuple, Union, Optional, Any
import pandas as pd
from pathlib import Path
import os
from terminusdb_client import WOQLClient, GraphType



spase_to_terminus_json_types = {
    "Text": "xsd:string",
    "URL": "xsd:string",
    "DateTime": "xsd:dateTime",
    "Numeric": "xsd:float",
    "Duration": "xsd:duration",
    "Count": "xsd:integer",
    "ID": "xsd:string",
    "Item": "xsd:string",
    # TODO: check if this is correct with Donny
    "Sequence": "xsd:string",
}
occurrence_map = {
    "0": "Optional",
    # "1": ".",
    "*": "Set",  # this is optional
    "+": "List",
    # TODO: check if this is correct with Donny
    "r": "Optional",
}


def get_sub_dictonary(dictionary: dict, keys: List[str]) -> dict:
    """
    Get the sub dictionary from the dictionary. The sub dictionary will only contain the keys specified.

    Parameters
    ----------
    dictionary : dict
        The dictionary to get the sub dictionary from.
    keys : list
        The keys of the sub dictionary.

    Returns
    -------
    dict
        The sub dictionary.
    """
    return {key: dictionary[key] for key in keys}


def get_spase_model(url: Optional[str] = None) -> dict:
    """
    Get the json file from the spase website.

    Parameters
    ----------
    url : str
        The url of the json file.
    Returns
    -------
    dict
        The json file.
    """
    if url is None:
        url = "https://spase-group.org/data/model/spase-2.6.0.json"

    # TODO: confirm if the schema is latest version, if not then warn user

    response: requests.Response = requests.get(url)
    spase_model = response.json()
    return spase_model


def get_all_documentation(data_dictonary: pd.DataFrame) -> Dict:
    """
    Get all the documentation & types from the spase model for each item.

    """
    data_dictonary["@class"] = data_dictonary["type"].map(spase_to_terminus_json_types)
    # where null replace with primary key:
    data_dictonary["@class"].fillna(data_dictonary.index.to_series(), inplace=True)

    return data_dictonary["definition"].to_dict(), data_dictonary[["@class"]].to_dict(
        "index"
    )


def get_class_schema(container, data_documentation, data_type_defination, spase_model):
    """
    Get the schema for a class.
    """

    class_schema = {
        "@type": "Class",
        "@id": container.name,
        "@documentation": {
            "@comment": container["definition"],
            "@properties": get_sub_dictonary(
                data_documentation, container["subElements"]
            ),
        },
    }
    # dict of dict: "index": {"@class": class_}
    subclasses_type = get_sub_dictonary(data_type_defination, container["subElements"])
   
    for key in spase_model["ontology"][container.name]:
        occurrence = spase_model["ontology"][container.name][key]["occurrence"]
        if occurrence_map.get(occurrence):
            subclasses_type[key]["@type"] = occurrence_map[occurrence]
        else:
            # TODO: change this
            subclasses_type[key] = subclasses_type[key]["@class"]

    class_schema = class_schema | subclasses_type
    return class_schema


def get_all_enums_schema(enums: pd.DataFrame) -> List[dict]:
    """
    Get the schema for all the enums.
    """
    enums.loc[:, "@type"] = "Enum"
    enums.reset_index(inplace=True)
    enums.rename(columns={"index": "@id", "allowedValues": "@value"}, inplace=True)
    enums_list = enums[["@type", "@id", "@value"]].to_dict("records")
    return enums_list


def get_all_classes_schema(
    containers: pd.DataFrame, data_documentation, data_class_types, spase_model
):
    """
    Get the schema for all the classes.
    """
    containers["schema"] = containers.apply(
        lambda x: get_class_schema(
            x, data_documentation, data_class_types, spase_model
        ),
        axis=1,
    )
    return containers["schema"].to_list()


def save_json(json_file_name: str, json_file_data: List[Dict]) -> Path:
    with open(json_file_name, "w") as f:
        json.dump(json_file_data, f, indent=4)
    return Path(json_file_name)


def get_context() -> Dict:
    # TODO: Update the context from fetched schema
    context = {
        "@type": "@context",
        "@base": "https://spase-group.org/data/",
        "@schema": "http://www.spase-group.org/data/schema",
    }
    return context


def create_terminus_db_schema_json():
    """
    Create schema json for teminus db.
    """
    spase_model = get_spase_model()
    data_dictonary = pd.DataFrame.from_dict(spase_model["dictionary"], orient="index")

    enums = data_dictonary[data_dictonary["type"] == "Enumeration"]
    enums_schema = get_all_enums_schema(enums)

    containers = data_dictonary[data_dictonary["type"] == "Container"]

    data_documentation, data_class_types = get_all_documentation(data_dictonary)

    containers_schema = get_all_classes_schema(
        containers, data_documentation, data_class_types, spase_model
    )
    # merge the above two lists and save:
    context = get_context()
    schema_json = [context, *enums_schema, *containers_schema]

    return schema_json
    


def create_and_save_json(file_path: str = None) -> Path:
    """
    Create the json file  and save the json file for the schema.
    """
    if file_path is None:
        file_path = os.getenv("TERMINUS_SCHEMA_FILE_PATH")
    
    assert file_path is not None, "Please provide the file path for the schema json file either through enviroment variable or argument."

    schema_json = create_terminus_db_schema_json()
    path = save_json(file_path, schema_json)
    assert path.exists(), "The file path does not exist."
    return path

def read_json_file(file_path):
    """
    Read the json file and returns the json file.
    """
    with open(file_path, "r") as f:
        schema_json = json.load(f)
    return schema_json


def create_terminus_db_from_schema(schema, dbid, team="admin", host="127.0.0.1", port="6363", on_exists_delete=False):
    """
    Create the terminus database with the schema and returns the connection to the database as well as classes created.
    """
    uri = f"http://{host}:{port}"
    client = WOQLClient(uri)
    client.connect(team=team)
    exists = client.has_database(dbid)
    if exists:
        print(f"Database {dbid} already exists!")
        if on_exists_delete:
            print("Delete the database first!")
            client.delete_database(dbid, force=True)
        else:
           print("Use on_exists_delete=True to delete the database!")
           return
        
    client.create_database(dbid, team=team)
    
    results = client.insert_document(
        schema, graph_type=GraphType.SCHEMA, full_replace=True
    )
    return client, results
