# neo4j_docker


```bash
docker pull jingyanwang1/neo4j:1.0.1

docker run -it ^
-p 5967:5967 ^
-p 3577:3577 ^
jingyanwang1/neo4j:1.0.1 ^
bash

python3 yan_neo4j_example.py
```


neo4j: http://0.0.0.0:5967/

bolt: bolt://0.0.0.0:3577

user name: neo4j

password: neo4j1
