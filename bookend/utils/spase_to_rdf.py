import glob
import importlib
import subprocess
import os
import uuid
import warnings
from enum import Enum
from pathlib import Path
from typing import List, Optional
from rdflib import Graph, URIRef, Literal, RDF, RDFS, OWL, XSD, BNode, DC
from rdflib.collection import Collection
import inspect
import re

from tqdm import tqdm
from xsdata.exceptions import ConverterWarning
from xsdata.formats.dataclass.parsers import XmlParser

PY_TO_XSD_TYPES = {
    int: XSD.int,
    Optional[int]: XSD.int,
    List[int]: XSD.int,
    float: XSD.double,
    Optional[float]: XSD.double,
    List[float]: XSD.double,
    str: XSD.string,
    Optional[str]: XSD.string,
    List[str]: XSD.string,
    bool: XSD.boolean,
    Optional[bool]: XSD.boolean,
    List[bool]: XSD.boolean
}

XS_DATA_TYPES_MAP = {
    "XmlDate": XSD.date,
    "XmlDateTime": XSD.dateTime,
    "XmlTime": XSD.time,
    "XmlDuration": XSD.duration,
}


def create_python_model_from_xsd(xsd_file_path, output_module):
    """Creates Python model from XSD file using xsdata"""
    # Check if xsdata is installed
    try:
        # Check if the xsdata command is available
        subprocess.run(["xsdata", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("xsdata is not installed. Please install xsdata to use this function.")
        return

    # Check if the XSD file exists
    if not os.path.isfile(xsd_file_path):
        print(f"XSD file not found: {xsd_file_path}")
        return

    # Create the output directory if it doesn't exist
    os.makedirs(output_module, exist_ok=True)

    # Generate Python code from XSD file using xsdata
    subprocess.run(["xsdata", "generate", "-p", output_module, xsd_file_path], check=True)

    print(f"Python model created in: {output_module}")


def create_owl_from_python_module(python_module_name: str, output_file):
    """Creates OWL Ontology using python module"""
    g = Graph()

    external_module = importlib.import_module(python_module_name)
    # Iterate over classes in the module
    for name, obj in inspect.getmembers(external_module, inspect.isclass):
        if hasattr(obj, '__annotations__') and hasattr(obj, '__dataclass_fields__') and hasattr(obj,
                                                                                                '__dataclass_params__'):
            # Check if the class is a dataclass
            # Create subject URI
            subject_uri = URIRef(f"http://www.spase-group.org/data/schema/{obj.__name__}")

            # Add type triple
            g.add((subject_uri, RDF.type, URIRef(f"http://www.w3.org/2002/07/owl#Class")))
            g.add((subject_uri, RDFS.label, Literal(obj.__name__)))
            g.add((subject_uri, RDFS.comment, Literal(obj.__doc__)))

            # Add triples for each dataclass field
            for field_name, field in obj.__dataclass_fields__.items():
                if field_name in obj.__annotations__:
                    if field.type == List:
                        for item in getattr(obj, field_name):
                            # print(field_name)
                            pass
                    elif field_name.endswith("id") and field_name != "prior_id":
                        target = "".join(x.capitalize() for x in field_name.replace("_id", "").lower().split("_"))
                        object_property_name = "has_" + field_name[:1].lower() + field_name[1:].replace("_id", "")
                        object_property = URIRef(f"http://www.spase-group.org/data/schema/{object_property_name}")
                        g.add((object_property, RDFS.subPropertyOf, OWL.topObjectProperty))
                        g.add((object_property, RDFS.label, Literal(object_property_name)))
                        g.add((object_property, RDFS.domain, subject_uri))
                        g.add((object_property, RDFS.range,
                               URIRef(f"http://www.spase-group.org/data/schema/{target}")))
                    else:
                        matches = re.search(r"\[([^\]]+)\]", str(obj.__annotations__[field_name]))
                        target = matches.group(1).split('.')[-1] if matches else str(obj.__annotations__[field_name])
                        if target in ["float", "int", "str", "bool", "<class 'str'>"] or target in XS_DATA_TYPES_MAP:
                            data_property_name = field_name[:1].lower() + field_name[1:]
                            data_property = URIRef(f"http://www.spase-group.org/data/schema/{data_property_name}")
                            g.add((data_property, RDFS.subPropertyOf, OWL.topDataProperty))
                            g.add((data_property, RDFS.label, Literal(data_property_name)))
                            g.add((data_property, RDFS.domain, subject_uri))
                            target_type = PY_TO_XSD_TYPES[obj.__annotations__[field_name]] if obj.__annotations__[
                                                                                                  field_name] in PY_TO_XSD_TYPES else \
                                XS_DATA_TYPES_MAP[target]
                            g.add((data_property, RDFS.range, URIRef(target_type)))
                        else:
                            object_property_name = "has_" + field_name[:1].lower() + field_name[1:]
                            object_property = URIRef(f"http://www.spase-group.org/data/schema/{object_property_name}")
                            g.add((object_property, RDFS.subPropertyOf, OWL.topObjectProperty))
                            g.add((object_property, RDFS.label, Literal(object_property_name)))
                            g.add((object_property, RDFS.domain, subject_uri))
                            g.add((object_property, RDFS.range,
                                   URIRef(f"http://www.spase-group.org/data/schema/{target}")))
        else:
            subject_uri = URIRef(f"http://www.spase-group.org/data/schema/{obj.__name__}")
            list_node = BNode()
            # Add type triple
            g.add((subject_uri, RDF.type, OWL.Class))
            g.add((subject_uri, RDFS.label, Literal(obj.__name__)))
            g.add((subject_uri, RDFS.comment, Literal(obj.__doc__)))
            for enum_name in list(obj.__members__.keys()):
                g.add((URIRef(f"http://www.spase-group.org/data/schema/{enum_name}"), RDF.type, OWL.NamedIndividual))
                g.add((URIRef(f"http://www.spase-group.org/data/schema/{enum_name}"), RDF.type, subject_uri))
                g.add((URIRef(f"http://www.spase-group.org/data/schema/{enum_name}"), RDFS.label,
                       Literal(obj.__members__[enum_name].value)))
            collection = Collection(g, list_node, [URIRef(f"http://www.spase-group.org/data/schema/{name}") for name in
                                                   list(obj.__members__.keys())])
            g.add((subject_uri, OWL.oneOf, list_node))
    # Serialize the RDF graph to a file
    g.add((URIRef("http://www.spase-group.org/data/schema/"), RDF.type, OWL.Ontology))
    g.add((URIRef("http://www.spase-group.org/data/schema/"), RDFS.label, Literal("Spase Group Ontology")))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        g.serialize(destination=output_file, format='pretty-xml')


def rdfize_obj(obj, g: Graph, obj_uuid=''):
    obj_uri = ''
    obj_name = ''
    if hasattr(obj, "resource_id"):
        obj_name = str(obj.resource_id.strip().replace('spase://', '')).replace('/', '_').replace(" ", "_").replace('.',
                                                                                                                    '_')
        obj_uri = URIRef(f"http://www.spase-group.org/data/schema/{obj_name}")
        g.add((obj_uri, DC.identifier, Literal(str(obj.resource_id))))
    else:
        obj_uuid = str(uuid.uuid4()) if obj_uuid == '' else obj_uuid
        obj_uri = URIRef(f"http://www.spase-group.org/data/schema/{obj.__class__.__name__}-{obj_uuid}")
        obj_name = f"{obj.__class__.__name__}-{obj_uuid}"

    class_uri = URIRef(f"http://www.spase-group.org/data/schema/{obj.__class__.__name__}")
    g.add((obj_uri, RDF.type, class_uri))
    g.add((obj_uri, RDFS.label, Literal(obj_name)))
    for member_name, member_value in vars(obj).items():
        if issubclass(member_value.__class__, Enum):
            # print('im enum')
            pass
        else:
            type_hint = obj.__class__.__annotations__.get(member_name)
            # print(type_hint)
            # print(f"Member: {member_name}, Value: {member_value}, Type: {type_hint}")
            if "model.spase_2_6_0." in str(
                    type_hint) and member_value is not None and member_value != [] and not isinstance(member_value,
                                                                                                      str):
                # print(f"a class {member_name}")
                object_property_name = "has_" + member_name[:1].lower() + member_name[1:]
                predicate_uri = URIRef(f"http://www.spase-group.org/data/schema/{object_property_name}")
                if "List" in str(type_hint):
                    for member in member_value:
                        process_member(member, obj_uri, predicate_uri, g)
                else:
                    process_member(member_value, obj_uri, predicate_uri, g)
            elif member_name.endswith("_id") and member_name != "prior_id" and member_value is not None:
                object_property_name = "has_" + member_name[:1].lower() + member_name[1:].replace("_id", "")
                if isinstance(member_value, list):
                    for member_subvalue in member_value:
                        member_uri = URIRef(
                            f"http://www.spase-group.org/data/schema/{str(member_subvalue.strip().replace('spase://', '')).replace('/', '_').replace(' ', '_').replace('.', '_')}")
                        predicate_uri = URIRef(f"http://www.spase-group.org/data/schema/{object_property_name}")
                        member_class = "".join(
                            x.capitalize() for x in member_name.replace("_id", "").lower().split("_"))
                        g.add((member_uri, RDF.type, URIRef(f"http://www.spase-group.org/data/schema/{member_class}")))
                        g.add((obj_uri, predicate_uri, URIRef(member_uri)))
                else:
                    member_uri = URIRef(
                        f"http://www.spase-group.org/data/schema/{str(member_value.strip().replace('spase://', '')).replace('/', '_').replace(' ', '_').replace('.', '_')}")
                    predicate_uri = URIRef(f"http://www.spase-group.org/data/schema/{object_property_name}")
                    g.add((obj_uri, predicate_uri, URIRef(member_uri)))
            elif member_value is not None:
                object_property_name = member_name[:1].lower() + member_name[1:]
                predicate_uri = URIRef(f"http://www.spase-group.org/data/schema/{object_property_name}")
                if isinstance(member_value, list):
                    for member_subvalue in member_value:
                        data_type = PY_TO_XSD_TYPES[type(member_subvalue)] if type(
                            member_subvalue) in PY_TO_XSD_TYPES else XS_DATA_TYPES_MAP[
                            str(member_subvalue.__class__.__name__).replace("xsdata.models.datatype.", "")]
                        g.add((obj_uri, predicate_uri, Literal(member_subvalue, datatype=data_type)))
                else:
                    data_type = PY_TO_XSD_TYPES[type(member_value)] if type(member_value) in PY_TO_XSD_TYPES else \
                        XS_DATA_TYPES_MAP[str(member_value.__class__.__name__).replace("xsdata.models.datatype.", "")]
                    g.add((obj_uri, predicate_uri, Literal(member_value, datatype=data_type)))


def process_member(member, obj_uri, predicate_uri, g):
    if hasattr(member.__class__, "__members__"):
        g.add((obj_uri, predicate_uri, URIRef(
            f"http://www.spase-group.org/data/schema/{member.name}")))
        return
    elif hasattr(member, "resource_id"):
        member_name = str(member.resource_id.strip().replace('spase://', '')).replace('/', '_').replace(" ",
                                                                                                        "_").replace(
            '.', '_')
        member_uri = URIRef(
            f"http://www.spase-group.org/data/schema/{member_name}")
        rdfize_obj(member, g, '')
    else:
        member_uuid = str(uuid.uuid4())
        member_uri = URIRef(
            f"http://www.spase-group.org/data/schema/{member.__class__.__name__}-{member_uuid}")
        rdfize_obj(member, g, member_uuid)
    g.add((obj_uri, predicate_uri, member_uri))


def parse_xml_file(xml_file_path, clazz):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ConverterWarning)
        xml_string = Path(xml_file_path).read_text()
        parser = XmlParser()
        return parser.from_string(xml_string, clazz)


def xml_to_rdf(root_path, module, output_path, partition_number=1):
    """Converts all tehj XML files on a path to RDF"""

    g = Graph()
    file_count = 0
    current_out_file = 0

    module = importlib.import_module(module)
    spase_class = getattr(module, 'Spase')
    # Get a list of all XML files in the specified path and its subdirectories
    xml_files = glob.glob(os.path.join(root_path, '**/*.xml'), recursive=True)

    # Determine the number of files for each output (one third of total files)
    num_files = len(xml_files)
    files_per_output = num_files // partition_number

    # Iterate through XML files using tqdm for progress tracking
    for xml_file in tqdm(xml_files, desc="Processing XML files"):
        if "Deprecated" in xml_file or "sitemap" in xml_file:
            continue
        try:
            order = parse_xml_file(xml_file, spase_class)
        except Exception as e:
            print(f"Error processing {xml_file}: {e}")
            continue

        try:
            rdfize_obj(order, g)
            file_count += 1
        except Exception as e:
            print(f"Error rdfizing {xml_file}: {e}")
            continue

        if file_count % files_per_output == 0:
            current_out_file += 1
            output_filename = f'{output_path}/spase_{current_out_file}.ttl' if partition_number > 1 else f'{output_path}/spase.ttl'
            g.serialize(destination=output_filename, format='turtle')
            # Clear the graph to start a new one for the next batch
            g = Graph()

    # Serialize any remaining data in the graph after processing all XML files
    if g:
        current_out_file += 1
        output_filename = f'{output_path}/spase_{current_out_file}.ttl'
        g.serialize(destination=output_filename, format='turtle')
