import csv
from datetime import datetime


def lee_variaciones_temperatura(ruta_csv):
    '''
     Recibe la ruta de un archivo de datos en formato CSV
    y devuelva una lista de tuplas con los datos leídos. 
    El archivo CSV constará de dos columnas, la primera de 
    las cuáles indica una fecha y la segunda la variación 
    de temperaturas con respecto a la temperatura media 
    del periodo completo.
    '''
    with open(ruta_csv, encoding='utf-8') as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for fecha, temp in lector:
            if "/" in fecha:
                fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            else:
                fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
            temp = float(temp)
            tupla = (fecha, temp)
            res.append(tupla)
        return res


if __name__ == '__main__':
    datos = lee_variaciones_temperatura("data/monthly_csv.csv")
    for d in datos[:3]:
        print(d)
