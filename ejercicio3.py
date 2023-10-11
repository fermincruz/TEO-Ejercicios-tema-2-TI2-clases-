from ejercicio1 import lee_variaciones_temperatura
from matplotlib import pyplot
from datetime import date


def muestra_variaciones_temperatura(ruta_csv, fecha_inicial, fecha_final):
    '''
    Suponemos que fecha_inicial y fecha_final son de tipo date
    '''
    datos = lee_variaciones_temperatura(ruta_csv)

    #Posible solución: buscar la fecha mínima de datos
    #if fecha_inicial == None:
    #    fecha_inicial = min(datos)[0]
    #
    # Pero mejor, cambiaremos la condición del filtrado

    # Esquema FILTRADO
    datos_filtrados = []
    for fecha, temp in datos:
        # Tratamos cada filtro por separado, y los unimos con and. 
        # En este caso,
        # hay dos filtros: un filtro por fecha inicial, y un
        # filtro por fecha final.
        # Para cada filtro, dado que si el parámetro es None
        # no hay que filtrar, usamos un or
        if  (fecha_inicial == None or fecha_inicial <= fecha)  and\
            (fecha_final == None or fecha <= fecha_final):
            tupla = (fecha, temp)
            datos_filtrados.append(tupla)

    # Esquema TRANSFORMACIÓN
    valores_x = []
    valores_y = []
    for fecha, temp in datos_filtrados:
        valores_x.append(fecha)
        valores_y.append(temp)

    pyplot.title("Variación de temperaturas medias del planeta")
    pyplot.plot(valores_x, valores_y)
    pyplot.show()


if __name__ == '__main__':
    muestra_variaciones_temperatura(
        "data/monthly_csv.csv", date(2001, 1, 1), date(2005, 1, 1))
    
    muestra_variaciones_temperatura(
        "data/monthly_csv.csv", None, date(1980, 1, 1))
    muestra_variaciones_temperatura(
        "data/monthly_csv.csv", date(1980, 1, 1), None)
    
    