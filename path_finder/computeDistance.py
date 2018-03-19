'''
Created on 19 Mar 2018

@author: Eimg
'''
import math

def getRadians(angle):
    multiplier = (2*math.pi) /360
    Radians = angle * multiplier
    return Radians

def getAngles(degrees):
    if degrees > 0:
        angle = 90 - degrees
    else:
        angle = 90 + degrees
    return angle

def cos(angle):
    return math.cos(angle)
    
def sin(angle):
    return math.sin(angle)


