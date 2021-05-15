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
from IK import IK
from servoPosition import servoPosition
from constants import const, colors
from utils import echo
from simulator import simulator
from audio import VoiceRecognition
from sequencer import sequencer
import speech_recognition as sr

import time


sim = simulator()
voice = VoiceRecognition()
seq = sequencer(sim)

# Esta funcion es la que se encarga de recibir el codigo de la orden
# y ejecutar la funcion o el workflow pertinente.
def procesar_orden(codigo):
    if codigo == const.ORDEN_VEN: # ven
        seq.ven()
        echo(const.GAARI_SAYS + "Gaari viene", color=colors.OKGREEN)
    elif codigo == const.ORDEN_ABRE: # abre
        seq.abre()
        echo(const.GAARI_SAYS + "Gaari está abriendo", color=colors.OKGREEN)
    elif codigo == const.ORDEN_AGARRA: # agarra
        seq.agarra()
        echo(const.GAARI_SAYS + "Gaari agarra", color=colors.OKGREEN)
    elif codigo == const.ORDEN_DEVUELVE: # devuelve
        # llamada a una funcion
        echo(const.GAARI_SAYS + "Gaari va a devolver", color=colors.OKGREEN)
    else:
        seq.objeto(codigo)
        echo(const.GAARI_SAYS + "Gaari procesa el objecto", color=colors.OKGREEN)

    return True


# Esta funcion es la que seejecuta en bucle y es la encargada de
# interpretar las ordenes y delegar las tareas a diferentes modulos
# del programa.
async def interpretar_comandos(loop):
    echo("Escuchando...", color=colors.OKCYAN)

    code = None

    with sr.Microphone() as source:
        while True:

            code = voice.recognize(source)

            if code != "APAGAR":
                if code != "REPITE" and code != None:
                    # procesar la orden
                    procesar_orden(code)
            else:
                # apagar el robot
                return


def robot_idle():
    sim.resting_position()


def init():

    echo(const.GAARI_SAYS + "Inicializando...")

    # colocar el robot en la posicion de reposo
    robot_idle()
    echo(const.GAARI_SAYS + "Ya estoy en reposo")

    # empezar a escuchar a los comandos de robot
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(interpretar_comandos(loop))
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