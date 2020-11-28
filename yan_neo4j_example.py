##########yan_neo4j_example.py##########
from yan_neo4j import * 

neo4j_session = initialize_neo4j_session(http_port = "6779", bolt_port = "7484")

t = [{
'subject':"a",
'subject_type':"b",
'subject_name':"c",
'object':"d",
'object_type':"e",
'object_name':"f",
'relation':"g",
}]
ingest_knowledge_triplets_to_neo4j(t, neo4j_session)


'''
# neo4j: http://0.0.0.0:6779/
'''
##########yan_neo4j_example.py##########
