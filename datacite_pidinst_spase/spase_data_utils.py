import requests
import json
import xmltodict
from typing import List, Dict, AnyStr, Any


def get_data_github_api(user: AnyStr, repo: AnyStr, branch: AnyStr) -> Dict:
    GITHUB_API: AnyStr = f"https://api.github.com/repos/{user}/{repo}/git/trees/{branch}?recursive=1"
    response: requests.Response = requests.get(GITHUB_API)
    return response.json()

def filter_xml_file(tree: Dict) -> bool:
    return tree['path'].endswith('.xml')

def list_xml_files(tree: Dict) -> List:
    return list(filter(filter_xml_file, tree['tree']))

def get_xml_data_from_github(user: str, repo: str, branch: str, path: str) -> str:
    url = f'https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path}'
    response: requests.Response = requests.get(url)
    return response.text

def save_xml_file(xml_data: str, path: str) -> None:
    with open(path, 'w') as f:
        f.write(xml_data)

def get_xml_data_from_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()
    
def parse_xml_data_to_dict(xml_data: str) -> Dict:
    return xmltodict.parse(xml_data, process_namespaces=True)

def save_json_file(data: Dict, path: str) -> None:
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
def main():
    #Define the GitHub API endpoint:
    USER = "hpde"
    REPO = "hpde.io"
    BRANCH = "master"
    # Get the data from the GitHub API
    data = get_data_github_api(USER, REPO, BRANCH)
    # Get the XML files
    xml_files = list_xml_files(data)
    print(xml_files[2]['path'])
    # Get the XML data from the GitHub API
    xml_data = get_xml_data_from_github(USER, REPO, BRANCH, xml_files[0]['path'])
    print(xml_data)
    # save the xml data to a file
    save_xml_file(xml_data, 'data.xml')
    # Parse the XML data
    print(json.dumps(xmltodict.parse(xml_data, process_namespaces=True), indent=4))
    # Save the json data to a file
    with open('data.json', 'w') as f:
        f.write(json.dumps(xmltodict.parse(xml_data, process_namespaces=True), indent=4))

    

# if __name__ == "__main__":
#     print("Hello, World!")
#     main()
