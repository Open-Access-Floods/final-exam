from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF, XSD, DCTERMS as DCT
import os

# Definir namespaces
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace("http://purl.org/dc/terms/")
FOAF_NS = Namespace("http://xmlns.com/foaf/0.1/")
XSD_NS = Namespace("http://www.w3.org/2001/XMLSchema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
FLOODS = Namespace("https://github.com/Open-Access-Floods/final-exam/tree/main/processed_RS")

# Data: List of dataset dictionaries (mas fácil para manipular)
datasets_list = [
    # D1 Disasters and Impact Data dataset
    {
        "id": "D1_Disasters_and_Impact_Data",
        "uri": "https://s2id.mi.gov.br/paginas/relatorios/",
        "title":  ["12300 - Alagamentos", "11321 - Deslizamentos", "12200 - Enxurradas", "12100 - Inundações", "13214 - Tempestade Local/Convectiva - Chuvas Intensas", "13213 - Tempestade Local/Convectiva - Granizo", "13212 - Tempestade Local/Convectiva - Tempestade de Raios", "13211 - Tempestade Local/Convectiva - Tornados", "13215 - Tempestade Local/Convectiva - Vendaval"],
        "description": "Os Relatórios apresentam diversos dados relacionados aos registros de danos e prejuízos, reconhecimento federal de situação de emergência, ações de resposta e obras de reconstrução realizadas pela SEDEC, de forma a apoiar o trabalho dos gestores públicos e informar a sociedade em geral.",
        "publisher_uri": "https://s2id.mi.gov.br/paginas/relatorios/",
        "publisher_name": "Relatório Gerencial: Danos informados. Sistema Integrado de Informações de Desastres (S2ID)",
        "creator_uri": "https://s2id.mi.gov.br/",
        "creator_name": "Relatório Gerencial: Danos informados. Sistema Integrado de Informações de Desastres (S2ID)",
        "language": "pt",
        "issued_date": "2014-01-31",
        "modified_date": "2025-05-27",
        "temporal_coverage": {
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "license_uri": "https://dados.gov.br/politica-de-dados-abertos-da-administracao-publica-federal",
        "keywords": ["Alagamentos", "Deslizamentos", "Enxurradas", "Inundações", "Tempestade" "Chuvas Intensas", "Granizo","Tempestade de Raios", "Tornados", "Vendaval"],
        "subject": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environment"
        }
    },
    # D2 Rainfall dataset
    {
        "id": "D2_Rainfall",
        "uri": "https://portal.inmet.gov.br/dadoshistoricos",
        "title": "Dados Historicos Anuais de Precipitação",
        "description": "Dados anuais de precipitação (mm) para estações meteorológicas do Brasil, abrangendo o período de 2002 a 2023.",
        "publisher_uri": "https://bdmep.inmet.gov.br/",
        "publisher_name": "Instituto Nacional de Meteorologia (INMET)",
        "creator_uri": "https://portal.inmet.gov.br/",
        "creator_name": "Intituto Nacional de Meteorologia (INMET)",
        "language": "pt",
        "issued_date": "2002-12-31",
        "modified_date": "2025-01-21",
        "temporal_coverage": {
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "license_uri": "https://dados.gov.br/politica-de-dados-abertos-da-administracao-publica-federal",
        "keywords": ["Alagamentos", "Deslizamentos", "Enxurradas", "Inundações", "Tempestade" "Chuvas Intensas", "Granizo","Tempestade de Raios", "Tornados", "Vendaval", "Bazilian Municipalities", "Rainfall", "Precipitation"],
        "subject": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environment"
        }
    },
    # D3_Population Data dataset (Portuguese content, mapped to pt language)
    {
        "id": "D3_Population_Risk",
        "uri": "https://www.ibge.gov.br/geociencias/organizacao-do-territorio/tipologias-do-territorio/21538-populacao-em-areas-de-risco-no-brasil.html?edicao=21537&t=sobre",
        "title": "População em áreas de risco no Brasil",
        "description": "Os dados divulgados na publicação são do ano de 2010, data do último Censo Demográfico realizado pelo IBGE, mas a metodologia foi desenvolvida para ser replicada a partir dos dados do Censo Demográfico de 2020, garantindo o baixo custo de execução e otimização de recursos públicos. Além disso, será possível acompanhar a evolução temporal das características da população exposta ao risco de desastres. Base Territorial Estatística de Áreas de Risco - BATER",
        "publisher_uri": "https://www.ibge.gov.br/geociencias/organizacao-do-territorio/tipologias-do-territorio/21538-populacao-em-areas-de-risco-no-brasil.html?edicao=21537&t=sobre",
        "publisher_name": "Instituto Brasileiro de Geografia e Estatística (IBGE) - Coordenação de Geografia",
        "creator_uri": "https://www.gov.br/cemaden/pt-br",
        "creator_name": "Centro Nacional de Monitoramento e Alertas de Desastres Naturais (CEMADEN)",
        "language": "pt",
        "issued_date": "2010-12-31",
        "modified_date": "2018-01-21",
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "license_uri": "https://dados.gov.br/politica-de-dados-abertos-da-administracao-publica-federal",
        "keywords": ["Censo Demográfico", "População", "Áreas de Risco", "Desastres Naturais", "Brasil" ],
        "subject": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/SOCI",
            "label": "Population and Society"
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
            "uri": "http://publications.europa.eu/resource/authority/data-theme/SOCI",
            "label": "Population and Society"
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
            "label": "Environment"
        }
    },
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
            "uri": "http://publications.europa.eu/resource/authority/subject-matter/PCIV",
            "label": "Civil Protection"
        }
    },
    # MASHUPS DATASETS
    { # MD1 
        "id": "MD1_Affected_Population",
        "distribution": "CSV",
        "title": "Affected Population by Disaster Type in Brazil",
        "description": "This dataset provides information on the number of people affected by various types of disasters in Brazil, including floods, landslides, and storms. The data is aggregated by disaster type and year. (EXAMPLE)",
        "theme": "http://publications.europa.eu/resource/authority/data-theme/SOCI",
        "first_production_year": "2025",
        "keywords": [
            "Affected population", "Disaster type", "Brazil", "Floods", "Landslides", "Storms"
        ],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "publisher_uri": ["https://github.com/rufferbaraldi", "https://github.com/CarlaMenegat", "https://github.com/csalguero10"],
        "publisher_name": ["Carla Menegart", "Rubens Baraldi", "Catalina Salguero"]
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