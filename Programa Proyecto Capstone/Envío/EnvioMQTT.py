"""
	Envio de datos a través de MQTT usando Python.
	
	Instalación requerida: paho-mqtt
		(Instalar en ubuntu con: sudo pip3 install paho-mqtt
		Todos los programas que usen paho-mqtt se deben ejecutar con python3)
  
  ***********************************************************************
  Ejemplo muestra de cómo se conecta a un tema de MQTT a través de python
"""
import paho.mqtt.client as mqtt
import time
from random import randrange

#Indica el broker al el que se va a enviar la información
#broker="127.0.0.1"
broker="18.158.198.79"

#Trata la conección de un usuario al broker. Usar un usuario que no esté ocupado
try:
    cliente=mqtt.Client("UsuarioEquipoInesIoT-SICUAM")
    cliente.connect(broker)
except:
    print("Error al intentar conectar el usuario")

#Temas a los que se va a publicar información
topicNivel1="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/NivelAgua1"
topicNivel2="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/NivelAgua1"
topicPH="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/PH"
topicTemp="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/Temperatura"
topicTurb="ProyectoCapstone/EquipoInes/Samsung/UAM/Sensores/Turbidez"

#Suscripción del cliente a los temas en los que se van a publicar los mensajes
try:
    cliente.subscribe(topicNivel1)
    cliente.subscribe(topicNivel2)
    cliente.subscribe(topicPH)
    cliente.subscribe(topicTemp)
    cliente.subscribe(topicTurb)
    print("Suscripción a los temas correctamente")
except:
    print ("Error al intentar suscribirse a los temas")
    
while True:
    #Los valores numéricos se guardan en forma String (cadena) para ser enviados por MQTT
    nivelAgua1=str(randrange(0,2))
    nivelAgua2=str(randrange(0,2))
    ph=str(randrange(0,15))
    temperatura=str(randrange(10,30))
    turbidez=str(randrange(0,2))
    
    #Publicar el mensaje en el tema en especifico
    cliente.publish(topicNivel1, nivelAgua1)
    cliente.publish(topicNivel2, nivelAgua2)
    cliente.publish(topicPH, ph)
    cliente.publish(topicTemp, temperatura)
    cliente.publish(topicTurb, turbidez)
    time.sleep(2)
    


