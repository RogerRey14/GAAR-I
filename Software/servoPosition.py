import math
from constants import const, colors
from utils import fatalError

# Classe para la cinematica inversa
class servoPosition(object):

    def __init__(self, poslist, ptype="deg"):

        if len(poslist) != const.ROBOT_TOTAL_AXIS:
            fatalError("La lista de angulos debe tener almenos " + str(const.ROBOT_TOTAL_AXIS) + " ejes")

        self.posicion = poslist.copy()
        self.ptype = ptype
        self.currentIdx = 0

    def update(self, poslist, ptype="deg"):
        # Función para crear una posición para cada motor del robot

        if len(poslist) != const.ROBOT_TOTAL_AXIS:
            fatalError("La lista de angulos debe tener almenos " + str(const.ROBOT_TOTAL_AXIS) + " ejes")

        self.ptype = ptype
        self.posicion = posicion.copy()
        self.currentIdx = 0

    def __coversion__(self, ptype):
        # Función para obtener una posición en deg/rad
        if self.ptype == ptype:
            return self.posicion
        else:
            if ptype == "deg":
                return [ pos * (180 / math.pi) for pos in self.posicion ]
            if ptype == "rad":
                return [ pos * (math.pi / 180) for pos in self.posicion ]

    def get(self, ptype="deg"):
        return self.__coversion__(ptype)

    # esta funcion en cada llamada devuelve la siguiente pocision de la lista self.posicion
    def next(self, ptype="deg"):
        if self.currentIdx < len(self.posicion):
            angulo_actual = self.__coversion__(ptype)[self.currentIdx]
            self.currentIdx = self.currentIdx + 1
            return angulo_actual

    def reset(self):
        self.currentIdx = 0
