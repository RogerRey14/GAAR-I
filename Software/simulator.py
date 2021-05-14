# class para conectar con el simulador

import time
import numpy as np
import sympy as sp

from sympy import *
import coppelia.sim as sim
import coppelia.simConst as simConst
import sympy as sp
from utils import fatalError
from constants import const

class simulator:

    ipAddr = "192.168.2.3"
    port = 19999
    clientID = None
    servos = list()
    pinza = None
    dummy = None

    robotIq = None
    grip = None

    current_object = None
    pinza = None
    tijeras = None
    bisturi = None
    jeringuilla = None

    cuboid0 = None
    cuboid = None
    camara = None

    def __init__(self):
        self.clientID = self.connect(self.port)
        for i in range(5):
            retCode, joint = sim.simxGetObjectHandle(self.clientID, f"Joint_{i}", simConst.simx_opmode_blocking)
            self.servos.append(joint)
            if retCode == -1:
                fatalError(f"no se pudo obtener la instancia del joint {i+1}")

        # Obtener los handlers para posteriormente manipular el robot
        retCode, self.dummy = sim.simxGetObjectHandle(self.clientID, "Dummy", simConst.simx_opmode_blocking)

        [retCode, self.robotIq] = sim.simxGetObjectHandle(self.clientID, 'ROBOTIQ_85_attachPoint', simConst.simx_opmode_blocking)
        retCode, self.grip = sim.simxGetObjectHandle(self.clientID, 'ROBOTIQ_85', simConst.simx_opmode_blocking)

        [retCode, self.tijeras] = sim.simxGetObjectHandle(self.clientID, 'Cuboid3', simConst.simx_opmode_blocking)
        [retCode, self.bisturi] = sim.simxGetObjectHandle(self.clientID, 'Cuboid6', simConst.simx_opmode_blocking)
        [retCode, self.jeringuilla] = sim.simxGetObjectHandle(self.clientID, 'Cuboid5', simConst.simx_opmode_blocking)
        [retCode, self.pinza] = sim.simxGetObjectHandle(self.clientID, 'Cuboid4', simConst.simx_opmode_blocking)

        retCode, self.camara = sim.simxGetObjectHandle(self.clientID,'Vision_sensor',simConst.simx_opmode_blocking)
        retCode, self.cuboid0 = sim.simxGetObjectHandle(self.clientID, 'Cuboid0', simConst.simx_opmode_blocking)
        retCode, self.cuboid = sim.simxGetObjectHandle(self.clientID,'Cuboid',simConst.simx_opmode_blocking)


        print("Simulator incializado")

    # Conexion al soppelia sim
    def connect(self, port):
        sim.simxFinish(-1)
        clientID = sim.simxStart(self.ipAddr, port, True, True, 2000, 5)
        if clientID == 0:
            print("conectado a", port)
        else:
            pass
            # fatalError("no se pudo conectar al simulador!")
        return clientID

    # Obtener la posición del Dummy
    def getDummyPosition(self):
        returnCode, pos = sim.simxGetObjectPosition(self.clientID, self.dummy, -1, simConst.simx_opmode_blocking)
        return pos

    # Obtener el angulo de un servo en concreto
    def getServoPosition(self, index):
        returnCode, pos = sim.simxGetObjectPosition(self.clientID, self.servos[index], -1, simConst.simx_opmode_blocking)
        return pos

    # Fijar una anglo a un servo especifo
    def setServoPosition(self, angle, index):
        returnCode = sim.simxSetJointTargetPosition(self.clientID, self.servos[index], angle, simConst.simx_opmode_oneshot)
        return returnCode != -1

    # Fijar una lista de angulos al robot entero
    def setPose(self, angles, sleep = False):
        if len(angles) > len(self.servos):
            fatalError("numero de angulos no coinciden con el numero de servos")

        for i in range(len(self.servos)):
            returnCode = sim.simxSetJointTargetPosition(self.clientID, self.servos[i], angles[i], simConst.simx_opmode_blocking)
            if sleep != False:
                time.sleep(sleep) # 100ms

        return returnCode != -1


    def gripper(self, status):
        res = sim.simxCallScriptFunction(self.clientID, "ROBOTIQ_85", simConst.sim_scripttype_childscript, "gripper", [status], [], [], "", simConst.simx_opmode_blocking)
        return res

    def open_grip(self, object_handler):
        res = sim.simxSetObjectParent(self.clientID, object_handler, -1, False, simConst.simx_opmode_blocking)
        self.gripper(0)

    def close_grip(self, object_handler):
        self.current_object = object_handler
        self.gripper(1)
        time.sleep(0.1)
        res = sim.simxSetObjectParent(self.clientID, object_handler, self.robotIq, True, simConst.simx_opmode_blocking)

    def resting_position(self):
        self.gripper(0)
        self.setPose(const.ZONA_DE_TRABAJO)

