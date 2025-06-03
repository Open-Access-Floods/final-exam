from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF, DCTERMS as DCT
import os

# Definir namespaces
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace("http://purl.org/dc/terms/")
FOAF_NS = Namespace("http://xmlns.com/foaf/0.1/")
XSD_NS = Namespace("http://www.w3.org/2001/XMLSchema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
BRASIL = Namespace("https://github.com/Open-Access-Floods/final-exam/")

# Data: List of dataset dictionaries (mas fácil para manipular)
datasets_list = [
    # D1 Disasters and Impact Data dataset
    {
        "id": "D1_Disasters_and_Impact_Data",
        "uri": "https://s2id.mi.gov.br/paginas/relatorios/D1_Disasters_and_Impact_Data", # Specific URI for this dataset
        "title":  ["12300 - Alagamentos", "11321 - Deslizamentos", "12200 - Enxurradas", "12100 - Inundações", "13214 - Tempestade Local/Convectiva - Chuvas Intensas", "13213 - Tempestade Local/Convectiva - Granizo", "13212 - Tempestade Local/Convectiva - Tempestade de Raios", "13211 - Tempestade Local/Convectiva - Tornados", "13215 - Tempestade Local/Convectiva - Vendaval"],
        "description": "Os Relatórios apresentam diversos dados relacionados aos registros de danos e prejuízos, reconhecimento federal de situação de emergência, ações de resposta e obras de reconstrução realizadas pela SEDEC, de forma a apoiar o trabalho dos gestores públicos e informar a sociedade em geral.",
        "publisher_uri": "https://s2id.mi.gov.br/", # Changed to the base URL for the publisher
        "publisher_name": "Sistema Integrado de Informações de Desastres (S2ID)", # Simplified publisher name
        "creator_uri": "https://s2id.mi.gov.br/", # Changed to the base URL for the creator
        "creator_name": "Sistema Integrado de Informações de Desastres (S2ID)", # Simplified creator name
        "language": "pt",
        "issued_date": "2014-01-31",
        "modified_date": "2025-05-27",
        "temporal_coverage": {
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "distribution": { # Added distribution details
            "access_url": "https://s2id.mi.gov.br/paginas/relatorios/D1_Disasters_and_Impact_Data.html", # Example access URL
            "media_type": "text/html",
            "format": "HTML",
            "byte_size": 15000, # Example byte size
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC" # Example access right
        },
        "license_uri": "https://dados.gov.br/politica-de-dados-abertos-da-administracao-publica-federal",
        "keywords": ["Alagamentos", "Deslizamentos", "Enxurradas", "Inundações", "Tempestade", "Chuvas Intensas", "Granizo","Tempestade de Raios", "Tornados", "Vendaval"],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environment"
        }
    },
    # D2 Rainfall dataset
    {
        "id": "D2_Rainfall",
        "uri": "https://portal.inmet.gov.br/dadoshistoricos/D2_Rainfall", # Specific URI for this dataset
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
        "distribution": { # Added distribution details
            "access_url": "https://portal.inmet.gov.br/dadoshistoricos/D2_Rainfall.csv", # Example access URL
            "media_type": "text/csv",
            "format": "CSV",
            "byte_size": 250000, # Example byte size
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://dados.gov.br/politica-de-dados-abertos-da-administracao-publica-federal",
        "keywords": ["Alagamentos", "Deslizamentos", "Enxurradas", "Inundações", "Tempestade", "Chuvas Intensas", "Granizo","Tempestade de Raios", "Tornados", "Vendaval", "Brazilian Municipalities", "Rainfall", "Precipitation"],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environment"
        }
    },
    # D3_Population Data dataset
    {
        "id": "D3_Population_Risk",
        "uri": "https://www.ibge.gov.br/geociencias/organizacao-do-territorio/tipologias-do-territorio/21538-populacao-em-areas-de-risco-no-brasil.html#D3_Population_Risk", # Specific URI
        "title": "População em áreas de risco no Brasil",
        "description": "Os dados divulgados na publicação são do ano de 2010, data do último Censo Demográfico realizado pelo IBGE, mas a metodologia foi desenvolvida para ser replicada a partir dos dados do Censo Demográfico de 2020, garantindo o baixo custo de execução e otimização de recursos públicos. Além disso, será possível acompanhar a evolução temporal das características da população exposta ao risco de desastres. Base Territorial Estatística de Áreas de Risco - BATER",
        "publisher_uri": "https://www.ibge.gov.br/", # Simplified publisher URI
        "publisher_name": "Instituto Brasileiro de Geografia e Estatística (IBGE)", # Simplified publisher name
        "creator_uri": "https://www.gov.br/cemaden/pt-br",
        "creator_name": "Centro Nacional de Monitoramento e Alertas de Desastres Naturais (CEMADEN)",
        "language": "pt",
        "issued_date": "2010-12-31",
        "modified_date": "2018-01-21",
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "distribution": { # Added distribution details
            "access_url": "https://www.ibge.gov.br/geociencias/organizacao-do-territorio/tipologias-do-territorio/21538-populacao-em-areas-de-risco-no-brasil.html",
            "media_type": "text/html",
            "format": "HTML",
            "byte_size": 30000,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://dados.gov.br/politica-de-dados-abertos-da-administracao-publica-federal",
        "keywords": ["Censo Demográfico", "População", "Áreas de Risco", "Desastres Naturais", "Brasil" ],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/SOCI",
            "label": "Population and Society"
        }
    },
    # D4_Urban_Expansion dataset
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
        "distribution": { # Added distribution details
            "access_url": "https://doi.org/10.58053/MapBiomas/2W2Z5M",
            "media_type": "text/html",
            "format": "HTML",
            "byte_size": 50000,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": ["Land Cover", "Transitions", "Statistics", "Brazilian states", "Brazilian municipalities"],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/SOCI",
            "label": "Population and Society"
        }
    },
    # D5_Deforestation dataset
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
        "distribution": { # Added distribution details
            "access_url": "https://doi.org/10.58053/MapBiomas/7STHCP",
            "media_type": "text/html",
            "format": "HTML",
            "byte_size": 70000,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": ["Deforestation", "Secondary Vegetation", "Statistics", "Brazilian states", "Brazilian municipalities"],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environment"
        }
    },
    {  # D6_Civil_Defense dataset
        "id": "D6_Civil_Defense",
        "uri": "https://portaldatransparencia.gov.br/graficos/incorporar/acao-especifica/evolucao-historica/linhas?codigoAcao=22BO#D6_Civil_Defense", # Specific URI
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
        "distribution": { # Added distribution details
            "access_url": "https://portaldatransparencia.gov.br/graficos/incorporar/acao-especifica/evolucao-historica/linhas?codigoAcao=22BO",
            "media_type": "text/html",
            "format": "HTML",
            "byte_size": 40000,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://dados.gov.br/politica-de-dados-abertos-da-administracao-publica-federal",
        "keywords": [
            "gastos públicos", "orçamento", "defesa civil",
            "ações emergenciais", "desastres naturais", "transparência pública"
        ],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/subject-matter/PCIV",
            "label": "Civil Protection"
        }
    },
    # MASHUPS DATASETS - Assuming these are also "datasets" within your catalog context
    { # MD1_Affected_Population dataset
        "id": "MD1_Affected_Population",
        "uri": BRASIL["MD1_Affected_Population"], # Construct URI using BRASIL namespace
        "title": "Affected Population by Disaster Type in Brazil",
        "description": "This dataset provides information on the number of people affected by various types of disasters in Brazil, including floods, landslides, and storms. The data is aggregated by disaster type and year. (EXAMPLE)",
        "language": "en", # Assuming English for this Mashup
        "issued_date": "2025-05-27", # Today's date
        "modified_date": "2025-05-27",
        "temporal_coverage": {
            "start_date": "2000-01-01", # Example coverage
            "end_date": "2024-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "distribution": {
            "access_url": "https://github.com/Open-Access-Floods/final-exam/blob/main/processed_RS/MD1_Affected_Population.csv", # Example access URL
            "media_type": "text/csv",
            "format": "CSV",
            "byte_size": 8000,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": [
            "Affected population", "Disaster type", "Brazil", "Floods", "Landslides", "Storms"
        ],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/SOCI", # Changed to SOCIETY theme
            "label": "Population and Society"
        },
        # For mashups, publisher/creator could be the project members
        "publisher_uri": "https://github.com/Open-Access-Floods/", # Example URI for the project team
        "publisher_name": "Open Access Floods Project Team",
    },
    { # MD1_Municipality_Rainfall
        "id": "MD2_Municipality_Rainfall",
        "uri": BRASIL["MD2_Municipality_Rainfall"], # Construct URI using BRASIL namespace
        "title": "Monthly Rainfall Aggregated by Municipality – Brazil (2024)",
        "description": "This dataset aggregates monthly precipitation totals for Brazilian municipalities in 2024, based on INMET weather station data geolocated to administrative boundaries. It supports hydrological risk and disaster analysis.",
        "language": "en", # Assuming English for this Mashup
        "issued_date": "2025-05-28", # Today's date
        "modified_date": "2025-05-28",
        "temporal_coverage": {
            "start_date": "2000-01-01", # Example coverage
            "end_date": "2024-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "distribution": {
            "access_url": "https://github.com/Open-Access-Floods/final-exam/blob/main/processed_RS/MD2_Municipality_Rainfall.csv", # Example access URL
            "media_type": "text/csv",
            "format": "CSV",
            "byte_size": 10000,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": [
            "Precipitation", "Rainfall", "Climate data", "Brazil", "Municipal level", "Hydrological risk", "Disaster analysis"
        ],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environment"
        },
        # For mashups, publisher/creator could be the project members
        "publisher_uri": "https://github.com/Open-Access-Floods/", # Example URI for the project team
        "publisher_name": "Open Access Floods Project Team",
    },
    { # MD3_Deforestation_RS
        "id": "MD3_Deforestation_RS",
        "uri": BRASIL["MD3_Deforestation_RS"], # Construct URI using BRASIL namespace
        "title": "Deforestation in Rio Grande do Sul – MapBiomas (2000–2022)",
        "description": "This dataset presents annual deforestation figures for municipalities in the state of Rio Grande do Sul, derived from MapBiomas land cover classifications. It enables the assessment of forest loss trends over two decades.",
        "language": "en", # Assuming English for this Mashup
        "issued_date": "2025-05-27", # Today's date
        "modified_date": "2025-05-27",
        "temporal_coverage": {
            "start_date": "2000-01-01", # Example coverage
            "end_date": "2022-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "distribution": {
            "access_url": "https://github.com/Open-Access-Floods/final-exam/blob/main/processed_RS/MD3_Deforestation_RS.csv", # Example access URL
            "media_type": "text/csv",
            "format": "CSV",
            "byte_size": 9000,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": [
            "Brazil", "Floods", "Landslides", "Deforestation", "Forest loss", "Land cover", "MapBiomas", "Rio Grande do Sul"
        ],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environment"
        },
        # For mashups, publisher/creator could be the project members
        "publisher_uri": "https://github.com/Open-Access-Floods/", # Example URI for the project team
        "publisher_name": "Open Access Floods Project Team",
    },
    { # MD4_Rain_Precipitation_States dataset
        "id": "MD4_Rain_Precipitation_States",
        "uri": BRASIL["MD4_Rain_Precipitation_States"], # Construct URI using BRASIL namespace
        "title": "Rainfall Volume by Brazilian State – INMET (2024)",
        "description": "This dataset provides aggregated rainfall data for each Brazilian state for the year 2024, based on meteorological station records from INMET. It supports regional analysis of extreme precipitation events.",
        "language": "en", # Assuming English for this Mashup
        "issued_date": "2025-05-27", # Today's date
        "modified_date": "2025-05-27",
        "temporal_coverage": {
            "start_date": "2024-01-01", # Example coverage
            "end_date": "2024-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "distribution": {
            "access_url": "https://github.com/Open-Access-Floods/final-exam/blob/main/processed_RS/MD4_Rain_Precipitation_States.csv", # Example access URL
            "media_type": "text/csv",
            "format": "CSV",
            "byte_size": 7000,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": [
            "Climate", "Precipitation", "Brazil", "INMET", "Rainfall", "Meteorological data", "Extreme weather", "Hydrological risk"
        ],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/REGI", # Changed to SOCIETY theme
            "label": "Regions and Cities"
        },
        # For mashups, publisher/creator could be the project members
        "publisher_uri": "https://github.com/Open-Access-Floods/", # Example URI for the project team
        "publisher_name": "Open Access Floods Project Team",
    },
    { # MD5_Monthly_Rainfall_Stations_RS
        "id": "MD5_Monthly_Rainfall_Stations_RS",
        "uri": BRASIL["MD5_Monthly_Rainfall_Stations_RS"], # Construct URI using BRASIL namespace
        "title": "Monthly Rainfall by Weather Station – Rio Grande do Sul (2024)",
        "description": "This dataset presents monthly rainfall measurements from INMET meteorological stations located in the state of Rio Grande do Sul, Brazil, for the year 2024. It enables fine-grained temporal and spatial analysis of precipitation patterns during extreme weather events.",
        "language": "en", # Assuming English for this Mashup
        "issued_date": "2025-05-27", # Today's date
        "modified_date": "2025-05-27",
        "temporal_coverage": {
            "start_date": "2024-01-01", # Example coverage
            "end_date": "2024-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "distribution": {
            "access_url": "https://github.com/Open-Access-Floods/final-exam/blob/main/processed_RS/MD5_Monthly_Rainfall_Stations_RS.csv", # Example access URL
            "media_type": "text/csv",
            "format": "CSV",
            "byte_size": 8500,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": [
            "Affected population", "Disaster type", "Brazil", "Rainfall", "Meteorological stations", "Rio Grande do Sul", "Monthly data", "INMET"],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI", # Changed to SOCIETY theme
            "label": "Environment"
        },
        # For mashups, publisher/creator could be the project members
        "publisher_uri": "https://github.com/Open-Access-Floods/", # Example URI for the project team
        "publisher_name": "Open Access Floods Project Team",
    },
    { # MD6_Urbanization_Growth_RS
        "id": "MD6_Urbanization_Growth_RS",
        "uri": BRASIL["MD7_Urbanization_Growth_RS"], # Construct URI using BRASIL namespace
        "title": "Urbanization Growth by Municipality – Rio Grande do Sul (2013–2023)",
        "description": "This dataset presents the percentage growth in urbanized land area for each municipality in Rio Grande do Sul, Brazil, between 2013 and 2023. The data is derived from MapBiomas and supports analysis of land use changes related to climate vulnerability and disaster risk.",
        "language": "en", 
        "issued_date": "2025-05-27", 
        "modified_date": "2025-05-28",
        "temporal_coverage": {
            "start_date": "2013-01-01", 
            "end_date": "2023-12-31"
        },
        "spatial_coverage_uri": "http://publications.europa.eu/resource/authority/country/BRA",
        "distribution": {
            "access_url": "https://github.com/Open-Access-Floods/final-exam/blob/main/processed_RS/MMD7_Urbanization_Growth_RS.csv", # Example access URL
            "media_type": "text/csv",
            "format": "CSV",
            "byte_size": 4800,
            "access_rights_uri": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
        },
        "license_uri": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": [
            "Urbanization", "Land use change", "Rio Grande do Sul", "MapBiomas","Urban growth"],
        "theme": {
            "uri": "http://publications.europa.eu/resource/authority/data-theme/ENVI",
            "label": "Environment"
        },
        # For mashups, publisher/creator could be the project members
        "publisher_uri": "https://github.com/Open-Access-Floods/", 
        "publisher_name": "Open Access Floods Project Team",
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
g.bind("brasil", BRASIL)  # Custom namespace for the project

