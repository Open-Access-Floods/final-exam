from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF, XSD, DCTERMS as DCT
import os

# Definir namespaces
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace("http://purl.org/dc/terms/")
FOAF_NS = Namespace("http://xmlns.com/foaf/0.1/")
XSD_NS = Namespace("http://www.w3.org/2001/XMLSchema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

# Data: List of dataset dictionaries (mas fácil para manipular)
datasets_list = [
    {  # D6_Civil_Defense dataset 
        "id": "D6_Civil_Defense",
        "uri": "https://portaldatransparencia.gov.br/graficos/incorporar/acao-especifica/evolucao-historica/linhas?codigoAcao=22BO",
        "title": "Evolução histórica dos gastos – Ação 22BO (Ações de Proteção e Defesa Civil)",
        "description": "Dados consolidados de execução orçamentária da Ação 22BO entre os anos de 2014 e 2025, extraídos do Portal da Transparência. Inclui valores empenhados, liquidados e pagos.",
        "publisher_uri": "https://www.gov.br/cgu",
        "publisher_name": "Controladoria-Geral da União", 
        "creator_uri": "https://www.gov.br/midr",
        "creator_name": "Ministério da Integração e do Desenvolvimento Regional",
        "language": "pt",
        "issued_date": "2014-01-01",
        "modified_date": "2025-01-01",
        "temporal_coverage": {
            "start_date": "2014-01-01",
            "end_date": "2025-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "license_uri": "https://dados.gov.br/politica-de-dados-abertos-da-administracao-publica-federal",
        "keywords": [
            "gastos públicos", "orçamento", "defesa civil",
            "ações emergenciais", "desastres naturais", "transparência pública"
        ],
        "subject": { 
            "uri": " http://publications.europa.eu/resource/authority/subject-matter/PCIV",
            "label": "Civil Protection"
        }
    },
    # D5_Deforestation dataset, but english content, mapped to pt language)
    {
        "id": "D5_Deforestation",
        "uri": "https://doi.org/10.58053/MapBiomas/7STHCP",
        "title": "Deforestation and secondary vegetation statistics by municipalities and states - MapBiomas Brasil Collection 9",
        "description": "Area data (ha) of deforestation and secondary vegetation by land cover class for municipality and state segments from 1985 to 2023",
        "publisher_uri": "https://data.mapbiomas.org/dataverse/brazil",
        "publisher_name": "MapBiomas", 
        "creator_uri": "https://data.mapbiomas.org/dataverse/brazil",
        "creator_name": "MapBiomas", 
        "language": "pt",
        "issued_date": "2023-12-31",
        "modified_date": "2025-01-21",
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": ["Deforestation", "Secondary Vegetation", "Statistics", "Brazilian states", "Brazilian municipalities"],
        "subject": { 
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environmental Science"
        }
    },
    # D4_Urban_Expansion dataset (English content, mapped to pt language)
    {
        "id": "D4_Urban_Expansion",
        "uri": "https://doi.org/10.58053/MapBiomas/2W2Z5M",
        "title": "Coverage and transitions statistics by states and municipalities - MapBiomas Brasil Collection 9",
        "description": "Area data (ha) of land cover class for states and municipalities from 1985 to 2023, based on MapBiomas Brazil Collection 9",
        "publisher_uri": "https://data.mapbiomas.org/dataverse/brazil",
        "publisher_name": "MapBiomas",
        "creator_uri": "https://data.mapbiomas.org/dataverse/brazil",
        "creator_name": "MapBiomas",
        "language": "pt",
        "issued_date": "2023-12-31",
        "modified_date": "2025-01-21",
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": ["Land Cover", "Transitions", "Statistics", "Brazilian states", "Brazilian municipalities"],
        "subject": {
            "uri": " http://publications.europa.eu/resource/authority/data-theme/SOCI",
            "label": "Population and Society"
        }
    }
]

# Create a new RDF graph
g = Graph()

# Bind prefixes to the graph 
g.bind("dcat", DCAT)
g.bind("dct", DCT)
g.bind("foaf", FOAF_NS)
g.bind("xsd", XSD_NS)
g.bind("skos", SKOS)

# Process each dataset in the list of dictionaries
for data in datasets_list:
    dataset_uri = URIRef(data["uri"])

    # Add triples for the dataset
    g.add((dataset_uri, RDF.type, DCAT.Dataset))

    # Title and Description with language tag
    if data.get("title"):
        content_lang = data.get("language")
        if content_lang:
            g.add((dataset_uri, DCT.title, Literal(data["title"], lang=content_lang)))
        else:
            g.add((dataset_uri, DCT.title, Literal(data["title"])))

    if data.get("description"):
        content_lang = data.get("language")
        if content_lang:
            g.add((dataset_uri, DCT.description, Literal(data["description"], lang=content_lang)))
        else:
            g.add((dataset_uri, DCT.description, Literal(data["description"])))

    # Publisher
    if data.get("publisher_uri"):
        publisher_uri = URIRef(data["publisher_uri"])
        g.add((dataset_uri, DCT.publisher, publisher_uri))
        # Add FOAF Person/Organization for publisher
        g.add((publisher_uri, RDF.type, FOAF_NS.Agent))
        if data.get("publisher_name"):
            g.add((publisher_uri, FOAF_NS.name, Literal(data["publisher_name"])))

    # Creator
    if data.get("creator_uri"):
        creator_uri = URIRef(data["creator_uri"])
        g.add((dataset_uri, DCT.creator, creator_uri))
        g.add((creator_uri, RDF.type, FOAF_NS.Agent))
        if data.get("creator_name"):
            g.add((creator_uri, FOAF_NS.name, Literal(data["creator_name"])))

    # Language
    if data.get("language"):
        g.add((dataset_uri, DCT.language, URIRef(f"http://lexvo.org/id/iso639-1/{data['language']}")))

    # Issued and Modified Dates
    if data.get("issued_date"):
        g.add((dataset_uri, DCT.issued, Literal(data["issued_date"], datatype=XSD_NS.date)))
    if data.get("modified_date"):
        g.add((dataset_uri, DCT.modified, Literal(data["modified_date"], datatype=XSD_NS.date)))

    # Temporal Coverage (PeriodOfTime)
    if "temporal_coverage" in data:
        tc = data["temporal_coverage"]
        temporal_bnode = BNode()
        g.add((dataset_uri, DCT.temporal, temporal_bnode))
        g.add((temporal_bnode, RDF.type, DCT.PeriodOfTime))
        if tc.get("start_date"):
            g.add((temporal_bnode, DCT.startDate, Literal(tc["start_date"], datatype=XSD_NS.date)))
        if tc.get("end_date"):
            g.add((temporal_bnode, DCT.endDate, Literal(tc["end_date"], datatype=XSD_NS.date)))

    # Spatial Coverage
    if data.get("spatial_coverage_uri"):
        g.add((dataset_uri, DCT.spatial, URIRef(data["spatial_coverage_uri"])))

    # Distribution
    if "distribution" in data:
        dist_data = data["distribution"]
        distribution_bnode = BNode()
        g.add((dataset_uri, DCAT.distribution, distribution_bnode))
        g.add((distribution_bnode, RDF.type, DCAT.Distribution))
        if dist_data.get("access_url"):
            g.add((distribution_bnode, DCAT.accessURL, URIRef(dist_data["access_url"])))
        if dist_data.get("media_type"):
            g.add((distribution_bnode, DCAT.mediaType, Literal(dist_data["media_type"])))
        if dist_data.get("format"):
            # Corrected line: Use DCT.format for file format
            g.add((distribution_bnode, DCAT.format, Literal(dist_data["format"])))

    # License
    if data.get("license_uri"):
        g.add((dataset_uri, DCT.license, URIRef(data["license_uri"])))

    # Keywords
    if "keywords" in data:
        lang_tag = data.get("language")
        for keyword in data["keywords"]:
            if lang_tag:
                g.add((dataset_uri, DCAT.keyword, Literal(keyword, lang=lang_tag)))
            else:
                g.add((dataset_uri, DCAT.keyword, Literal(keyword)))

    # Subject
    if data.get("subject"):
        subject_uri = URIRef(data["subject"]["uri"])
        g.add((dataset_uri, DCT.subject, subject_uri))
        g.add((subject_uri, RDF.type, SKOS.Concept))
        if data["id"] == "D6_Civil_Defense":
            g.add((subject_uri, SKOS.prefLabel, Literal(data["subject"]["label"], lang="pt")))
        else:
            g.add((subject_uri, SKOS.prefLabel, Literal(data["subject"]["label"], lang="en")))

# Define the output directory name
output_dir = "rdf_serialization"

# Create the directory
os.makedirs(output_dir, exist_ok=True)

# Define the full path for the output file
datasets_file = os.path.join(output_dir, "serialization_datasets.ttl")

# Write the serialized graph to the file
with open(datasets_file, "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

print(f"File saved as: {datasets_file}")