from ejercicio1 import lee_variaciones_temperatura
from matplotlib import pyplot


def muestra_variaciones_temperatura(ruta_csv):
    datos = lee_variaciones_temperatura(ruta_csv)
    # Esquema TRANSFORMACIÓN
    valores_x = []
    valores_y = []
    for fecha, temp in datos:
        valores_x.append(fecha)
        valores_y.append(temp)

    pyplot.title("Variación de temperaturas medias del planeta")
    pyplot.plot(valores_x, valores_y)
    pyplot.show()


if __name__ == '__main__':
    muestra_variaciones_temperatura("data/monthly_csv.csv")
