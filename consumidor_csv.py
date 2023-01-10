import csv
from schema.metric import Metric

def generar_csv(metric:Metric):
    f = open('archivo.csv', 'a', newline='') 
    fila = (metric)
    writer = csv.writer(f,delimiter=',')
    writer.writerow(fila)
    f.close()