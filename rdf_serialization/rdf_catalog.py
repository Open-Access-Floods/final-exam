from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF, RDFS, XSD, DCTERMS as DCT, FOAF, PROV
import os

# Define Namespaces
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCAT3 = Namespace("http://www.w3.org/ns/dcat3#")
ADMS = Namespace("http://www.w3.org/ns/adms#")
CC = Namespace("http://creativecommons.org/ns#")
XSD_NS = Namespace("http://www.w3.org/2001/XMLSchema#") 
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
BRASIL = Namespace("https://github.com/Open-Access-Floods/final-exam/tree/main/processed_RS#")

# Initialize RDF Graph for the Catalog
catalog_g = Graph()

# Bind prefixes for cleaner Turtle output
catalog_g.bind("dcat", DCAT) 
catalog_g.bind("dcat3", DCAT3)
catalog_g.bind("dct", DCT)
catalog_g.bind("adms", ADMS)
catalog_g.bind("xsd", XSD_NS) 
catalog_g.bind("cc", CC)
catalog_g.bind("foaf", FOAF) 
catalog_g.bind("skos", SKOS)
catalog_g.bind("brasil", BRASIL) 
catalog_g.bind("prov", PROV) #provenace

# Define Catalog URI and Add Metadata 
catalog_uri = URIRef("https://github.com/Open-Access-Floods/final-exam/tree/main/processed_RS#") # Made URI more specific
catalog_g.add((catalog_uri, RDF.type, DCAT.Catalog))
catalog_g.add((catalog_uri, DCT.title, Literal("Brazil in Data: Disasters, Environment, and Society", lang="en")))
catalog_g.add((catalog_uri, DCT.description, Literal("Catalog containing the datasets for the Brazil in Data: Disasters, Environment, and Society project", lang="en")))

# Add the publisher information
publisher_uri = URIRef("https://github.com/Open-Access-Floods/final-exam/")
catalog_g.add((catalog_uri, DCT.publisher, publisher_uri))
catalog_g.add((publisher_uri, RDF.type, FOAF.Organization)) 
catalog_g.add((publisher_uri, FOAF.name, Literal("Open Access Project", lang="en"))) 

# Dates should use XSD.date for date literals
catalog_g.add((catalog_uri, DCT.issued, Literal("2025-01-01", datatype=XSD_NS.date)))
catalog_g.add((catalog_uri, DCT.modified, Literal("2025-05-27", datatype=XSD_NS.date))) 

# DCAT.language is preferred for the catalog language, using Lexvo URI for standard practice
catalog_g.add((catalog_uri, DCAT.language, URIRef("http://lexvo.org/id/iso639-1/en")))

# ADMS.identifier should use XSD.string if it's a plain string identifier
catalog_g.add((catalog_uri, ADMS.identifier, Literal("BRASIL_Catalog", datatype=XSD_NS.string)))

# Link to a theme taxonomy used by the catalog.
theme_taxonomy_uri = URIRef("http://publications.europa.eu/resource/authority/data-theme")
catalog_g.add((catalog_uri, DCAT.themeTaxonomy, theme_taxonomy_uri))
catalog_g.add((theme_taxonomy_uri, RDF.type, SKOS.ConceptScheme))
catalog_g.add((theme_taxonomy_uri, DCT.title, Literal(" Publications Office of the European Union Data Themes", lang="en")))
catalog_g.add((theme_taxonomy_uri, DCT.description, Literal("Data theme is a controlled vocabulary that lists concepts associated with themes used for dataset classification. Its main scope is to support activities associated with the Data Catalog Vocabulary application profile (DCAT-AP).  The concepts have been defined by the working group in charge of the revision of the DCAT-AP. Data theme is maintained by the Publications Office of the European Union and disseminated on the EU Vocabularies website.", lang="en")))

# New: Indicate if the catalog conforms to a specific standard or application profile.
dcat_ap_uri = URIRef("https://www.w3.org/TR/vocab-dcat-3/")
catalog_g.add((catalog_uri, DCT.conformsTo, dcat_ap_uri))

# Define and Link License Information
license_uri = URIRef("https://creativecommons.org/licenses/by/4.0/")
catalog_g.add((catalog_uri, DCT.license, license_uri))

# Add details about the Creative Commons license
catalog_g.add((license_uri, RDF.type, CC.License))
# CC.legalcode refers to the actual legal text of the license
catalog_g.add((license_uri, CC.legalcode, URIRef("https://creativecommons.org/licenses/by/4.0/legalcode"))) # Corrected legalcode URI

# Use the specific CC properties for permissions and requirements
catalog_g.add((license_uri, CC.permits, CC.Reproduction))
catalog_g.add((license_uri, CC.permits, CC.Distribution))
catalog_g.add((license_uri, CC.permits, CC.DerivativeWorks))
catalog_g.add((license_uri, CC.requires, CC.Notice))
catalog_g.add((license_uri, CC.requires, CC.Attribution))
catalog_g.add((license_uri, RDFS.label, Literal("Creative Commons Attribution 4.0 International", lang="en"))) 

# Add Specific Dataset IDs to the Catalog

catalog_g.add((catalog_uri, PROV.wasAttributedTo, URIRef("https://github.com/Open-Access-Floods/final-exam/")))

# List of dataset IDs as string literals
dataset_ids = [
    "D1_Disasters_and_Impact_Data",
    "D2_Rainfall",
    "D3_Population_Risk",
    "D4_Urban_Expansion",
    "D5_Deforestation",
    "D6_Civil_Defense",
    "MD1_Affected_Population",
    "MD2_Municipality_Rainfall",
    "MD3_Deforestation_RS",
    "MD4_Rain_Precipitation_States",
    "MD5_Monthly_Rainfall_Stations_RS",
    "MD6_Urbanization_Growth_RS"
]

# Add each dataset ID using the custom 'dcat3:dataset' property
for dataset_id in dataset_ids:
    catalog_g.add((catalog_uri, DCAT3.dataset, Literal(dataset_id))) 

## Saving the RDF Graph
output_dir = "rdf_serialization"  

# Create the output directory if it doesn't already exist
os.makedirs(output_dir, exist_ok=True)

# Define the full path for the catalog output file
catalog_file = os.path.join(output_dir, "serialization_catalog.ttl")

# Serialize the graph to Turtle format and write it to the file
with open(catalog_file, "w", encoding="utf-8") as f:
    f.write(catalog_g.serialize(format="turtle"))

# Inform the user that the serialization is complete
print(f"Serialization complete! Catalog file saved as: {catalog_file}")