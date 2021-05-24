# GAAR-I
<b>Generic Arm Assist Robot - Intelligent</b>

# Tabla de contenidos
   * [What is this?](#what-is-this)
   * [Descripción](#descripción)
   * [Requerimientos](#requerimientos)
   * [Esquema del hardware](#esquema-del-hardware)
   * [Arquitectura del software](#arquitectura-del-software)
   * [Módulos](#módulos)
      * [Reconocimiento de voz](#reconocimiento-de-voz)
      * [Detección de objetos](#detección-de-objetos)
      * [Cinemática inversa](#cinemática-inversa)
      * [Planificación de secuencias de movimiento](#planficación-de-secuencias-de-movimiento)
      * [Control de flujo](#control-de-flujo)
   * [Componentes y piezas 3d](#componentes-y-piezas-3d)
   * [Simulación](#simulación)
   * [Contribuciones](#contribuciones)
   * [Autores](#autores)

# What is this?

Somos un grupo de estudiantes de ingeniería informática que hemos cursado la asignatura de Robótica, Lenguage y Planificación y hemos creado este brazo robótico como proyecto de la asignatura.

A causa de la pandemia del COVID-19 no se ha podido realizar la construcción de la parte física y del hardware y por lo tanto esa parte ha tenido que ser simulada. Más adelante encontrareis una guía para que cualquiera pueda ejecutar el código y ver el funcionamiento de este.

# Descripción

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

# Arquitectura del software

# Módulos

## Reconocimiento de voz

## Detección de objetos

## Cinemática inversa

## Planificación de secuencias de movimiento

## Control de flujo

# Componentes y piezas 3d

# Simulación

# Contribuciones

# Autores
- [Daniel López Lara](https://github.com/Dani26999)
- [Javier Alegre Revuelta](https://github.com/Javier-21)
- [Roger Rey Mesa](https://github.com/RogerRey14)
- [Mohsin Ríaz](https://github.com/im-mou)