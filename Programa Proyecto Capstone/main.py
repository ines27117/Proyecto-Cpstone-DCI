import time
import paho.mqtt.client as mqtt

from lecturas import turbidez, nivel_agua, temperatura, sensorPH

broker="18.158.198.79"
#Trata la conección de un usuario al broker
try:
    cliente=mqtt.Client("aewno-bgtdytd")
    cliente.connect(broker)
except:
    print("Error al intentar conectar el usuario")

topic0="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/PH1"
topic1="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/Turbidez"
topic2="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/Temperatura"
topic3="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/NivelAgua"


def main():
    while True:
        time.sleep(0.5)
        _turbidez, val_turbidez = turbidez.obtenerTurbidez()
        sensor_1, sensor_2 = nivel_agua.obtenerNivel()
        _temperatura = temperatura.leer_temp()
        _sensorPH=sensorPH.obtenerPH()
        cliente.publish(topic1, _turbidez)
        cliente.publish(topic0, _sensorPH)
        cliente.publish(topic2, _temperatura)
        cliente.publish(topic3, sensor_1)

        print(val_turbidez, "Contenedor 1 esta medio lleno?:", sensor_1, "Contenedor 2 esta medio lleno?:", sensor_2,
              "Temperatura: ", _temperatura,"PH:",_sensorPH)


if __name__ == '__main__':
    main()
