import RPi.GPIO as GPIO
import time


def obtenerNivel():
    # Se declaran los pines GPIO donde estarán los sensores de nivel del agua
    pin_sensor_1 = 19
    # pinSensor_2 = 26

    # Se inicializan los pines GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_sensor_1, GPIO.IN)
    # GPIO.setup(pin_sensor_2, GPIO.IN)
    # Se recupera el valor de los pines GPIO
    nivel_sensor_1 = int(GPIO.input(pin_sensor_1))
    nivel_sensor_2 = 1

    # Se limpian los pines GPIO
    GPIO.cleanup()
    # Se regresan los valores de los pines
    return nivel_sensor_1, nivel_sensor_2
    # return GPIO.input(pin_sensor_1), GPIO.input(pin_sensor_2)