import servoPosition
import numpy as np
import math
from sympy import *
from constants import const


class IK(object):

    def __init__(self):
        #Medidas
        self.m = const.L4
        self.H = const.L1
        self.b = const.L2
        self.ab = const.L3

    def inverse_kinematics(self, x, y, z, cabGrados=90, Axis5=0):
        y -= 0.225
        cabRAD=cabGrados*np.pi/180
        Axis1=math.atan2(y, x)
        M=math.sqrt(pow(x,2)+pow(y,2))
        xprima=M
        yprima=z

        Afx=math.cos(cabRAD)*self.m
        B=xprima-Afx
        Afy=math.sin(cabRAD)*self.m
        A=yprima+Afy-self.H
        Hip=math.sqrt(pow(A,2)+pow(B,2))
        alfa=math.atan2(A,B)
        beta=math.acos((pow(self.b,2)-pow(self.b,2)+pow(Hip,2))/(2*self.b*Hip))
        Axis2=alfa+beta
        gamma=math.acos((pow(self.b,2)+pow(self.b,2)-pow(Hip,2))/(2*self.b*self.b))
        Axis3=gamma
        Axis4=2*np.pi-cabRAD-Axis2-Axis3

        j0=Axis1*180/np.pi #joint0
        j1=90-Axis2*180/np.pi #joint1
        j2=180-Axis3*180/np.pi #joint2
        j3=180-Axis4*180/np.pi #joint3
        j4=Axis5 + j0 #joint5 Se ha dado en grados inicialmente

        # devuelve angulo en grados
        return j0, j1, j2, j3, j4

