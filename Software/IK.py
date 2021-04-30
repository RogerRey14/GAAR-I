import servoPosition

# Inverse Kinematics class.
# params:
#  - cartesian_coordinates = [x, y, z]
def inverseKinematic(cartesian_coordinates):

    coords = cartesian_coordinates.copy()

    # ... procesar

    # devolver la posicion en angulos o radianes
    angulos = servoPosition([90, 180, 90, 180, 90], "deg")
    return angles
