'''
Created on 18 Mar 2018

@author: Eimg

'''
from airport import *
import csv
import math
from computeDistance import *
from matplotlib.mlab import dist

class AirportAtlas:
    """
    Holds information on all of the airports and allows us to look up airports in a variety of ways.
    """
    def __init__(self, csvFile):
        #Create the dictionary
        self.airportDict = {}
        #calling loadData method
        self.loadData(csvFile)
 
    def loadData(self, csvFile):
        #Create the dictionary
        #airportDict = {}
        #open the csv file and read line by line
        with open(csvFile) as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                #pass each line in csv file to the airport constructor to create an Airport instance
                createClass = airport(row)
                #Add the airport instance to the Dictionary using the IATA code as the key
                self.airportDict[createClass.Code]= createClass
            #Checking if dictionary is storing the objects
            #print(self.airportDict["DUB"])
            return self
        
    def getAirport(self, code):
        
        #print(self.airportDict[code])
        #airport = self.dictionary.get(code)
        #print(airport)
        return(self.airportDict[code])
    
    @staticmethod
    def greatCircleDist(lat1, long1, lat2, long2):
        #Find difference in long1 and long 2
        long = long1 - long2
        
        #get value of angles for lat and long values
        angle1 = getAngles(lat1)
        angle2 = getAngles(lat2)
        
        #Convert angles to radians
        lat1Radians = getRadians(angle1)
        lat2Radians = getRadians(angle2)
        lateralDist = getRadians(long)
        
        #Assign value to earthRadians
        earthRadians = 6371

        #Comput first part of formula
        part1 = sin(lat1Radians)*sin(lat2Radians)*cos(lateralDist)
        #Compute second part of formula
        part2 = cos(lat1Radians)*cos(lat2Radians)
        #Add first two parts of formular
        part3 = (part1 + part2)
        #getting arc cosine of formula before converting to km
        part4 = math.acos(part3)
        #get the distance in km
        distance = part4*earthRadians
        return int(distance)
    
    def getDistanceBetweenAirports(self,code1, code2):
        lat1 = float(self.airportDict[code1].lat)
        long1 = float(self.airportDict[code1].long)
        lat2 = float(self.airportDict[code2].lat)
        long2 = float(self.airportDict[code2].long)
        return (AirportAtlas.greatCircleDist(lat1, long1, lat2, long2))        
        