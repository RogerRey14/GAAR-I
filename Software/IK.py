import math

# Classe para la cinematica inversa
class servoPosition(object):

    def __init__(self, poslist, ptype="deg"):

        if len(poslist) < 5:
            # mostrar error
            pass

        self.posicion = poslist.copy()
        self.ptype = ptype

    def update(self, poslist, ptype="deg"):
        # Función para crear una posición para cada motor del robot

        if len(poslist) < 5:
            # mostrar error
            pass

        self.ptype = ptype
        self.posicion = posicion.copy()

    def get(self, ptype="deg"):
        # Función para obtener una posición en deg/rad
        if self.ptype == ptype:
            return self.posicion
        else:
            if ptype == "deg":
                return [ pos * (180 / math.pi) for pos in self.posicion ]
            if ptype == "rad":
                return [ pos * (math.pi / 180) for pos in self.posicion ]




# Inverse Kinematics class.
# params:
#  - cartesian_coordinates = [x, y, z]
def inverseKinematic(cartesian_coordinates):

    coords = cartesian_coordinates.copy()

    # ... procesar

    # devolver la posicion en angulos o radianes
    angulos = servoPosition([90, 180, 90, 180, 90], "deg")
    return angles
