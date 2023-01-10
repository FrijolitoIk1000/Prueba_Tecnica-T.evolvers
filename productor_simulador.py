from random import randint
from datetime import date
from schema.metric import Metric
from redis_client.conection import redis_client
import asyncio
from consumidor_csv import generar_csv

def main():
    limite = 0
    while limite < 10 or limite > 100:
        limite = int(input("Ingrese el rango del simulador de Fuerza(Newton) (10 - 100): "))
    asyncio.run(simulador(limite))

#Loop del simulador
async def simulador(limite: int):
    for i in range (limite):
        metrica = Metric (
            newton = randint(0,100),
            date = str(date.today())
        ) 

        generar_csv(metrica)#Llamado de microservicio para generar csv

        try:
           asyncio.create_task(envio_post(metrica))
           notif = asyncio.create_task(envio_notificacion(metrica))
           await notif
           await asyncio.sleep(3)
        except Exception as e:
            print(e) 
            

async def envio_notificacion(metrica: Metric):
    redis_client.xadd("metric_complete",metrica.dict(),'*') #Envio de evento consumidor_notification
async def envio_post(metrica: Metric):
    redis_client.xadd("metric_save",metrica.dict(),'*') #Envio de evento consumidor_post  


if __name__ == '__main__':
    main()