#!/usr/bin/env python3
"""
GAAR-I: Generic Arm Assist Robot - Intelligent
"""

__author__ = "GAAR-I"
__version__ = "0.1.0"
__license__ = "MIT"

import re
import argparse
import asyncio
from IK import servoPosition, inverseKinematic
from constants import const, colors
from utils import echo

#  las ordenes disponibles
ordenes = [
    { "label": "exit",                              "codigo": 0 },
    { "label": "ven",                               "codigo": 1 },
    { "label": "abre",                              "codigo": 2 },
    { "label": "devuelve",                          "codigo": 3 },
    { "label": "bisturi",                           "codigo": 4 },
    { "label": "abrazadera de diseccion recta",     "codigo": 5 },
    { "label": "tijeras mayo curva",                "codigo": 6 },
    { "label": "tijeras de mayo recta",             "codigo": 7 },
]


# Esta funcion es la que se encarga de recibir el codigo de la orden
# y ejecutar la funcion o el workflow pertinente.
def procesar_orden(codigo):
    if codigo == 1: # ven
        # llamada a una funcion del fichero IK...
        echo("Garri viene", color=colors.OKGREEN)
        pass
    if codigo == 2: # abre
        # llamada a una funcion
        echo("Garri está abriendo", color=colors.OKGREEN)
        pass
    if codigo == 3: # devuelve
        # llamada a una funcion
        echo("Garri va a devolver", color=colors.OKGREEN)
        pass
    if codigo > 3: # traer objeto
        # llamada a una funcion
        echo("Garri vooooy", color=colors.OKGREEN)
        pass


# Esta funcion es la que seejecuta en bucle y es la encargada de
# interpretar las ordenes y delegar las tareas a diferentes modulos
# del programa.
async def intrpretar_comandos():
    echo("Escuchando...", color=colors.OKGREEN)

    orden_actual = None
    cmd_text = ""

    while True:
        # por el momento leer la orden por la consola
        cmd_input = input("Escribe la orden:\n")

        # considerar la entrada si la orden empieza con la palabra "garri"
        if re.search("^garri", cmd_input):
            orden = cmd_input.split()

            # comprobamos que la orden tiene almenos dos palabras
            if len(orden) > 1:
                # solo nos interesa la segunda palabra
                orden = orden[1]

            # comprobar si la orden existe
            orden_existe = False
            orden_codigo = None
            for _orden in ordenes:
                if orden == _orden["label"]:
                    orden_existe = True
                    orden_codigo = _orden["codigo"]

            print(orden_codigo)
            if orden_existe:
                # orden para salir de la ejecución
                if orden_codigo == 0:
                    pass

                # To-Do: Comprobar si la orden es posible
                orden_actual = orden_codigo

                # llamar la función para procesar la orden
                procesar_orden(orden_codigo)

            else:
                echo(const.PRINT_PREFIX + "No te he entendido, repite porfavor.", color=colors.FAIL)


def robot_idle():
    # posicion de reposo
    initial_position = servoPosition(const.ROBOT_INITIAL_FK_POSITION)


def init():

    echo(const.PRINT_PREFIX + "Inicializando...")

    # colocar el robot en la posicion de reposo
    robot_idle()
    echo(const.PRINT_PREFIX + "Ya estoy en reposo")

    # empezar a escuchar a los comandos de robot
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(intrpretar_comandos())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        echo("Cerrando...")
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