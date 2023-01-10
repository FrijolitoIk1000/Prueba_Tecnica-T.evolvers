from redis_om import get_redis_connection
from redis.exceptions import ConnectionError
from os import getenv

#Conexion a BD Redis

try:
    redis_client = get_redis_connection( #Cambiar estos datos para la conexion
    host="localhost",
    port="6379",
    )
    print("REDIS CONNECTED")
except ConnectionError as e:
    print(e)

