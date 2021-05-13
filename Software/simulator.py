# class para conectar con el simulador

import time
import coppelia.sim as sim
import coppelia.simConst as simConst
import sympy as sp
from utils import fatalError

import numpy as np
import sympy as sp
import math
import sim
import time
import cv2
import matplotlib.pyplot as plt
from sympy import *

class simulator:

    clientID = None
    servos = list()
    pinza = None
    dummy = None

    robotIq = None
    grip = None

    Cuboid3 = None
    Cuboid6 = None
    Cuboid5 = None
    Cuboid4 = None
    cuboid0 = None
    cuboid = None

    camara = None

    tijeras = None
    bisturi = None
    jeringuilla = None
    pinza = None

    def __init__(self):
        self.clientID = self.connect(19999)
        for i in range(5):
            retCode, joint = sim.simxGetObjectHandle(self.clientID, f"joint{i+1}", simConst.simx_opmode_blocking)
            self.servos.append(joint)
            if retCode == -1:
                fatalError(f"no se pudo obtener la instancia del joint {i+1}")

        retCode, self.dummy = sim.simxGetObjectHandle(self.clientID, "Dummy", simConst.simx_opmode_blocking)

        [retCode, Robotiq] = sim.simxGetObjectHandle(self.clientID, 'ROBOTIQ_85_attachPoint', sim.simx_opmode_blocking)
        self.robotIq = Robotiq

        retCode, self.grip = sim.simxGetObjectHandle(self.clientID, 'ROBOTIQ_85', sim.simx_opmode_blocking)

        [retCode, self.tijeras] = sim.simxGetObjectHandle(self.clientID, 'Cuboid3', sim.simx_opmode_blocking)
        [retCode, self.bisturi] = sim.simxGetObjectHandle(self.clientID, 'Cuboid6', sim.simx_opmode_blocking)
        [retCode, self.jeringuilla] = sim.simxGetObjectHandle(self.clientID, 'Cuboid5', sim.simx_opmode_blocking)
        [retCode, self.pinza] = sim.simxGetObjectHandle(self.clientID, 'Cuboid4', sim.simx_opmode_blocking)

        retCode, self.camara = sim.simxGetObjectHandle(self.clientID,'Vision_sensor',sim.simx_opmode_blocking)
        retCode, self.cuboid0 = sim.simxGetObjectHandle(self.clientID, 'Cuboid0', sim.simx_opmode_blocking)
        retCode, self.cuboid = sim.simxGetObjectHandle(self.clientID,'Cuboid',sim.simx_opmode_blocking)


        print("Simulator incializado")

    # Conexion al soppelia sim
    def connect(self, port):
        sim.simxFinish(-1)
        clientID = sim.simxStart('127.0.0.1', port, True, True, 2000, 5)
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
    def setPose(self, angles):
        if len(angles) > len(self.servos):
            fatalError("numero de angulos no coinciden con el numero de servos")

        for i in range(len(self.servos)):
            returnCode = sim.simxSetJointTargetPosition(self.clientID, self.servos[i], angles[i], simConst.simx_opmode_blocking)
            time.sleep(0.1) # 100ms

        return returnCode != -1


    def gripper(self, status):
        res = sim.simxCallScriptFunction(self.clientID, "ROBOTIQ_85", sim.sim_scripttype_childscript, "gripper", [status], [], [], "", sim.simx_opmode_blocking)
        return res

    def open_grip(self,object_handler):
        res = sim.simxSetObjectParent(self.clientID, object_handler, -1, False, sim.simx_opmode_blocking)
        self.gripper(0)

    def close_grip(self, object_handler):
        self.gripper(1)
        time.sleep(0.1)
        res = sim.simxSetObjectParent(self.clientID, object_handler, self.robotIq, True, sim.simx_opmode_blocking)

    def init_pos(self):
        self.gripper(0)

        angulos = [-np.pi/8, np.pi/8, np.pi/8, 3*np.pi/4, -np.pi/8]

        for i, joint in enumerate(self.servos):
            sim.simxSetJointTargetPosition(self.clientID, joint, angulos[i], sim.simx_opmode_blocking)

    def finish_pos(self):
        angulos = [-np.pi, np.pi/2, 0, 0, 0]
        for i, joint in enumerate(self.servos):
            sim.simxSetJointTargetPosition(self.clientID, joint, angulos[i], sim.simx_opmode_blocking)
            if i == 0:
                time.sleep(0.4)

    def start_pos(self):
        for joint in self.servos:
            sim.simxSetJointTargetPosition(self.clientID, joint, 0, sim.simx_opmode_blocking)
