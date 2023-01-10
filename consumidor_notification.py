from redis_client.conection import redis_client
import time
import asyncio

key = 'metric_complete'
group= "metric-group-gt50"

try:
    redis_client.xgroup_create(key,group) #Creacion del grupo en el stream
except:
    print("Group already exists")

async def notificacion():
    while True:
        results = redis_client.xreadgroup(group,key, {key: '>'},None) #Obtencion de todos los eventos
        if results == []:
            print("Ninguna notificacion")
            time.sleep(5)
        else:

            obj = results [0]
            obj_detail = obj [1][0][1]
            r = int(obj_detail["newton"]) #Obtenemos un str y lo convertimos a int para comparar 
            if r > 50:
                print("Metrica mayor a 50 newtons")
           
asyncio.run(notificacion())           