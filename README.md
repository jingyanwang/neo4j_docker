# neo4j_docker

## pull the docker image

```bash
docker pull jingyanwang1/neo4j:1.0.3
```

## start the docker

```bash
docker run -it ^
-p 5967:5967 ^
-p 3577:3577 ^
jingyanwang1/neo4j:1.0.3 ^
bash
```

# run the example 

```bash
python3 yan_neo4j_example.py
```

## see the result at 

neo4j: http://localhost:5967/browser/

<img src="WeChat%20Screenshot_20220320193129.png" width="500">

## the username and pasword (if needed)

bolt: http://localhost:3577

user name: neo4j

password: neo4j1
