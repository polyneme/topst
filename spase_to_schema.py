import requests
import json
import pandas as pd
import numpy as np
from typing import List, Dict, Tuple, Union, Optional, Any
from datetime import datetime as dt


# Simple types in spase (i.e not user defined types):
spase_to_terminus_types = {
    "Text": "str",
    "URL": "str",
    "DateTime": "dt.datetime",
    "Numeric": "float",
    "Duration": "dt.timedelta",
    "Count": "int",
    "ID": "str",
    "Item": "str",
}
# Below defines how many times a field can occur in a spase type
occurrence_map = {
    "0": "Optional[.]",
    "1": ".",
    "*": "Set[.]",  # this is optional
    "+": "List[.]",
    # TODO: check if this is correct with Donny
    "r": ".",
}


def get_json(url: Optional[str] = None) -> dict:
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
    json_data = response.json()
    return json_data


def get_all_available_data_types(
    json_data: dict,
) -> Tuple[Dict[str, Dict[str, Any]], pd.DataFrame]:
    """
    Get all available data types that needs to be defined in schema from the json file.

    Parameters
    ----------
    json_data : dict
        The json file.
    Returns
    -------
    all_available_data : pd.DataFrame
        The pandas dataframe of all available data types.
    """
    all_available_data = pd.DataFrame.from_dict(json_data["dictionary"], orient="index")
    return (
        json_data["ontology"],
        all_available_data,
    )


def preprocess_enum_str_for_py(enum_values: List[str]) -> List[str]:
    """
    Preprocess the enum values for python code.

    Parameters
    ----------
    enum_values : List[str]
        The list of enum values.
    Returns
    -------
    enum_py_values : List[str]
        The list of enum values for python code.
    """
    py_keywords = ["None"]
    to_replace = ["-", " ", "(", ")", "/", "."]
    enum_py_values = []

    for i in range(len(enum_values)):
        var_name = enum_values[i]
        var_def = enum_values[i]

        if len(var_name) == 0:
            print(enum_values)
            raise ValueError("Empty string in enum values")

        for r in to_replace:
            var_name = var_name.replace(r, "_")

        if var_name in py_keywords or var_name[0].isdigit():
            var_name = "_" + var_name
        enum_py_values.append(f"{var_name} = '{var_def}'")
    return enum_py_values


# given a row of container_elements, convert to python code:
def container_element_to_python_code(row: pd.Series) -> str:
    """
    Convert a row of container_elements to python code.

    Parameters
    ----------
    row : pd.Series
        A row of container_elements.
    Returns
    -------
    str
        The python code.
    """
    if row["spase_type"] == "Sequence":
        return ""
    
    if row["python_type"] is np.nan:
        element = '"' + row["element"] + '"' #TODO: If python is updated, use f-strings
        return f'{row["element"]} : {row["occurrence"].replace(".", element)}'
    
    return f'{row["element"]} : {row["occurrence"].replace(".",  row["python_type"])}'


def get_container_elements_code_from_json(
    container_def: Dict[str, Dict[str, Any]], all_available_data: pd.DataFrame
) -> Dict[str, str]:
    """
    Get the python code for each container from the json file.

    Parameters
    ----------
    container_def : Dict[str, Dict[str, Any]]
        The json file.
    all_available_data : pd.DataFrame
        The pandas dataframe of all available data types.
    Returns
    -------
    container_elements : pd.DataFrame
        The pandas dataframe of all available elements in each containers.
    """
    # flatten dict of dict & convert to dataframe:
    container_elements = pd.DataFrame(
        [
            container_def[container][element]
            for container in container_def
            for element in container_def[container]
        ]
    )
    # assert containers are correctly defined in dictionary:
    assert (
        container_elements["object"].isin(all_available_data.index).all()
    ), "Some containers are not defined in dictionary"

    assert container_elements["object"].nunique() == sum(
        all_available_data["type"] == "Container"
    ), "There are more containers in dictionary than in ontology"

    # assert elements are correctly defined in dictionary:
    assert (
        container_elements["element"].isin(all_available_data.index).all()
    ), "Some elements in containers are not defined in dictionary"

    # Map the type of the element to the type in dictionary:
    container_elements["spase_type"] = container_elements["element"].map(
        all_available_data["type"]
    )
    # Get the description of the element from dictionary:
    container_elements["description"] = container_elements["element"].map(
        all_available_data["definition"]
    )

    # Utils for python code for container elements:
    container_elements["python_type"] = container_elements["spase_type"].map(
        spase_to_terminus_types
    )
    # container_elements["python_type"] = container_elements["python_type"].fillna(
    #     container_elements["element"]
    # )

    container_elements["occurrence"] = container_elements["occurrence"].map(
        occurrence_map
    )

    # Get the python code for container elements:
    container_elements["python_element_code"] = container_elements.apply(
        container_element_to_python_code, axis=1
    )

    # combine python code for each container:
    container_element_code = lambda x: "\n\t".join(
        list(x.sort_values(by="reference")["python_element_code"])
    )

    containers = (
        container_elements.groupby("object").apply(container_element_code).to_dict()
    )

    return containers


