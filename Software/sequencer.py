import time

from IK import IK
from servoPosition import servoPosition
from constants import const


invK = IK()

#    ORDENES = [
#         { "label": "ven",                               "codigo": ORDEN_VEN },
#         { "label": "abre",                              "codigo": ORDEN_ABRE },
#         { "label": "agarra",                            "codigo": ORDEN_AGARRA },
#         { "label": "devuelve",                          "codigo": ORDEN_DEVUELVE },

#         { "label": "bisturí",                           "codigo": 20 },
#         { "label": "tijeras",                           "codigo": 21 },
#         { "label": "jeringuilla",                       "codigo": 22 },
#         { "label": "pinza",                             "codigo": 23 },
#     ]

'''
casos de uso:

caso 1: el cirujano quiere un objeto "traer objeto":
    *   garri esta en posicion inicial con la pinza abierta

    cirujano    >   "gaari <<nombre objeto>>"
    garri       <   mueve a la posición de la "zona de trabajo"
                <   toma una foto y con la IK saca las coordenadas
                <   se acerca al objeto
                <   cierra la pinza (make child)
                <   mueve a la posicion de "zona de trabajo"
                <   mueve a la posicion de "recogida/entraga"
                <   Espera a la orden de "gaari abre"
    cirujano    >   "gaari abre"
    garri       <   abre la pinza y elimina el child
                <   mueve a la posición de la "zona de trabajo"


caso 2: : devolver un objeto a su posicion de recogida
    *   el robot esta en posicion "zona de trabajo" con la pinza abierta

    cirujano    >   "gaari ven"
    garri       <   mueve a la posicion de "recogida/entraga"
    cirujano    >   "gaari cierra"
    garri       <   cierra la pinza y crea el child
    cirujano    >   "gaari devuelve <<nombre objeto>>"
    garri       <   mueve a la posicion de "zona de trabajo"
                <   mueve a la posicion de especifica de donde se recogió el objeto
                <   abre la pinza y elimina el child
                <   mueve a la posición de la "zona de trabajo"

'''


class sequencer(object):

    sim = None

    def __init__(self, simInstance):
        self.sim = simInstance

    def ven(self):
        self.sim.setPose(const.ZONA_DE_ENTREGA_RECOGIDA)

    # reqiuere pruebas addicionales
    def abre(self):
        if self.sim.current_object != None:
            self.sim.open_grip(self.sim.current_object)
        else:
            self.sim.gripper(0)

        self.sim.setPose(const.ZONA_DE_TRABAJO)

    def agarra(self):
        if self.sim.current_object != None:
            self.sim.close_grip(self.sim.current_object)
        else:
            self.sim.gripper(1)

    def devuelve(self, codigo):

        #otra entrada de audio "gary devuelve <objeto>" MODIFICAR FICHERO AUDIO
        #partimos posicion zona de entrega con pinza cerrada

        self.sim.setPose(const.ZONA_DE_TRABAJO)

        x = self.sim.object_positions[codigo][0]
        y = self.sim.object_positions[codigo][1]
        z = self.sim.object_positions[codigo][2]

        angulos3 = invK.inverse_kinematics(x, y, z)
        self.sim.setPose(servoPosition(angulos3).get("rad"))

        self.abre()


    def objeto(self, codigo):
        self.sim.setPose(const.ZONA_DE_TRABAJO)

        # toma foto y saca las x, y, z -> vision
        x = 0.4
        y = 0.225
        z = 0.78

        # usar otra variable para grados
        angulos1 = invK.inverse_kinematics(x, y, z)

        self.sim.setPose(servoPosition(angulos1).get("rad"))

        # toma foto y saca las x, y, z -> vision
        x = 0.4
        y = 0.225
        z = 0.705

        angulos2 = invK.inverse_kinematics(x, y, z)
        self.sim.setPose(servoPosition(angulos2).get("rad"))

        # guardar la pocicion del objeto a recoger
        self.sim.object_positions[codigo][0] = x
        self.sim.object_positions[codigo][1] = y
        self.sim.object_positions[codigo][2] = z

        # cierra la pinza (make child)
        self.sim.close_grip(self.sim.object_positions.get(codigo)[3])

        #  mueve a la posicion de "zona de trabajo"
        self.sim.setPose(const.ZONA_DE_TRABAJO)

        #  mueve a la posicion de "recogida/entraga"
        self.sim.setPose(const.ZONA_DE_ENTREGA_RECOGIDA)



