# encoding: utf-8
"""
Constants.py
"""
import numpy as np

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
    #  las ordenes disponibles
    ORDENES = [
        { "label": "ven",                               "codigo": ORDEN_VEN },
        { "label": "abre",                              "codigo": ORDEN_ABRE },
        { "label": "agarra",                            "codigo": ORDEN_AGARRA },
        { "label": "devuelve",                          "codigo": ORDEN_DEVUELVE },

        { "label": "bisturí",                           "codigo": 20 },
        { "label": "tijeras",                           "codigo": 21 },
        { "label": "jeringuilla",                       "codigo": 22 },
        { "label": "pinza",                             "codigo": 23 },
    ]
    ZONA_DE_TRABAJO = [-np.pi/8, np.pi/8, np.pi/8, 3*np.pi/4, -np.pi/8]
    # ZONA_DE_ENTREGA_RECOGIDA = [-np.pi, np.pi/2, 0, 0, 0]
    
    ZONA_DE_ENTREGA_RECOGIDA = [3*np.pi/4, np.pi/4, np.pi/3, np.pi/2.5, 0]
    POST_ZONA_DE_ENTREGA_RECOGIDA = [3*np.pi/4, np.pi/4, np.pi/3, 0, 0]
    PRE_ZONA_DE_ENTREGA_RECOGIDA = [3*np.pi/4, np.pi/6, np.pi/3, 0, 0]
    # ZONA_DE_ENTREGA_RECOGIDA = [1.35619, 0.5708, 0.785398, 1.0944, 0.5708]

    # 135, -90, -45, 120, -90
