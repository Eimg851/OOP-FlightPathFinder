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

def getAngles(degrees):
    """
    Getting values for angles which are positive or negative degrees from equator/meridian
    """
    if degrees > 0:
        angle = 90 - degrees
    else:
        angle = 90 + degrees
    return angle

def cos(angle):
    return math.cos(angle)
    
def sin(angle):
    return math.sin(angle)


