import json
import requests
from typing import List, Dict, Tuple, Union, Optional, Any
import pandas as pd
import numpy as np
from pathlib import Path


spase_to_terminus_json_types = {
    "Text": "xsd:string",
    "URL": "xsd:string",
    "DateTime": "xsd:dateTime",
    "Numeric": "xsd:float",
    "Duration": "xsd:duration",
    "Count": "xsd:integer",
    "ID": "xsd:string",
    "Item": "xsd:string",
    #TODO: check if this is correct with Donny
    "Sequence": "xsd:string"
   
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
    data_dictonary["@class"] = data_dictonary['type'].map(spase_to_terminus_json_types)
    # where null replace with primary key:
    data_dictonary["@class"].fillna(data_dictonary.index.to_series(), inplace=True)
  
    return data_dictonary['definition'].to_dict(), data_dictonary[['@class']].to_dict('index')


def get_class_schema(container, data_documentation, data_type_defination, spase_model):
    """
    Get the schema for a class.   
    """

    class_schema = {
       "@type": "Class",
       "@id": container.name,
          "@documentation" : {
          "@comment" : container["definition"],
          "@properties":  get_sub_dictonary(data_documentation, container['subElements']),
          },
   }
    # dict of dict: "index": {"@class": class_}
    subclasses_type  = get_sub_dictonary(data_type_defination, container['subElements'])
    ## Get occurance from ontology here:
    #spase_model['ontology'][container.name]
    for key in spase_model['ontology'][container.name]:
        occurrence = spase_model['ontology'][container.name][key]['occurrence']
        if occurrence_map.get(occurrence):
            subclasses_type[key]["@type"] = occurrence_map[occurrence]
        else:
            #TODO: change this
            subclasses_type[key] = subclasses_type[key]['@class']

    class_schema = class_schema | subclasses_type
    return class_schema

def get_all_enums_schema(enums:pd.DataFrame)-> List[dict]:
    enums.loc[:, "@type"] = "Enum"
    enums.reset_index(inplace=True)
    enums.rename(columns={"index": "@id", "allowedValues": "@value"}, inplace=True)
    enums_list = enums[['@type', "@id", "@value"]].to_dict('records')
    return enums_list

def get_all_classes_schema(containers:pd.DataFrame, data_documentation, data_class_types, spase_model):
    containers['schema'] = containers.apply(lambda x: get_class_schema(x, data_documentation, data_class_types, spase_model), axis=1)
    return containers['schema'].to_list()

def save_json(json_file_name: str, json_file_data: List[Dict])-> Path:
    with open(json_file_name, "w") as f:
        json.dump(json_file_data, f, indent=4)
    return Path(json_file_name)
    

def get_context() -> Dict:
    #TODO: Update the context from fetched schema
    context={
            "@type": "@context",
            "@base": "https://spase-group.org/data/",
            "@schema": "http://www.spase-group.org/data/schema",
        }
    return context

def create_and_save_json():
    """
    Create the json file  and save the json file for the schema.
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
    schema_json = [context, *enums_schema,*containers_schema]
    file_name = "/home/helio/terminus-db-schema/topst-ssh/schema.json"
    path = save_json(file_name, schema_json)
    assert path.exists()
    #return file path:
    return path
