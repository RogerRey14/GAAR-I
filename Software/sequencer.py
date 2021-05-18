import time

from constants import const
from IK import IK
from servoPosition import servoPosition

invK = IK()


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
    altura_mesa = 0.71

    def __init__(self, simInstance):
        self.sim = simInstance

    def ven(self):
        self.sim.setPose(const.PRE_ZONA_DE_ENTREGA_RECOGIDA)
        time.sleep(2)
        self.sim.setPose(const.ZONA_DE_ENTREGA_RECOGIDA)

    # reqiuere pruebas addicionales
    def abre(self):
        if self.sim.current_object != None:
            self.sim.open_grip(self.sim.current_object)
        else:
            self.sim.gripper(0)
        time.sleep(3)
        self.sim.setPose(const.POST_ZONA_DE_ENTREGA_RECOGIDA)
        time.sleep(1.5)
        self.sim.setPose(const.ZONA_DE_TRABAJO)

    def abre_devuelve(self):
        if self.sim.current_object != None:
            self.sim.open_grip(self.sim.current_object)
        else:
            self.sim.gripper(0)
        #time.sleep(3)
        #self.sim.setPose(const.POST_ZONA_DE_ENTREGA_RECOGIDA)
        time.sleep(1.5)
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

        self.abre_devuelve()


    def objeto(self, codigo):
        self.sim.setPose(const.ZONA_DE_TRABAJO)

        # posicion fija
        x = 0.5250
        y = 0.0330

        # toma foto y saca las x, y, z -> vision

        # usar otra variable para grados
        angulos1 = invK.inverse_kinematics(x, y, self.altura_mesa + 0.075)
        self.sim.setPose(servoPosition(angulos1).get("rad"))

        angulos2 = invK.inverse_kinematics(x, y, self.altura_mesa)
        self.sim.setPose(servoPosition(angulos2).get("rad"))

        # guardar la pocicion del objeto a recoger
        self.sim.object_positions[codigo][0] = x
        self.sim.object_positions[codigo][1] = y
        self.sim.object_positions[codigo][2] = self.altura_mesa

        # cierra la pinza (make child)
        self.sim.close_grip(self.sim.object_positions.get(codigo)[3])

        time.sleep(3)

        #  mueve a la posicion de "zona de trabajo"
        self.sim.setPose(const.ZONA_DE_TRABAJO)

        #  mueve a la posicion de "recogida/entraga"
        self.sim.setPose(const.ZONA_DE_ENTREGA_RECOGIDA)


