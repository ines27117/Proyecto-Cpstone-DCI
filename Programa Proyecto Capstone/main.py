import time
import paho.mqtt.client as mqtt

from lecturas import turbidez, nivel_agua, temperatura, sensorPH

broker = "3.126.191.185"
# Trata la conexión de un usuario al broker
try:
    cliente = mqtt.Client("Zerol")
    cliente.connect(broker)
except:
    print("Error al intentar conectar el usuario")

topicNivel1 = "ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/NivelAgua1"
topicNivel2 = "ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/NivelAgua2"
topicPH = "ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/PH"
topicTemp = "ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/Temperatura"
topicTurb = "ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/Turbidez"


def main():
    while True:
        time.sleep(0.5)
        _turbidez, val_turbidez = turbidez.obtenerTurbidez()
        sensor_1, sensor_2 = nivel_agua.obtenerNivel()
        _temperatura = temperatura.leer_temp()
        _sensorPH = sensorPH.obtenerPH()
        cliente.publish(topicNivel1, sensor_1)
        cliente.publish(topicNivel2, sensor_2)
        cliente.publish(topicPH, _sensorPH)
        cliente.publish(topicTemp, _temperatura)
        cliente.publish(topicTurb, _turbidez)

        print(val_turbidez, "Contenedor 1 esta medio lleno?:", sensor_1, "Contenedor 2 esta medio lleno?:", sensor_2,
              "Temperatura: ", _temperatura, "PH:", _sensorPH)


if __name__ == '__main__':
    main()
