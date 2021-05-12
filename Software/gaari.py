#!/usr/bin/env python3
"""
GAAR-I: Generic Arm Assist Robot - Intelligent
"""

__author__ = "GAAR-I"
__version__ = "0.2.0"
__license__ = "MIT"

import re, sys
import argparse
import asyncio
from IK import inverseKinematic
from servoPosition import servoPosition
from constants import const, colors
from utils import echo
from simulator import simulator
from audio import VoiceRecognition
import speech_recognition as sr


sim = simulator()
voice = VoiceRecognition()

# Esta funcion es la que se encarga de recibir el codigo de la orden
# y ejecutar la funcion o el workflow pertinente.
def procesar_orden(codigo):
    if codigo == const.ORDEN_VEN: # ven
        # llamada a una funcion del fichero IK...
        print(sim.getDummyPosition())
        sim.setPose(servoPosition([90, 90, 90, 10, 10]).getAll("rad"))
        echo(const.GAARI_SAYS + "Gaari viene", color=colors.OKGREEN)
        pass
    elif codigo == const.ORDEN_ABRE: # abre
        # llamada a una funcion
        echo(const.GAARI_SAYS + "Gaari está abriendo", color=colors.OKGREEN)
        pass
    elif codigo == const.ORDEN_AGARRA: # agarra
        # llamada a una funcion
        echo(const.GAARI_SAYS + "Gaari agarra", color=colors.OKGREEN)
        pass
    elif codigo == const.ORDEN_DEVUELVE: # devuelve
        # llamada a una funcion
        echo(const.GAARI_SAYS + "Gaari va a devolver", color=colors.OKGREEN)
        pass
    else:
        # llamada a una funcion
        echo(const.GAARI_SAYS + "Gaari procesa el objecto", color=colors.OKGREEN)
        pass

    return True


# Esta funcion es la que seejecuta en bucle y es la encargada de
# interpretar las ordenes y delegar las tareas a diferentes modulos
# del programa.
async def intrpretar_comandos(loop):
    echo("Escuchando...", color=colors.OKCYAN)

    code = None

    with sr.Microphone() as source:
        while True:

            code = voice.recognize(source)

            if code != "APAGAR":
                if code != "REPITE" and code != None:
                    procesar_orden(const.ORDEN_VEN)
                    # procesar la orden
            else:
                # apagar el robot
                return


def robot_idle():
    # posicion de reposo
    initial_position = servoPosition(const.ROBOT_INITIAL_ANGLES)


def init():

    echo(const.GAARI_SAYS + "Inicializando...")

    # colocar el robot en la posicion de reposo
    robot_idle()
    echo(const.GAARI_SAYS + "Ya estoy en reposo")

    # empezar a escuchar a los comandos de robot
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(intrpretar_comandos(loop))
    finally:
        echo("Apagando...")
        loop.close()
        robot_idle()


def main(args):
    """ Punto de entrada """

    # Realizar pruebas para comprobar que todos los componentes funcionan bien
    # test_sequence()

    # Empezar la ejecucion
    init()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Optional argument which requires a parameter (eg. -d test)
    # parser.add_argument("-n", "--name", action="store", dest="name")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)