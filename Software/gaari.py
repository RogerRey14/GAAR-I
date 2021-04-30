#!/usr/bin/env python3
"""
GAAR-I: Generic Arm Assist Robot - Intelligent
"""

__author__ = "GAAR-I"
__version__ = "0.1.0"
__license__ = "MIT"

import re, sys
import argparse
import asyncio
from IK import inverseKinematic
from servoPosition import servoPosition
from constants import const, colors
from utils import echo

#  las ordenes disponibles
ordenes = [
    { "label": "ven",                               "codigo": const.ORDEN_VEN },
    { "label": "abre",                              "codigo": const.ORDEN_ABRE },
    { "label": "agarra",                            "codigo": const.ORDEN_AGARRA },
    { "label": "devuelve",                          "codigo": const.ORDEN_DEVUELVE },

    { "label": "bisturi",                           "codigo": 20 },
    { "label": "abrazadera de diseccion recta",     "codigo": 21 },
    { "label": "tijeras mayo curva",                "codigo": 22 },
    { "label": "tijeras de mayo recta",             "codigo": 23 },
]

# lista de las ordenes permitidas dependiendo del estado actual del gaari
secuencias_permitidas = [
    { const.ORDEN_VEN : [const.ORDEN_ABRE, const.ORDEN_AGARRA ] },
    { const.ORDEN_ABRE : [const.ORDEN_AGARRA ] },
    { const.ORDEN_AGARRA : [const.ORDEN_DEVUELVE] },
]

# Esta funcion es la que se encarga de recibir el codigo de la orden
# y ejecutar la funcion o el workflow pertinente.
def procesar_orden(codigo):
    if codigo == const.ORDEN_VEN: # ven
        # llamada a una funcion del fichero IK...
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


# Esta funcion es la que seejecuta en bucle y es la encargada de
# interpretar las ordenes y delegar las tareas a diferentes modulos
# del programa.
async def intrpretar_comandos(loop):
    echo("Escuchando...", color=colors.OKGREEN)

    orden_actual = None
    cmd_text = ""

    while True:
        # por el momento leer la orden por la consola
        cmd_input = input("Escribe la orden:\n")

        # considerar la entrada si la orden empieza con la palabra "gaari"
        if re.search("^gaari", cmd_input):
            orden = cmd_input.split()

            # comprobamos que la orden tiene almenos dos palabras
            if len(orden) > 1:
                # solo nos interesa la segunda palabra
                orden = orden[1]

            # comprobar si la orden existe
            orden_existe = False
            orden_solicitada = { "label": None, "codigo": None }
            for _orden in ordenes:
                if orden == _orden["label"]:
                    orden_existe = True
                    orden_solicitada = _orden


            # Comprobar si la secuencia del orden es posible
            if orden_existe:
                orden_valida = False

                if orden_actual != None:
                    for seq in secuencias_permitidas:
                        ordenes_posibles = seq.get(orden_actual)
                        if ordenes_posibles != None and len(ordenes_posibles) > 0:
                            for _ord in ordenes_posibles:
                                if _ord == orden_solicitada["codigo"]:
                                    orden_actual = orden_solicitada["codigo"]
                                    orden_valida = True
                                    break
                else:
                    # si el la primera orden, no imponemos ninguna restriccion
                    orden_actual = orden_solicitada["codigo"]
                    orden_valida = True


                if orden_valida:
                    # llamar la función para procesar la orden
                    procesar_orden(orden_solicitada["codigo"])
                else:
                    echo(const.GAARI_SAYS + "La orden no es valida.", color=colors.WARNING)

            else:
                echo(const.GAARI_SAYS + "No te he entendido, repite porfavor.", color=colors.FAIL)

        # parar la ejecución
        elif cmd_input == 'exit' or cmd_input == 'bye':
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