import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


# Se lee la interfaz 1-wire
def leer_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


# Se lee la temperatura
def leer_temp():
    # A partir de lo leído en la interfaz 1-wire
    lines = leer_temp_raw()
    # Mientras la lectura no del mensaje de YES se espera el programa
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = leer_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        # Se regresa la temperatura en Celsius
        return temp_c
