# class para conectar con el simulador

import time
import coppelia.sim as sim
import coppelia.simConst as simConst
import sympy as sp
from utils import fatalError

class simulator:

    clientID = None
    servos = list()
    pinza = list()
    dummy = None

    def __init__(self):
        self.clientID = self.connect(19999)
        for i in range(5):
            retCode, joint = sim.simxGetObjectHandle(self.clientID, f"joint{i+1}", simConst.simx_opmode_blocking)
            self.servos.append(joint)
            if retCode == -1:
                fatalError(f"no se pudo obtener la instancia del joint {i+1}")

        retCode, self.dummy = sim.simxGetObjectHandle(self.clientID, "Dummy", simConst.simx_opmode_blocking)

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


    def getCameraImage(self):
        pass