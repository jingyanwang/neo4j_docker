# yan_neo4j_docker


```bash
docker build -t gaoyuanliang/yan_neo4j:1.0.1 .

docker run -it \
-m 10g \
-v /Users/Jim/Downloads/:/Users/Jim/Downloads/ \
-p 5967:5967 \
-p 3577:3577 \
gaoyuanliang/yan_neo4j:1.0.1 \
bash

python3 yan_neo4j_example.py
```


neo4j: http://0.0.0.0:5967/

bolt: bolt://0.0.0.0:3577

user name: neo4j

password: neo4j1
