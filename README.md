# Proyecto-Cpstone-DCI
Nombre: "Instrumentacion e implementacion del IoT en un filtro de aguas grises".

El agua es un recurso indispensable para la subsistencia de cualquier organismo vivo en el planeta tierra, al igual que es indisociable de cualquier actividad hecha por los seres humanos desde aspectos de la vida cotidiana como hidratarnos, asearnos, las labores de la casa, por mencionar algunos, hasta procesos más complejos como ocurre en la industria extractiva, metalúrgica, química, alimentaria, farmacéutica, de textiles, papelera etc.

A medida que fueron evolucionando estos tipos de industrias y fue cambiando el estilo de vida urbanita, se agravaron las problemáticas entorno al medio ambiente por la constante emisión de contaminantes, la sobre explotación de los recursos naturales, en particular el agua en la que influye determinantemente el crecimiento demográfico.

Actualmente a nivel mundial se ha vuelto una “tendencia” la preocupación por la recuperación de estos ecosistemas, muchas organizaciones, empresas e industrias están migrando a las Tecnologías limpias (verdes), que de acuerdo con la definición de la ONU en la agenda 2021, son los procesos y productos que protegen el ambiente, que son menos contaminantes, usan los recursos de forma sustentable, reciclan sus residuos y productos y manejan los desechos residuales de una manera aceptable. 

En la agenda 2030 de la ONU se plantean 17 objetivos del desarrollo sostenible, uno de estos abarca el punto sobre el “agua y saneamiento” donde muestran cifras alarmantes de que, en un futuro cercano más del 40 por ciento de las personas en el mundo sufran escasez de agua recurrente, experimentando el estrés hídrico y el aumento de la sequía y la desertificación. Por lo que se propone que los gobiernos inviertan en infraestructura adecuada, proporcionando instalaciones de saneamiento para la protección y restauración de los ecosistemas vinculados con el tema del agua, así como garantizar el agua en calidad y cantidades adecuadas para las personas.

Por otra parte, así como el agua es indisociable de las actividades del ser humano, el internet de las cosas se ha vuelto un tema emergente que enfrenta muchos desafíos y te da la posibilidad de solucionar todo tipo de problemáticas haciendo más eficiente el trabajo cotidiano, por lo que recolectar el agua va a ser un trabajo oficios que nos va a demandar tiempo y tecnología para poder acceder a este bien.


### Objetivo General

- Dentro de este trabajo el objetivo general es crear un modelo básico (mínimo indispensable) del internet de las cosas donde se articulen varios sensores y se envíe información sobre los parámetros del agua residual.

### Objetivos especificos:

- Diseñar un sistema de filtración de aguas grises manteniendo el flujo a presión.
- Determinar qué tipo de materiales son adecuados para una filtración eficiente de las aguas residuales domésticas.
- Desarrollar programas para la interconexión de los sensores asi como una base de datos donde se pueda tener un registro continuo de los datos obtenidos del agua, antes y después de pasar por el sistema de filtros.

