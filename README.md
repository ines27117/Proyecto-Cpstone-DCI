# Proyecto-Cpstone-DCI
Nombre: "Implementación del IoT para el monitoreo del agua en su tratamiento con campo magnético".

Innovar en este proyecto es insoslayable retomar e incorporar a nuestra cotidianidad la tecnología, es mi proyecto que es cosechar agua de lluvia dentro de procedimientos innovadoras (aplicando toda la creatividad y las nuevas tecnologías) para cosechar agua de lluvia o incorporar agua grises de usos domestico y reciclarla utilizándola en nuestro día a día.

La idea del prototipo de proyecto es conducir el agua residual a través de un campo magnético, esta pasara  través de una tubería de vidrio. La función del campo magnético es reordenar las partículas de las sales  como: Carbonato de calcio, nitritos nitratos. nitrógeno amoniacal, etc. e incluso influir en los microorganismos que viven en la muestra de agua.

Como sabemos todos los organismos vivos tenemos un campo magnético. Todos somos energía y estamos compuestos por electrones, protones, neutrones. Así que someternos a la influencia de un campo magnético adicional puede tener un efecto benéfico en la organización y metabolización de los seres vivos (en caso de de acelerar su metabolismos estos consumirán algunos nutrientes en el agua y por ende incrementara la biodegradación).
En el caso de las sales, al ser influenciadas por el CM cambian su morfología, por ejemplo el carbonato de calcio y así prevenir o disminuir la formación de incrustaciones en las tuberías.

Lo innovador en el proyecto seria la implementación del internet de las cosas para medir los parámetros del agua al salir del campo magnético y determinar su calidad con algunos electrodos (ph, nitrógeno amoniacal, temperatura, oxido reductor, etc) y esto se tendría que comparar con los datos registrados en la NOM para determinar su calidad.

Cabe resaltar que el agua que se va obtener después del tratamiento no será potables, mas bien agua limpia, agua tratada que se podrá reutilizar para otros procesos e incluso de podría conducir a un humedal para continuar con su tratamiento o mandarla directamente para riego de cultivos extensos o tecnificados.

La problemática de este proyecto es el rigor con que se tiene que llevar acabo las medición de los parámetros, ya que en algunos artículos se mencionan mediciones de hasta 90 días, 30 o 15 días.

### Objetivos Generales

- Analizar y observar los efectos del campo magnético en la remoción de nutrientes y carga orgánica en tratamiento del agua residual domestica y del agua de lluvia.
- Aplicar distintas intensidades del campo magnético para determinar con cuales se obtienen resultados más óptimos.
- ODS: Garantizar la disponibilidad del agua y su gestión sostenible y saneamiento para todos.

### Objetivos especificos:

- Crear un modelo básico del internet de las cosas donde se puedan articular sensores y enviar información sobre los parámetros del agua residual por medio del internet.
- Desarrollar un programa donde se pueda tener un registro de los datos obtenidos del agua residual después de pasar por el tratamiento.
- Determinar si cumple con determinadas normativas para que el  agua tratada pueda ser reutilizada en otros procesos (agrícola, industrial, domestico, etc.).
- Aplicar técnicas de tratamiento a cuerpos de agua, en este caso del campo magnético.

### Circuito
El esquema realizado para la observación de los datos fue el siguiente:
![ProyectoCapstone_bb](https://user-images.githubusercontent.com/64336142/148916586-210c1b0c-3be5-4281-9fe5-823d2ed396dc.png)

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





