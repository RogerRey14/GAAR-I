import servoPosition
import numpy as np
import math
from sympy import *

class IK(object):

    def __init__(self):
        pass

    def inverse_kinematics(self, x, y, z, cabGrados=90, Axis5=0):
        #Medidas
        l1 = 0.955
        l2 = 0.3
        l3 = 0.3
        l4 = 0.26
        dTotal = 0.0757
        m = l4
        H = l1
        b = l2
        ab = l3

        y -= 0.225
        cabRAD=cabGrados*np.pi/180
        Axis1=math.atan2(y, x)
        M=math.sqrt(pow(x,2)+pow(y,2))
        xprima=M
        yprima=z

        Afx=math.cos(cabRAD)*m
        B=xprima-Afx
        Afy=math.sin(cabRAD)*m
        A=yprima+Afy-H
        Hip=math.sqrt(pow(A,2)+pow(B,2))
        alfa=math.atan2(A,B)
        beta=math.acos((pow(b,2)-pow(ab,2)+pow(Hip,2))/(2*b*Hip))
        Axis2=alfa+beta
        gamma=math.acos((pow(b,2)+pow(ab,2)-pow(Hip,2))/(2*b*ab))
        Axis3=gamma
        Axis4=2*np.pi-cabRAD-Axis2-Axis3

        j0=Axis1*180/np.pi #joint0
        j1=90-Axis2*180/np.pi #joint1
        j2=180-Axis3*180/np.pi #joint2
        j3=180-Axis4*180/np.pi #joint3
        j4=Axis5 + j0 #joint5 Se ha dado en grados inicialmente

        # devuelve angulo en grados
        return [j0, j1, j2, j3, j4]