def get_python_code_utils(
    container_def: Dict[str, Dict[str, Any]], all_available_data: pd.DataFrame
) -> None:
    """
    This function adds the python code utils to the all_available_data dataframe.
    Parameters
    ----------
    container_def : Dict[str, Dict[str, Any] ]
        The dictionary which contains the container definitions.

    all_available_data : pd.DataFrame
        The pandas dataframe of all available data types.

    """

    container_elements_py = get_container_elements_code_from_json(
        container_def, all_available_data
    )

    python_code_utils = {
        "Container": {
            "element_code": lambda x: container_elements_py[x.name],
            "class_type": "DocumentTemplate",
        },
        "Enumeration": {
            "element_code": lambda x: "\n\t".join(
                preprocess_enum_str_for_py(x["allowedValues"])
            ),
            "class_type": "EnumTemplate",
        },
    }

    for key in python_code_utils:
        all_available_data.loc[
            all_available_data["type"] == key, "python_elements_code"
        ] = all_available_data.loc[all_available_data["type"] == key].apply(
            lambda x: python_code_utils[key]["element_code"](x), axis=1
        )
        all_available_data.loc[
            all_available_data["type"] == key, "class_type"
        ] = python_code_utils[key]["class_type"]

    # Return only non-null values:
    code_class = all_available_data[
        all_available_data["python_elements_code"].notnull()
    ]
    return code_class


# TODO: Fix this function
def python_code_for_class(row: pd.Series) -> str:
    """
    Convert a row of container to python code.

    Parameters
    ----------
    row : pd.Series
        A row of container.
    Returns
    -------
    str
        The python code.
    """
    # index is the container name
    script = f'class {row.name}({row["class_type"]}):'
    # add description:
    script += f'\n\t"""{row["definition"]}"""'
    # add schema:
    script += "\n\t_schema=schema\n"
    script += "\n\t"
    # add the element code:
    script += row["python_elements_code"]
    return script

#TODO: Return Intial Python Code from a function
def generate_python_schema_code(
    all_available_data: pd.DataFrame,
) -> str:
    """
    Generate the python code for the schema.

    Parameters
    ----------
    all_available_data : pd.DataFrame
        The pandas dataframe of all available data types.
    Returns
    -------
    str
        The python code for the schema.
    """

    python_script = '\nfrom typing import  Set, Optional, List\nimport datetime as dt\nfrom terminusdb_client import Client\nfrom terminusdb_client.woqlschema.woql_schema import (DocumentTemplate,EnumTemplate,WOQLSchema,LexicalKey,\n)\nimport pandas as pd\nfrom tqdm import tqdm\nimport tempfile\nimport random\nschema = WOQLSchema()\n'

    container_def, all_available_data = get_all_available_data_types(get_json())
    code_class = get_python_code_utils(container_def, all_available_data)
    # Get the python code for each container:
    code_list = code_class.apply(python_code_for_class, axis=1).to_list()
    # combine python code for each container:
    python_script += "\n\n".join(code_list)
    return python_script

def save_code_file(code: str, file_name: str) -> None:
    """
    Save the python code to a file.

    Parameters
    ----------
    code : str
        The python code.
    file_name : str
        The file name.
    """
    assert file_name.endswith(".py"), "File name must end with .py"
    with open(file_name, "w") as f:
        f.write(code)

if __name__ == "__main__":
    code = generate_python_schema_code(get_json())
    save_code_file(code, "terminus_schema/schema.py")
    print("Schema file saved to /terminus_schema/schema.py")