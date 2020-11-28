############Dockerfile###########
FROM openjdk:8

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN apt-get install -y tar

RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip

####neo4j
RUN pip3 install neo4j==4.1.1
RUN wget http://neo4j.com/artifact.php?name=neo4j-community-3.5.12-unix.tar.gz
RUN tar -xf 'artifact.php?name=neo4j-community-3.5.12-unix.tar.gz'
WORKDIR /

###download the codes
RUN echo "gsdgssdretb"
WORKDIR /

RUN git clone https://github.com/yanliang12/yan_neo4j_docker.git
RUN mv /yan_neo4j_docker/* ./
RUN rm -r yan_neo4j_docker

RUN rm Dockerfile*
############Dockerfile###########
