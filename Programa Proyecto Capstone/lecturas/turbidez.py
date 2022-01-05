import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# Función _map la cual es equivalente a la función map de arduino
# es decir que a partir de un valor de entrada dará un valor de salida
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def obtenerTurbidez():
    # Se inicializa el canal donde se va a leer el voltaje de la turbidez
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    channel = AnalogIn(ads, ADS.P0)

    turbidez = _map(channel.value, 13317, 15394, 100, 0)
    if turbidez <= 20:
        # Si el valor de turbidez es menor o igual a 20 quiere decir que el agua esta clara
        return 0, "El agua esta clara"
    elif 20 < turbidez < 50:
        # Si el valor de turbidez es mayor a 20, pero menor a 50 quiere decir que el agua está medio sucia
        return 1, "El agua esta medio sucia"
    else:
        # Si el valor es mayor o igual a 50 quiere decir que el agua esta sucia
        return 2, "El agua esta sucia"