for data in datasets_list:
    # Use BRASIL namespace with the 'id' to create a clear, consistent URI for each dataset.
    # This also handles the 'id' requirement.
    dataset_uri = BRASIL[data["id"]]

    # Add this dataset to the catalog. Assuming a single catalog URI like BRASIL["catalog"]
    # This links the dataset to the catalog.
    catalog_uri = BRASIL["catalog"] # Define the main catalog URI if not already defined
    g.add((catalog_uri, DCAT.dataset, dataset_uri))

    # Add triples for the Dataset
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
    publisher_uris = data.get("publisher_uri")
    publisher_names = data.get("publisher_name")

    if publisher_uris:
        if not isinstance(publisher_uris, list):
            publisher_uris = [publisher_uris]  # Asegura que sea lista

        for i, uri in enumerate(publisher_uris):
            publisher_uri = URIRef(uri)
            g.add((dataset_uri, DCT.publisher, publisher_uri))
            g.add((publisher_uri, RDF.type, FOAF_NS.Agent))

            # Si publisher_name también es una lista, emparejamos por índice
            if publisher_names:
                if isinstance(publisher_names, list):
                    if i < len(publisher_names):
                        g.add((publisher_uri, FOAF_NS.name, Literal(publisher_names[i])))
                else:
                    g.add((publisher_uri, FOAF_NS.name, Literal(publisher_names)))

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
        distribution_bnode = BNode() # Use a BNode for the specific distribution instance
        g.add((dataset_uri, DCAT.distribution, distribution_bnode))
        g.add((distribution_bnode, RDF.type, DCAT.Distribution))

        if dist_data.get("access_url"):
            g.add((distribution_bnode, DCAT.accessURL, URIRef(dist_data["access_url"])))
        if dist_data.get("media_type"):
            g.add((distribution_bnode, DCAT.mediaType, Literal(dist_data["media_type"])))
        if dist_data.get("format"):
            # Use DCT.format for file format description
            g.add((distribution_bnode, DCT["format"], Literal(dist_data["format"])))
        if dist_data.get("byte_size"):
            # Use DCAT.byteSize for the size of the distribution in bytes
            g.add((distribution_bnode, DCAT.byteSize, Literal(dist_data["byte_size"], datatype=XSD_NS.integer)))
        if dist_data.get("access_rights_uri"):
            # Use DCT.accessRights for the access rights of the distribution
            g.add((distribution_bnode, DCT.accessRights, URIRef(dist_data["access_rights_uri"])))

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
    if data.get("theme"):
        subject_uri = URIRef(data["theme"]["uri"])
        g.add((dataset_uri, DCT.theme, subject_uri))
        g.add((subject_uri, RDF.type, SKOS.Concept))
        if data["id"] == "D6_Civil_Defense":
            g.add((subject_uri, SKOS.prefLabel, Literal(data["theme"]["label"], lang="pt")))
        else:
            g.add((subject_uri, SKOS.prefLabel, Literal(data["theme"]["label"], lang="en")))

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