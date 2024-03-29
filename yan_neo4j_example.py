##########yan_neo4j_example.py##########
from yan_neo4j import start_neo4j
from yan_neo4j import create_neo4j_session
from yan_neo4j import ingest_knowledge_triplets_to_neo4j

start_neo4j(
	http_port = "5967", 
	bolt_port = "3577",
	neo4j_path = '/neo4j-community-3.5.12',
	)

neo4j_session = create_neo4j_session(
	bolt_port = "3577",
	)

t = [
	{
	'subject':"jingyan",
	'subject_type':"people",
	'subject_name':"jingyan",
	'object':"neo4j",
	'object_type':"software",
	'object_name':"neo4j",
	'relation':"proficient_in",
	},
	{
	'subject':"jingyan",
	'subject_type':"people",
	'subject_name':"jingyan",
	'object':"cypher",
	'object_type':"programming_langeuage",
	'object_name':"cypher",
	'relation':"proficient_in",
	},
	{
	'subject':"jingyan",
	'subject_type':"people",
	'subject_name':"jingyan",
	'object':"dr",
	'object_type':"title",
	'object_name':"dr.",
	'relation':"has_title",
	},
]
ingest_knowledge_triplets_to_neo4j(t, neo4j_session)

'''
neo4j: 

localhost:5967

bolt: bolt://0.0.0.0:3577

user name: neo4j

password: neo4j1
'''
##########yan_neo4j_example.py##########