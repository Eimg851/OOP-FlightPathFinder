'''
Created on 18 Mar 2018

@author: Eimg

'''
from airport import *
from errorHandler import isValidCode
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
        try:
            with open(csvFile) as csvFile:
                reader = csv.reader(csvFile)
                for row in reader:
                    #pass each line in csv file to the airport constructor to create an Airport instance
                    createClass = airport(row)
                    #Add the airport instance to the Dictionary using the IATA code as the key
                    self.airportDict[createClass.Code]= createClass
                #Checking if dictionary is storing the objects
                #print(self.airportDict["DUB"])
        except IOError:
            print("Could not read file:", csvFile)
        return self
        
    def getAirport(self, code):
        """
        Returns airport objects stored in a Dictionary
        """
        if isValidCode(code) == True:
            #access the dictionary using the code as a key
            return(self.airportDict[code])
        else:
            return("You have not entered a valid code.")
        
    @staticmethod
    def greatCircleDist(lat1, long1, lat2, long2):
        """
        Finds the distance between two airports using their geographical co-ordinates
        """
        #Convert angles to radians
        lat1Radians = getRadians(lat1)
        lat2Radians = getRadians(lat2)
        long1Radians = getRadians(long1)
        long2Radians = getRadians(long2)
        longDis = long2Radians - long1Radians
   
        #Assign value to earthRadians
        earthRadians = 6371

        #Compute first part of formula
        part1 = sin(lat1Radians)*sin(lat2Radians)
        #Compute second part of formula
        part2 = cos(lat1Radians)*cos(lat2Radians)*cos(longDis)
        #Add first two parts of formula
        part3 = (part1 + part2)
        #getting arc cosine of formula before converting to km
        part4 = math.acos(part3)
        #get the distance in km
        distance = part4*earthRadians
        return int(distance)
    
    def getDistanceBetweenAirports(self,code1, code2):
        """
        Takes the IATA code of two airports and computes the distance between the two
        """
        #Access the class objects stored in the dictionary and store their attributes in variables
        #Use float to convert from a string - to allow for computations
        lat1 = float(self.airportDict[code1].lat)
        long1 = float(self.airportDict[code1].long)
        lat2 = float(self.airportDict[code2].lat)
        long2 = float(self.airportDict[code2].long)
        #Pass the variables to the getCirleDist method to find the distance between two airports
        return (AirportAtlas.greatCircleDist(lat1, long1, lat2, long2))   
    
    def findAirportbyName(self, name):
        #for loop iterates over the dictionary
        for key in self.airportDict:
            #Check to see if the name of each object matches the name to look up
            if self.airportDict[key].Name == name:
                #if found return that object
                return self.airportDict[key]
        #error handling if airport is not found
        return('Airport not found')
        