import sys
from constants import colors

# sobreescribir la funcion print para darle colores
def echo(string, color=colors.OKBLUE):
    print(color + string + colors.ENDC)

def fatalError(string):
    print(colors.FAIL + "ERROR: " + str(string) + colors.ENDC)
    sys.exit(0)