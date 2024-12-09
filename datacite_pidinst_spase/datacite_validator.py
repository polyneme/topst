import requests
from lxml import etree
import logging
from typing import Tuple, Optional
from io import BytesIO
import urllib.parse

class DataCiteValidator:
    SCHEMA_URLS = {
        "4.4": "https://schema.datacite.org/meta/kernel-4.4/metadata.xsd",
        "4.5": "https://schema.datacite.org/meta/kernel-4.5/metadata.xsd",
        "pidinst": "https://raw.githubusercontent.com/rdawg-pidinst/schema/refs/heads/master/support/pidinst-schema-1_0.xsd"
    }
    
    def __init__(self, schema_version: str = "4.5"):
        if schema_version not in self.SCHEMA_URLS:
            raise ValueError(f"Unsupported schema version. Choose from: {', '.join(self.SCHEMA_URLS.keys())}")
            
        self.schema_version = schema_version
        
        class SchemaResolver(etree.Resolver):
            def __init__(self, schema_version):
                self.schema_version = schema_version
            
            def resolve(self, url, pubid, context):
                try:
                    # Handle different base URLs based on schema type
                    if self.schema_version.startswith('4.'):
                        # DataCite schemas
                        if not url.startswith('http'):
                            base_url = f"https://schema.datacite.org/meta/kernel-{self.schema_version}/"
                            full_url = urllib.parse.urljoin(base_url, url)
                        else:
                            full_url = url
                    elif self.schema_version == 'pidinst':
                        # PIDINST schema
                        if not url.startswith('http'):
                            base_url = "https://raw.githubusercontent.com/rdawg-pidinst/schema/refs/heads/master/support/"
                            full_url = urllib.parse.urljoin(base_url, url)
                        else:
                            full_url = url
                    
                    response = requests.get(full_url)
                    response.raise_for_status()
                    return self.resolve_string(response.text, context)
                except Exception as e:
                    logging.error(f"Could not resolve schema include: {url}")
                    return None

        # Fetch main schema
        schema_url = self.SCHEMA_URLS[schema_version]
        response = requests.get(schema_url)
        
        # Create parser with custom resolver
        parser = etree.XMLParser()
        parser.resolvers.add(SchemaResolver(schema_version))
        
        # Parse schema with resolver
        try:
            schema_tree = etree.parse(BytesIO(response.content), parser)
            self.validator = etree.XMLSchema(schema_tree)
        except etree.XMLSchemaParseError as e:
            logging.error(f"Schema parsing error: {e}")
            raise
    
    def validate_xml(self, xml_content: bytes) -> Tuple[bool, Optional[str]]:
        """
        Validate XML content against DataCite schema.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            xml_doc = etree.fromstring(xml_content)
            self.validator.assertValid(xml_doc)
            return True, None
        except etree.DocumentInvalid as e:
            return False, str(e)
        except etree.XMLSyntaxError as e:
            return False, f"XML parsing error: {str(e)}"