### Circuito
El esquema realizado para la observación de los datos fue el siguiente:
![ProyectoCapstone_bb](https://user-images.githubusercontent.com/64336142/149452924-879e6827-8ae6-40a9-a864-bc96b17d29d3.png)

### Interfaces necesarias
Para correr el programa principal de este repositorio es necesario habilitar las interfaces i2c y 1-wire dentro de la raspberry pi, para esto es necesario ejecutar el siguiente comando en la terminal de la raspberry:
```
sudo raspi-config
```
Lo cual abrira la siguiente interfaz:
![primera_imagen](https://user-images.githubusercontent.com/64336142/148917349-8a87653a-faab-4552-8323-275b33009d67.png)

Donde utilizando el teclado seleccionaremos la tercera opcion "3 Interface Options", una vez seleccionada presionaremos Enter, lo que nos llevara a la siguiente pantalla
![Segunda_imagen](https://user-images.githubusercontent.com/64336142/148917647-b0358191-b879-452d-a67b-268600c8ad95.png)

Primero habilitaremos la interfaz i2c, por lo que con el teclado seleccionaremos esta opción y presionaremos Enter, nos saldra una ventana donde nos preguntara si deseamos habilitar la interfaz i2c a lo cual responderemos que si.
![Tercera_imagen](https://user-images.githubusercontent.com/64336142/148917822-44d6fe38-3b78-457d-ad7d-851e8b17e975.png)
![Cuarta_imagen](https://user-images.githubusercontent.com/64336142/148917882-eaec0423-71c9-41d4-8b4d-ecf691730072.png)

Ahora, para que este habilitada por completo será necesario reiniciar nuestra raspberry pi, en nuestro caso no lo haremos pues aun falta habilitar la interfaz 1-wire.

Volveremos a la ventada de configuracion de interfaces y ahora seleccionaremos la interfaz 1-wire, daremos enter.
![image](https://user-images.githubusercontent.com/64336142/148918082-ee4d817d-4c3e-46b9-9c4b-a40363c3999e.png)

Nos preguntará de la misma manera si queremos habilitar la interfaz 1-wire, le diremos que si.
![image](https://user-images.githubusercontent.com/64336142/148918414-5c7264dd-414e-4b7f-a037-8144b2c10d9a.png)
![image](https://user-images.githubusercontent.com/64336142/148918204-77a046a9-f35c-4ff7-b096-6dc9082af98f.png)

Lo cual nos dará el mensaje de que la interfaz ha sido habilitada, es ahora donde al volver a la ventada principal de raspi-config le daremos "Finish" y procederemos a reiniciar la raspberry pi.

Una ver reiniciada para verificar que estas dos interfaces están habilitadas solo será necesario ejecutar los siguientes comandos

```
sudo i2cdetect -y 1
```

Lo cual, si se habilito correctamente la interfaz, nos debe de dar una pantalla similar a la siguiente:
![image](https://user-images.githubusercontent.com/64336142/148919136-ab5f7f2b-6b72-4d51-9b75-fc2219748e07.png)

y para la interfaz 1-wire es necesario ejecutar el siguiente comando
```
lsmod | grep -i w1_
```

lo cual, si se habilito correctamente la interfaz, nos debe dar una pantalla similar a la siguiente:

![image](https://user-images.githubusercontent.com/64336142/148919728-37cf5325-a4a6-4b58-ac54-c2ac062f1aaf.png)

¡Listo!, has habilitado las dos interfaces necesarias para ejecutar este programa :)

### Programación
Para correr este programa tambien es necesario instalar la libreria CircuitPython y la libreria del ADS1x15 para CircuitPython, la primera se instala de la siguiente manera:

Abre una terminal y ejecuta el siguiente codigo

```
sudo pip3 install Adafruit-Blinka
```
y despues
```
sudo pip3 install adafruit-circuitpython-ads1x15
```

¡Listo!, ahora solo clona este repositorio dentro de tu raspberry pi y corre el archivo 
```
main.py
```
con tu IDE de Python 3.

### Envío de datos
Para poder enviar los datos a través de MQTT es necesario instalar su propia libreria:

```
sudo pip3 install paho-mqtt
```
Esto será suficiente para que el archivo pueda enviar los datos a través de cualquier broker haciendo usao de MQTT.

### Uso de InfluxDB para almacenar los datos y visualización en Grafana
Se hace uso de una base de datos para guardar todos resultados que el sistema envía, además que se necesita leer de forma clara todos estos valores. Para lograr esto se hace uso de Node-RED, InfluxDB y Grafana.

Node-RED es una plataforma útil que ayuda a unificar varias tecnologías entre sí. Para este caso, va a permitir obtener los datos recibidos por MQTT y cambiar su formato de tal forma que se puedan almacenar en la base de datos de InfluxDB.

InfluxDB va a contener todos los datos de los diferentes circuitos de tal forma que puedan ser usados por cualquier otro servicio, como Grafana.

Grafana será de gran utilidad a la hora de visualizar los datos de Influx, mostrando de forma clara los valores de los sensores. Se pueden crear paneles con diferentes gráficas para monitorear en tiempo real el sistema.

#### Instalación de MQTT broker
Para poder utilzar MQTT, también conocido como mosquitto, se debe de instalar y habilitar:
```
sudo apt install mosquitto mosquitto-clients

sudo systemctl enable mosquitto
```

Para encender Node-RED se debe de hacer desde terminal usando: 
```
node-red
```
Con esto, y por defecto, se podrá acceder desde un navegador accediendo a la dirección: 127.0.0.1:1880

#### Instalación de InfluxDB
InfluxDB se puede utilizar de manera online, desde su propia página, o manera local, instalando en la propia máquina. Para este proyecto se hizo de manera local, por lo que se hizo la instalación de InfluxDB usando los comandos: 
```
sudo apt install influxdb
sudo apt install influxdb-client
sudo service influxdb start
```
Ahora solo falta modificar una pequeña parte de influx para que se pueda utilizar. Escribiendo en una terminal: 
```
sudo nano /etc/influxdb/influxdb.conf
```
En la parte de "http" se debe descomentar: "enabled = true" borrando el símbolo de gato. Ahora faltaría reiniciar influx para poder utilizarlo.
```
sudo service influxdb restart
```

##### Uso de bases con Influx
Para facilitar el manejo de información, para cada circuito se hará una base de datos propia usando InfluxDB. Para hacer esto, desde una terminal se debe entrar a influx y crearla.
```
influx
```
Con este comando se entra a la terminal de InfluxDB. Una vez dentro se crearán las bases que se necesiten usando:
```
create database "nombre de la base"
```
Y para ver las bases que se han creado se usa:
```
show databases
```
Si ya no se requiere una base o se quiere eliminar por cualquier motivo se utiliza el comando:
```
drop database "nombre de la base"
```
Para salir de Influx basta con poner
```
exit
```









