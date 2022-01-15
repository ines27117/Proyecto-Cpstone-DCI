# Programa de calibración del sensor PH-4502C
# La ecuación de la recta tiene la forma:
# y = mx + b
# esta ecuación se utiliza para obtener los valores de PH dependiendo del voltaje de entrada, por lo que
# con el uso de un archivo se guardaran los valores de la pendiente m, y la ordenada al origen b.
# este archivo tendrá el siguiente formato:
# m,b
# si lo desea, también puede añadir su propio archivo txt con estos valores.
# Programa elaborado por Mejia Bazan Cesar Arturo
# Basado en el repositorio: https://github.com/agrabbs/automatedhorticulture

import sys
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# Método para obtener el voltaje actual de la entrada analógica del canal seleccionado
def obtener_voltaje(channel):
    print("Obteniendo el voltaje...")
    voltaje = 0.0
    # Se hace lectura de 5 voltajes
    for x in range(5):
        time.sleep(0.1)
        voltaje = voltaje + channel.voltage

    # Se obtiene el promedio
    voltaje = voltaje / 5
    # Se redondea el voltaje a 2 cifras significativas
    voltaje = round(voltaje, 2)
    # Se regresa el voltaje
    return voltaje


# Método para calibrar, este método recibe el canal seleccionado, y los valores de PH conocidos
def calibrar(channel, y_1: float, y_2: float):
    # Se crea el archivo de escritura recta.txt
    file = open("recta.txt", "w")

    # Se obtiene la cadena que representa a los valores de PH conocidos,
    # el formato es solo con una cifra después del punto
    str_y1 = "{:.1f}".format(y_1)
    str_y2 = "{:.1f}".format(y_2)

    print("Vamos a comenzar a calibrar, primero coloca el electrodo en la solución de PH:", str_y1)
    input("Presiona ENTER cuando el electrodo este en la solución")

    # Se obtiene el voltaje de la solución con PH y_1
    x_1 = obtener_voltaje(channel)
    print("y_1:", str_y1, "x_1:", x_1)
    print("Ahora coloca el electrodo en la solución de PH:", str_y2)
    input("Presiona ENTER cuando el electrodo este en la solución")

    # Se obtiene el voltaje de la solución con PH y_2
    x_2 = obtener_voltaje(channel)
    print("y_2:", str_y2, "x_2:", x_2)

    # Se obtiene la pendiente, recordar que la pendiente se obtiene con la siguiente ecuación:
    # m = (y_2 - y_1 ) / (x_2 - x_1)
    # en este caso redondeamos a 4 cifras significativas
    m = round((y_2 - y_1) / (x_2 - x_1), 4)

    # Se obtiene la ordenada al origen, tomando cualquier punto de nuestra ecuación, en este caso con y_1
    # recordar que la ecuación de la recta es:
    # y = m*x + b
    # entonces despejando b obtenemos
    # b = -m*x + y
    # redondeamos esto a 4 cifras significativas
    b = round((-m * x_1 + y_1), 4)

    # escribimos los valores obtenidos en el archivo
    file.write(m + "," + b + "\n")
    # cerramos el archivo
    file.close()

    # Fin del programa
    input("Archivo recta.txt creado con exito, presiona ENTER para terminar")


# Método para elegir que soluciones predefinidas se utilizaran
def calibrarPH(channel):
    print(
        "\n\nPrepara dos soluciones con PH conocido, \nla recomendación es trabajar con soluciones de PH de 7 y 4 para"
        "calibrar, ¿Qué opción quieres tomar?")
    opcion = -1
    while opcion not in [1, 2]:
        try:
            opcion = int(input("1.-Calibrar con soluciones PH 7 y 4"
                               "\n2.-Calibrar con soluciones de PH conocido diferentes"))
        except:
            print("Se ingreso una opción no valida")

    if opcion == 1:
        # Se comienza a calibrar con las soluciones de PH estándar
        calibrar(channel, 4.0, 7.0)
    elif opcion == 2:
        while True:
            try:
                sol_1 = float(input("Dame el PH de la primera solución"))
                sol_2 = float(input("Dame el PH de la segunda solución"))
                break
            except:
                print("Los datos que ingresaste son incorrectos")
        # Se comienza a calibar con las soluciones de PH personalizadas
        calibrar(channel, sol_1, sol_2)
    else:
        sys.exit("Error inesperado seleccionado una opción")


# Método principal
def main():
    # Se inicializa la interfaz I2C para el ADS1115
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    print("\nPrograma de calibración del sensor de PH-4502C\n")
    channel = -1
    # Se pregunta en cual canal se encuentra conectado el PH-4502C
    while channel not in [0, 1, 2, 3]:
        try:
            channel = int(input("¿En qué canal se encuentra conectado el sensor de PH al ADS1115? 0-3:"))
        except:
            print("Se ingreso una opción no valida")

    # Se lee la entrada analógica del canal seleccionado
    if channel == 0:
        channel = AnalogIn(ads, ADS.P0)
    elif channel == 1:
        channel = AnalogIn(ads, ADS.P1)
    elif channel == 2:
        channel = AnalogIn(ads, ADS.P2)
    elif channel == 3:
        channel = AnalogIn(ads, ADS.P3)
    else:
        sys.exit("Error seleccionando un canal del ADS1115")

    # Se comienza la calibración con la lectura de ese canal
    calibrarPH(channel)


if __name__ == '__main__':
    main()
