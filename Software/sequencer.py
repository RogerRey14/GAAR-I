import time

from constants import const
from IK import IK
from servoPosition import servoPosition
from vision_net import vision_net####
import coppelia.sim as sim
import coppelia.simConst as simConst
import numpy as np
import math
import time
import argparse
import os
import numpy as np
import json
import cv2
import copy
import imgaug as ia
from imgaug import augmenters as iaa
from keras.utils import Sequence
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from skimage import morphology
from skimage.color import rgb2gray
from skimage import measure
from keras.models import Model
import tensorflow as tf
from keras.layers import Reshape, Activation, Conv2D, Input, MaxPooling2D, BatchNormalization, Flatten, Dense, Lambda
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.merge import concatenate
from keras.optimizers import SGD, Adam, RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
import matplotlib.pyplot as plt

invK = IK()
#vision = vision_net()


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
    vision = None
    altura_mesa = 0.71
    position_plataforma = 0

    def __init__(self, simInstance, vision):
        self.sim = simInstance
        self.vision = vision

    def ven(self):
        angulos = invK.inverse_kinematics(-0.3642, 0.5892, 0.84)
        self.sim.setPose(servoPosition(angulos).get("rad"))
        time.sleep(0.5)
        angulos = invK.inverse_kinematics(-0.3642, 0.5892, 0.82)
        self.sim.setPose(servoPosition(angulos).get("rad"))
        '''self.sim.setPose(const.PRE_ZONA_DE_ENTREGA_RECOGIDA)
        time.sleep(0.5)
        self.sim.setPose(const.ZONA_DE_ENTREGA_RECOGIDA)'''

    # reqiuere pruebas addicionales
    def abre(self):
        if self.sim.current_object != None:
            self.sim.open_grip(self.sim.current_object)
        else:
            self.sim.gripper(0)
            
        time.sleep(2)
        angulos = invK.inverse_kinematics(-0.3642, 0.5892, 0.84)
        self.sim.setPose(servoPosition(angulos).get("rad"))
        time.sleep(1)
        self.sim.setPose(const.ZONA_DE_TRABAJO)

    def abre_devuelve(self):
        if self.sim.current_object != None:
            self.sim.open_grip(self.sim.current_object)
        else:
            self.sim.gripper(0)
        #time.sleep(3)
        #self.sim.setPose(const.POST_ZONA_DE_ENTREGA_RECOGIDA)
        
        time.sleep(3)
        
        [x, y, z] = self.sim.getDummyPosition()
        angulos = invK.inverse_kinematics(x, y, z + 0.075)
        self.sim.setPose(servoPosition(angulos).get("rad"))
        
        time.sleep(1)
        self.sim.setPose(const.ZONA_DE_TRABAJO)

    def agarra(self, codigo):
        if codigo != None:
            self.sim.close_grip(self.sim.get_object_instance(codigo))
        else:
            self.sim.gripper(1)

    def devuelve(self, codigo):
        
        self.agarra(codigo)

        #otra entrada de audio "gary devuelve <objeto>" MODIFICAR FICHERO AUDIO
        #partimos posicion zona de entrega con pinza cerrada
        time.sleep(1.5)
        self.sim.setPose(const.POST_ZONA_DE_ENTREGA_RECOGIDA)
        time.sleep(1)
        self.sim.setPose(const.ZONA_DE_TRABAJO)

        x = self.sim.object_positions[codigo][0]
        y = self.sim.object_positions[codigo][1]
        z = self.sim.object_positions[codigo][2]
        orient = self.sim.object_positions[codigo][4]

        angulos3 = invK.inverse_kinematics(x, y, z, Axis5=orient)
        self.sim.setPose(servoPosition(angulos3).get("rad"))

        self.abre_devuelve()



    def objeto(self, codigo):
        self.sim.setPose(const.ZONA_DE_TRABAJO)

        # Obtener posiciones de los objetos 

        if codigo == 20: #bisturi  
            label = 'bisturi'
        elif codigo == 21: #tijeras
            label = 'tijera'
        elif codigo == 22: #jeringuilla
            label = 'jeringuilla'
        elif codigo == 23: #pinza
            label = 'pinza'

        
        # Obtener las coordenadas y el grado de giro
        pixel, orientation = self.vision.get_coords(self.sim.camara, label, self.sim.clientID)
  

        # normalizar las coordenadas para el simulador
        x, y = self.vision.transform_xy(pixel[1], pixel[0])

        # usar otra variable para grados
        angulos1 = invK.inverse_kinematics(x, y, self.altura_mesa + 0.075, Axis5=orientation)

        
        self.sim.setPose(servoPosition(angulos1).get("rad"))
        

        angulos2 = invK.inverse_kinematics(x, y, self.altura_mesa, Axis5=orientation)
        self.sim.setPose(servoPosition(angulos2).get("rad"))

        # guardar la pocicion del objeto a recoger
        self.sim.object_positions[codigo][0] = x
        self.sim.object_positions[codigo][1] = y
        self.sim.object_positions[codigo][2] = self.altura_mesa
        self.sim.object_positions[codigo][4] = orientation

        # cierra la pinza (make child)
        self.sim.close_grip(self.sim.object_positions.get(codigo)[3])

        time.sleep(3)

        #  mueve a la posicion de "zona de trabajo"
        self.sim.setPose(const.ZONA_DE_TRABAJO)

        #  mueve a la posicion de "recogida/entraga"
        angulos = invK.inverse_kinematics(-0.3642, 0.5892, 0.8293)
        self.sim.setPose(servoPosition(angulos).get("rad"))
        time.sleep(0.5)
        #angulos = invK.inverse_kinematics(-0.3642, 0.5892, 0.82)
        #self.sim.setPose(servoPosition(angulos).get("rad"))

