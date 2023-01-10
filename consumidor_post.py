from redis_client.conection import redis_client
import requests
import time
import json
import asyncio

key = "metric_save"
group = "metric-group-post"

url="http://127.0.0.1:8000/metric" #Conexion @app.post

headers = {
    'Content-Type': 'application/json'
}

async def post_fastapi(headers: dict):
    try:
        redis_client.xgroup_create(key,group) #Creacion del grupo en el stream
    except:
        print("Group already exists")

    while True:
        results = redis_client.xreadgroup(group,key, {key: '>'},None) #Obtencion de todos los eventos
        if results == []:
            print("Ningun POST")
            time.sleep(5)
        else:
            obj = results [0]
            obj_detail = obj [1][0][1]
            requests.request("POST",url,headers=headers,data=json.dumps(obj_detail))
            print("POST EXITOSO")

asyncio.run(post_fastapi(headers))