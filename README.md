# GAAR-I
<b>Generic Arm Assist Robot - Intelligent</b>

# Tabla de contenidos
<img src="https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/scene_1.png" align="right" width="300" alt="header pic"/>

   * [What is this?](#what-is-this)
   * [Descripción](#descripción)
   * [Requerimientos](#requerimientos)
   * [Esquema del hardware](#esquema-del-hardware)
   * [Arquitectura del software](#arquitectura-del-software)
   * [Módulos](#módulos)
      * [Reconocimiento de voz](#reconocimiento-de-voz)
      * [Detección de objetos](#detección-de-objetos)
      * [Cinemática inversa](#cinemática-inversa)
      * [Planificación de secuencias de movimiento](#planificación-de-secuencias-de-movimiento)
      * [Control de flujo](#control-de-flujo)
   * [Componentes y piezas 3d](#componentes-y-piezas-3d)
   * [Simulación](#simulación)
   * [Contribuciones](#contribuciones)
   * [Autores](#autores)

# What is this?

Somos un grupo de estudiantes de ingeniería informática que hemos cursado la asignatura de Robótica, Lenguage y Planificación y hemos creado este brazo robótico como proyecto de la asignatura.

A causa de la pandemia del COVID-19 no se ha podido realizar la construcción de la parte física y del hardware y por lo tanto esa parte ha tenido que ser simulada. Más adelante encontrareis una guía para que cualquiera pueda ejecutar el código y ver el funcionamiento de este.

# Descripción

<img src="https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/animacion-robot.gif" align="right" width="400" alt="animacion robot"/>



GAAR-I es un brazo robótico inteligente, asistente de materiales y objetos.  A través de un módulo de reconocimiento de voz se le indica un objeto a seleccionar situado en la base del robot, y gracias a la visión por computador identifica el objeto y se lo proporciona al usuario.

Nuestro robot está contextualizado en el ámbito quirúrgico, donde un médico/cirujano pedirá un instrumento que necesite como podría ser el bisturí y se lo acercará.
El funcionamiento del brazo consistirá en una primera fase donde el brazo estará situado en una posición inicial con una cámara apuntando a la base donde se encuentran los instrumentos implicados en la cirugía.

Al emitir una orden de forma oral el cirujano el robot procesa la petición del objeto en demandado y a través de la camará y algorítmicas de visión por computador se llevará a cabo el reconocimiento del instrumento y dará a la orden al brazo de 5 ejes para que llegue a esa posición mediante la cinemática inversa. Una vez el instrumento está en la pinza este irá a una posición fija donde sostendrá el objeto a una posición elevada cercana al cirujano para que este pueda coger el objeto deseado sin necesidad de mucho esfuerzo, lo que le permitirá seguir concentrado en la cirugía. En el momento en el que el cirujano coge el instrumento de la pinza este tendrá que emitir otra orden para que se abra la pinza y libere el objeto, una vez liberado el robot volverá a la posición inicial.

En el caso inverso, donde el cirujano quiere dejar un objeto,  este tendrá que emitir otra orden para que el brazo vaya a la posición cerca del cirujano y este coloque el objeto en las pinzas, cuando quiera que el brazo cierre la pinza y devuelva el objeto juntos al resto deberá especificarlo.

Las órdenes disponibles que hay son:
- GAAR-I “objeto”: Con esta orden el brazo acercará el objeto al cirujano y esperará a nuevas órdenes. La palabra “objeto” deberá ser sustituida por el instrumento deseado.
- GAAR-I abre: La pinza se abrirá y después de un segundo volverá a su posición inicial.
- GAAR-I devuelve “objeto”: La pinza se cerrará y después de un segundo procederá a dejar el objeto en su posición inicial y volverá a su posición inicial.  La palabra “objeto” deberá ser sustituida por el instrumento deseado.
- GAAR-I ven: Con esta orden el brazo se acercará al cirujano con la pinza abierta a la espera de nuevas órdenes.

El conjunto de objetos que va a ser capaz de reconocer serán los siguientes:
- Pinzas
- Bisturí
- Jeringuilla
- Tijeras

# Requerimientos

Para poder ejecutar el código se necesita tener instalado Anaconda y el simulador Coppelia.

Es necesario descargar dos archivos que corresponden a los pesos inciales de la red neuronal YOLOv2 (full_yolo_backend.h5) y los pesos finales despues de realizar el reentreno (final_weights.h5). Descargar ambos ficheros de este [link](https://drive.google.com/drive/folders/1kTTjqQHphzvhfBYMRvWN7xF5b4su-gsq?usp=sharing) y guardar en la carpeta *Software*.

Según el sistema operativo que se utiliza debemos colocar los archivos *sim.py*, *simConst.py* y *remoteApi.so* correctos dentro de la carpeta *Software/coppelia* y eliminar los ya existente. Para encontrar estos archivos se debe ir a *Software/coppelia/windows* o *Software/coppelia/linux* según se requiera. Una vez hecho esto hay que seguir una sería de pasos que dejaremos anotados a continuación.

## Windows

- Primero de todo abriremos la consola de Anaconda, Anaconda Prompt.
- Una vez abierto crearemos un entorno con la versión de Python correcta, la 3.6:
``` conda create -n gaari python=3.6 ```
- Ahora debemos activar el entorno creado con el comando:
``` conda activate gaari ```
- Seguidamente instalaremos las liberías necesarías:
```
pip install tensorflow==1.13.2
pip install keras==2.0.8
pip install imgaug==0.2.5
pip install opencv-python
pip install h5py==2.10.0
pip install tqdm
pip install imutils
pip install sympy
pip install SpeechRecognition
pip install pipwin
pipwin install pyaudio 
```
- Antes de ejecutar el código debemos abrir una de las escenas que hay dentro de la carpeta *Software/coppelia* con el Coppelia y darle al run.
- Finalmente debemos situar la consola dentro de la carpeta *Software* y ejecutar el comando:
```python gaari.py```

## Linux
- Primero de todo abriremos una consola.
- Una vez abierto crearemos un entorno con la versión de Python correcta, la 3.6:
``` conda create -n gaari python=3.6 ```
- Ahora debemos activar el entorno creado con el comando:
``` conda activate gaari ```
- Seguidamente instalaremos las liberías necesarías:
```
pip install tensorflow==1.13.2
pip install keras==2.0.8
pip install imgaug==0.2.5
pip install opencv-python
pip install h5py==2.10.0
pip install tqdm
pip install imutils
pip install sympy
pip install SpeechRecognition
pip install pyaudio 
```
- Si la instalación de *pyaudio* da problemas hay que instalar el siguiente paquete: ```sudo apt-get install portaudio19-dev```
- Antes de ejecutar el código debemos abrir una de las escenas que hay dentro de la carpeta *Software/coppelia* con el Coppelia y darle al run.
- Finalmente debemos situar la consola dentro de la carpeta *Software* y ejecutar el comando:
```python gaari.py```

# Esquema del hardware

La imágen representa el esquema hardware que tendríamos que haber realizado en caso que hubieramos podido realizar el brazo robótico físicamente. Los componentes han sido seleccionados teniendo en cuenta que se dispone de un presupuesto limitado, con lo que para construir este proyecto se necesitarían 116,5€. En el cálculo del presupuesto se ha realizado teniendo en cuenta los costes de los materiales para la impresión 3D y los cables para realizar las conexiones.

![Esquema del hardware](https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/hardware.png)

# Arquitectura del software

![Esquema del software](https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/esquema_sw.PNG)

Como se puede observar en la anterior imagen, GAAR-I está conformado por 5 módulos principales:
- Módulo de reconocimiento de voz, que mediante los comandos que el usuario le dicta es capaz de realizar lo que este desea.
- Módulo de detección de objetos el cual le permite detectar objetos y decidir por dónde y con qué orientación coger el instrumento.
- Módulo de planificación de trayectorias donde están determinadas las posiciones iniciales y el conjunto de movimientos que debe realizar según la orden indicada a realizar.
- Módulo de la cinemática inversa, el cual se encarga de calcular los ángulos necesarios para llegar a la posición del instrumento y poderlo coger correctamente.
- Módulo del control de flujo, encargado de coordinar todos los anteriores módulos para conseguir el objetivo del robot.
La cámara, que se utiliza cuando GAAR-I debe detectar un objeto para dárselo al cirujano, el micrófono para escuchar lo que se le ordena y los servos que permiten el movimiento están conectados a la Raspberry Pi.


# Módulos

## Reconocimiento de voz

Tal y como se ha mencionado en el apartado de Arquitectura del Software, uno de los módulos más importantes es el reconocimiento de voz. En este apartado, se explicará más en detalle su funcionamiento y se mostrará el resultado obtenido.
La librería de python SpeechRecognition nos permite mediante la API de Google, transformar un input de audio a texto. De esta manera podemos pasarle los comandos a procesar por los demás módulos de GAAR-I. Una de las características de este módulo es que está constantemente “escuchando” o esperando una orden por parte del usuario, debido a esto, se le ha añadido una opción de supresión de sonido ambiente para que el input pueda ser más nítido. Además, se ha escogido como único idioma intérprete el español. Este es el listado total de órdenes que GAAR-I acepta:

GAAR-I tijeras 			(entrega el objeto tijeras)
GAAR-I bisturí 			(entrega el objeto bisturí)
GAAR-I jeringuilla 			(entrega el objeto jeringuilla)
GAAR-I pinza			(entrega el objeto pinza)
GAAR-I abre				(abre la pinza)
GAAR-I ven				(va a la posición de entrega/recogida)
GAAR-I devuelve tijeras		(devuelve tijeras a su posición inicial)
GAAR-I devuelve bisturí		(devuelve bisturí a su posición inicial)
GAAR-I devuelve jeringuilla	(devuelve jeringuilla a su posición inicial)
GAAR-I devuelve pinza		(devuelve pinza a su posición inicial)
apágate / adiós			(apaga el robot)


El nombre GAAR-I lo detecta como “Gary” o “Cari”, de manera interna se trata con estos términos.
Constantemente está sacando información por consola para saber el estado en el cual nos encontramos. En caso que se introduzca una orden válida, mostrará ésta por consola y en caso que la orden no sea válida, pedirá que se vuelva a repetir. Este es un ejemplo de un ciclo entero de entregar y recoger un objeto con errores forzados de por medio:

![Reconocimiento de voz](https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/voice_recognition.PNG)

## Detección de objetos

El módulo de visión ha sido implementado mediante la red neuronal YOLOv2. Para que esta proceda a la detección de objetos primeramente se ha realizado un trabajo de recopilación de datos, más concretamente se han obtenido aproximadamente unas 2000 imágenes de los objetos a reconocer con diferentes ángulos, perspectivas, escalas y fondos. Después de capturar las imágenes se ha realizado un proceso de etiquetado, en el cual mediante una herramienta especializada para ello se ha especificado qué objeto es cada uno, creando así las 4 clases de objetos que se detectan.
Una vez ya obtenido el dataset se ha procedido a entrenar la red para conseguir la clasificación de los objetos que aparecen en la escena. Una vez ya entrenada, como entrada toma la nueva imagen y como salida devuelve los bounding box donde se encuentra cada objeto.
Como ejemplo, si las imagenes de entrada fueran las siguientes:

<img src="https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/area_trabajo.PNG" height="250" width="250"><img src="https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/area_trabajo2.PNG" height="250" width="250">


La salida de la red sería, por cada instrumento que detectase, el bounding box donde ha detectado ese objeto y el label/clase de este. La salida aplicada a las anteriores imagenes quedaría de la siguiente manera, respectivamente:

<img src="https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/bounding_boxes.PNG" height="250" width="250"><img src="https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/bounding_boxes2.PNG" height="250" width="250">



Una vez se tienen las herramientas que ve el robot clasificadas, se recorta el bounding box del instrumento deseado, quedando como la siguiente imagen:

![Bounding box de la jeringuilla](https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/bb_jeringuilla.PNG) 

El siguiente paso es binarizar la imagen, y aplicar morfología matemática, concretamente un “close” para rellenar posibles vacíos dentro del instrumento y en el caso de que el objeto sea una pinza posteriormente se le realiza una dilatación ya que es un instrumento muy fino e interesa aumentar el grosor para facilitar el último paso. Con todo esto se obtiene el objeto con una forma sólida, minimizando agujeros dentro del objeto y eliminando pequeños píxeles ruidosos de la imagen, quedando imágenes como la del ejemplo:

![Bounding box jeringuilla con binarización y morfología](https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/bb_jeringuilla_morfo.PNG)

Con todo este tratamiento podemos aplicar una función a la imagen resultante para encontrar el centro del objeto y su orientación, es decir encontramos la posición X e Y de destino y la orientación que debe tomar el último eje para poder coger el objeto de forma correcta.

## Cinemática inversa

Esquema simplificado del robot:

![Esquema simplificado de GAAR-I](https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/esquema_gaari.PNG)

Parámetros Denavit-hartenberg:

![Matriz DH](https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/dh.PNG)

Para realizar la cinemática inversa del robot, al tratarse de un brazo de cinco ejes no se ha podido realizar mediante la matriz de parámetros de Denavit-Hartenberg. Por ello la solución se ha realizado mediante métodos geométricos y desacoplamiento cinemático mediante los ángulos de Euler.
GAAR-I tiene el objetivo de determinar la posición en la que se encuentra el objeto deseado, para ello tiene acoplada una cámara que le permite captar los instrumentos que hay. La cámara está enfocada en el área de trabajo del brazo, por ello lo que se captura es una pequeña parte de la escena. Mediante la visión por computador se determina cuál es el instrumento deseado y determina cuáles son las coordenadas de ese objeto respecto al área de trabajo. Una vez determinadas, estas coordenadas se tienen que pasar a las coordenadas reales globales de la escena, para ello se hace un escalado y una traslación en base a unos puntos de referencia predefinidos.
A continuación se observan los cálculos realizados por el algoritmo para llevar a cabo la orden de traer la jeringuilla:


<img alt="Secuencia cinematica" src="https://github.com/RogerRey14/GAAR-I/blob/main/Documentacion/Imagenes/grafica_cinematica.gif" width="350" />

## Planificación de secuencias de movimiento

Este módulo se dedica a crear una secuencia de movimientos del robot para poder llevar a cabo una orden.
Empieza desde su posición inicial (reposo), ejecuta la orden y vuelve a su posición de reposo.
Ejemplo:
- El robot se encuentra en posición de reposo preprogramada.
- Se le ordena traer un objeto en concreto.
- El robot planificará la siguiente secuencia:
  - Ir desde la posición actual a la de la zona de los objetos.
  - Navegar a la posición concreta del objeto a recoger.
  - Realizar las operaciones de la pinza para agarrar el objeto.
  - Navegar a la posición preprogramada para ofrecer el objeto al usuario.
  - Volver a la posición de reposo del robot.


## Control de flujo

El módulo de control de flujo se dedica a controlar y coordinar el resto de módulos para poder efectuar las órdenes deseadas por el usuario.
Esta parte es la encargada de: 
- Poner en marcha al robot y realizar la secuencia de inicialización y pruebas.
- Tener integrados los algoritmos de voice-to-text.
- Tener integrado el algoritmo de planificación de la secuencia de movimientos.
- Ejecutar la secuencia de movimiento usando la cinemática inversa.
- Usar algoritmos de visión para ubicar los objetos.
- Controlar el estado de la secuencia de movimientos.
- Ver si la orden se ha completado para volver a la posición de reposo.
- Esperar a la siguiente orden.


# Componentes y piezas 3d

# Simulación

La escena, estará ambientada en una sala de operaciones donde se realiza una operación. Dispondremos de varios objetos para realizar una simulación lo más realista posible, como son una camilla con un paciente tumbado encima, una mesita quirúrgica donde se entregarán los objetos que se ordene el cirujano/médico,  una mesa sobre la que estará GAAR-I, en la misma mesa estarán depositados los objetos que se le pedirán a GAAR-I y más elementos de atrezzo para la escena como paredes, una puerta, estanterías, botiquines, lámparas e incluso aparatos tecnológicos . El robot estará posicionado de manera estratégica para poder asistir óptimamente al cirujano/médico, que estará frente al paciente.

La simulación se realizará mediante la interconexión entre Coppelia y Script de Python.

# Contribuciones

Estas son las contribuciones que aporta nuestro proyecto al mundo, sobre todo en el ámbito quirúrgico y medicinal:
- Automatización del proceso de asistencia de objetos a un cirujano/médico. 
- Reducción de personal durante los procesos quirúrgicos en una sala de operaciones.
- Mayor precisión a la hora de asistir al cirujano/médico acercándo los instrumentos que sean necesarios.
- Gracias al control por voz, se permite dar órdenes al brazo robótico y tener libres las manos al mismo tiempo.
- Visión por computador integrada con una inteligencia artificial que permite determinar cuál es el objeto deseado, permitiendo que la colocación de los objetos no esté totalmente predefinida y tenga cierto grado de flexibilidad.
- Evita la pérdida de tiempo y errores humanos derivados de la presión, distracción o cansancio. ya que el brazo robótico reconoce y encuentra el objeto rápidamente. 


# Autores
- [Daniel López Lara](https://github.com/Dani26999)
- [Javier Alegre Revuelta](https://github.com/Javier-21)
- [Roger Rey Mesa](https://github.com/RogerRey14)
- [Mohsin Ríaz](https://github.com/im-mou)
