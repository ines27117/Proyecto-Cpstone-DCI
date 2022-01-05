import time

from lecturas import turbidez, nivel_agua, temperatura


def main():
    while True:
        time.sleep(0.5)
        _turbidez, val_turbidez = turbidez.obtenerTurbidez()
        sensor_1, sensor_2 = nivel_agua.obtenerNivel()
        _temperatura = temperatura.leer_temp()

        print(val_turbidez, "Contenedor 1 esta medio lleno?:", sensor_1, "Contenedor 2 esta medio lleno?:", sensor_2,
              "Temperatura: ", _temperatura)


if __name__ == '__main__':
    main()
