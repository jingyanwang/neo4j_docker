# yan_neo4j_docker


```bash
docker build -t gaoyuanliang/yan_neo4j:1.0.1 .

docker run -it \
-m 10g \
-v /Users/Jim/Downloads/:/Users/Jim/Downloads/ \
-p 6779:6779 \
-p 7484:7484 \
gaoyuanliang/yan_neo4j:1.0.1 \
bash
```


```bash
neo4j: http://0.0.0.0:6779/
```
