# class para manegar el la camara y la deteccion de los objetos

import time
import numpy as np

import coppelia.sim as sim
import coppelia.simConst as simConst
from utils import fatalError
from vision_net import vision_net####


class vision(object):
    sim = None
    
    def __init__(self, simulator_instance):
        self.sim = simulator_instance
    
    def transform_xy(self, x, y):
        x_return = ((((x-22.505)/(488.00-22.505)))*(0.6319997906684875-0.03499991074204445))+0.03499991074204445
        y_return = ((((y-37.500)/(446.07-37.500)))*(0.3389997184276581+0.1810000091791153))-0.1810000091791153
        return x_return, y_return
        
    def get_coords(self, camara_instance, object_name, clientID):
        vision_n = vision_net()
        pixel, orientation = vision_n.mainVision(camara_instance, object_name, clientID)
        return pixel, orientation