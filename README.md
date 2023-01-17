# data-streaming-pipeline-docker-compose
Create a data-pipeline using python,kafka,logstash,elasticsearch & kibana.
First Created a Python producer which produced some random and send to a kafka-cluster topic then logstash use kafka topic as input data source
and processed those data then send to elasticseaerch.Kibana connect internally with elasticsearch and vistualize the data from elasticsearch index.  
![Screenshot from 2023-01-17 16-16-23](https://user-images.githubusercontent.com/99273251/212872474-7dca2d9f-8685-4c2a-94b0-84613257dba5.png)
