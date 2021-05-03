# encoding: utf-8
"""
Constants.py
"""
#  colores para la consola
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class const:
    ROBOT_TOTAL_AXIS = 5
    ROBOT_INITIAL_ANGLES = [0,0,0,0,0]
    GAARI_SAYS = 'GAARI says: '
    ORDEN_VEN = 1
    ORDEN_ABRE = 2
    ORDEN_AGARRA = 3
    ORDEN_DEVUELVE = 4