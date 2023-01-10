# Prueba_Tecnica-T.evolvers
Santiago Olmedo Echeverri\
santiago08olmedoecheverri@gmail.com
### Introducción
En este repositiorio se encuentra el proyecto para la prueba tecnica de T.evolvers, esta consta de una simulacion de un generador de fuerza
medidos en Newtons.

### Reto abordado

**PRUEBA TÉCNICA DESARROLLADOR PYTHON**

**Objetivo:**

Validar los conocimientos técnicos requeridos para el buen desempeño en el stack requerido para el mismo.

- Conocimientos a evaluar:
- Python
- FastApi
- Redis
- Redis streams
- Diseño de arquitectura backend.

La prueba se dividirá en 2 partes:

1. Simulador y comunicación entre microservicios.
1. Simular un dispositivo eléctrico que reporte medidas de manera aleatoria en un rango determinado. Ejemplo: (10 - 100), datos a reportar:
- ID Dispositivo
- Métrica 1 medida (kwh, temp, etc), Ejemplo: 55 kwh
- Timestamp

Criterios punto a:

- El simulador deberá estar desarrollado en python
- Utilizar loop de asyncio para que el simulador siempre este reportando métricas.
- Utilizar redis streams para producir un evento cada vez que llegue una métrica

Nota: Este servicio tendrá rol de Producer.

2. Crear un microservicio en fastapi o django que contenga un CRUD el cual permita administrar los datos enviados por el medidor.
2. Crear un microservicio con python que escuche los eventos reportados por el simulador y llame al microservicio de fastapi o django para almacenar las métricas.

Nota: Este servicio tendrá rol de Consumer, tener en cuenta que cada evento consumido se deberá quitar de la lista del consumidor.

4. Crear un microservicio conectado al mismo stream de eventos pero que reaccione de una forma diferente, en este caso se deberá simular un alerta o notificación en caso tal de que la medida reportada supere un umbral de 50.
2. Análisis
1. Recolección de datos de la tabla que almacena los eventos guardados por el microservicio y generar un CSV
1. Analizar los datos del CSV y mostrar en una gráfica el número que más veces se repite del rango reportado y cuantos datos se han reportado en 1 minutos. (Se pueden agregar más comparaciones para hacer el ejercicio más completo).

Resultado esperado:

- Un productor de eventos (Métricas de dispositivo).
- Dos grupos de consumidores (1 para consumir servicio de fastapi y otro para generar alertas).
- Un microservicio en fastapi con el CRUD de métricas.
- Diagrama de diseño de arquitectura y comunicación entre microservicios.

NOTA:  Cada  microservicio  deberá  correr  de  forma  independiente  como  un contenedor de Docker

### Diagrama de Diseño de arquitectura

![Diseño](https://i.ibb.co/Xj657Sw/Diagrama-en-blanco.png[/img][/url)

### Guia

#### Primero:
Tener un endpoint de redis `en mi caso lo hice localmente`  y configurarlo en el archivo `Prueba_Tecnica-T.evolvers/redis_client/conection.py  ` 
#### Segundo:
Ejecutar el archivo `Prueba_Tecnica-T.evolvers/productor_simulador.py`, y abrir en paralelo 2 consolas con el entorno virtual del proyecto para poder ejecutar los microservicios consumidores

Microservicio de notificación `Prueba_Tecnica-T.evolvers/consumidor_notification.py  `

Microservicio de POST con FastApi `Prueba_Tecnica-T.evolvers/consumidor_post.py `
#### Tercero:
Al ingresar los datos se genera un evento mediante Redis Stream donde se notificara si la metrica supero un umbral mayor a 50N de su medida.\
Se generará tambien con Redis Stream un peticion de POST mediante FastApi.
#### Cuarto:
Todo lo generado por sesión de ejecución de `Prueba_Tecnica-T.evolvers/productor_simulador.py`, se guardará en un CSV, para su análisis.
#### Quinto:
Ejecutar el archivo `Prueba_Tecnica-T.evolvers/consumidor_CRUD.py` para el manejo del CRUD mediante FastApi


Referencias:
https://fastapi.tiangolo.com/ \
https://redis.io/topics/streams-intro \
https://aioredis.readthedocs.io/en/latest/ \
https://docs.docker.com/
