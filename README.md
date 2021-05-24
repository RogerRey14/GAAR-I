# GAAR-I
<b>Generic Arm Assist Robot - Intelligent</b>

# Tabla de contenidos
   * [What is this?](#what-is-this)
   * [Descripción](#descripcion)
   * [Requerimientos](#requerimientos)
   * [Esquema de hardware](#esquema-de-hardware)
   * [Arquitectura del software](#arquitectura-del-software)
   * [Módulos](#modulos)
      * [Reconocimiento de voz](#reconocimiento-voz)
      * [Detección de objetos](#deteccion-objetos)
      * [Cinemática inversa](#cinematica-inversa)
      * [Planificación de secuencias de movimiento](#planficacion-movimiento)
      * [Control de flujo](#control-flujo)
   * [Componentes y piezas 3d](#3d)
   * [Simulación](#simulacion)
   * [Contribuciones](#conrtibuciones)
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
