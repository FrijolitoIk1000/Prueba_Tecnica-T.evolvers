from redis_om import HashModel
from redis_client.conection import redis_client

#Utilizamos el model de redis_om para un mejor trabajo de redis

class Metric(HashModel):
    #Damos por hecho que el id de este modelo es la pk
    newton: int
    date: str

    class Meta:
        database: redis_client
