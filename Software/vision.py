# class para manegar el la camara y la deteccion de los objetos

import time
import numpy as np

import coppelia.sim as sim
import coppelia.simConst as simConst
from utils import fatalError

class vision(object):
    sim = None
    
    def __init__(self, simulator_instance):
        self.sim = simulator_instance
        
    def take_image(self):
        pass
        
    def get_coords(self, codigo):
        iamge = self.take_image()
        pass