# Programa creado por Mejia Bazan Cesar Arturo 2182005565
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def obtenerPH():
    # Se inicializa el canal donde se va a leer el voltaje de la turbidez
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    channel = AnalogIn(ads, ADS.P1)
    voltaje = 0.0
    for x in range(5):
        voltaje = voltaje + channel.voltage
        
    voltaje = voltaje/5
    voltaje = round(voltaje,2)
    # Ecuación de la recta
    ph = round((-voltaje + 22.115)/5.7692 , 1)
#     print("v:",voltaje, "ph:", ph)
    return ph;
