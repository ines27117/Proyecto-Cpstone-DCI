# Programa creado por Mejia Bazan Cesar Arturo 2182005565
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


def obtenerPH():
    # Se inicializa el canal donde se va a leer el voltaje
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    # Se lee el canal en donde esta conectado el sensor de PH, en este caso es el A1 del ADS1115
    channel = AnalogIn(ads, ADS.P1)
    voltaje = 0.0
    # Se hacen 5 lecturas al canal analógico del ADS1115
    for x in range(5):
        time.sleep(0.1)
        voltaje = voltaje + channel.voltage

    # Se obtiene su promedio
    voltaje = voltaje / 5
    # Se redondea a 2 cifras significativas
    voltaje = round(voltaje, 2)
    try:
        # Se lee el archivo donde se encuentra la pendiente y la ordenada al origen
        file = open("recta.txt", "r")
        m, b = file.readline().split(",")
        m = float(m)
        b = float(b)
        # Se cierra el archivo
        file.close()
    except:
        # Si hubo un error en la conversion o en la lectura del archivo se regresa -1
        return -1
    # Ecuación de la recta
    ph = round((m * voltaje) + b, 1)
    #     print("v:",voltaje, "ph:", ph)

    # Se regresa el valor obtenido de Ph
    return ph
