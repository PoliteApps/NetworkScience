# NetworkScience

This [Git repository](https://github.com/PoliteApps/NetworkScience) was created for the final project. 

Data can be consumed by this [Streamlit app](https://avalia-ai.streamlit.app/). Source code available at [Github](https://github.com/jvbm07/IRTify).

## Steps to analyze a network using Neo4j
1. Go to [Neo4j Labs](https://llm-graph-builder.neo4jlabs.com/)  
1. Drop file "Neo4j-a29b25df-Created-2024-11-15.txt" to use as credentials. This will connect to an AuraDB
1. Download previous tests at [Inep Website](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem/provas-e-gabaritos)
1. Drop it at Neo4j Labs on "Drag & Drop"
1. Click on "Graph Enhancement"
1. On Node Labels use: subjects, study topics, behaviours. Hint: type each one separatadely and then press "tab"
1. On Relationship Types use: related to, discussed about, talked about, includes, needs, contains. Use the same hint as previous point.
1. Select document and then click on "Generate Graph"
1. Select document again and click on "Explore graph" this will open Neo4j Bloom
1. Go to "Query" tab: if you click on any "Database information" item, this will create a Cypher query that will run in the right panel.
1. In the right panel there is an option called "Table" if you go there, there is a small "download" icon, that allows you to download the graph as a *.json file
1. Use the jupyter notebook to process this data

## Another data sources:
[Maritaca Enem](https://huggingface.co/datasets/maritaca-ai/enem)
[Enem Microdata](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

## To do:

1. tools/script.py generates questions_2022.csv and questions_2023.csv [Done]
1. tools/dif.py generates enem_dif_dataset.csv with student characteristics and enem_responses_dataset.csv [Rerun]
1. tools/samplig.py generates enem_random_sample.csv and we need to filter tests that matches with Maritaca dataset [Rerun]

## To do but in portuguese:

1. tirar uma sample do dataset de alunos que fizeram o caderno de provas que a gente precisa (coloquei no README) - foco 2022
1. ⁠Fazer um dataset com o gabarito + o que cada estudante marcou em cada questão
1. ⁠Fazer um dataset com os estudantes e as características dele (genero, tipo de escola, etc)
1. Utilizar outro repositório para gerar os grafos
1. Definir as perguntas e analisar