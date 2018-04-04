'''
Created on 19 Mar 2018

@author: Eimg
'''
import math

def getRadians(angle):
    """
    converts angles from degrees to radians
    """
    multiplier = (2*math.pi) /360
    Radians = angle * multiplier
    return Radians
