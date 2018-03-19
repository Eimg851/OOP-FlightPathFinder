'''
Created on 18 Mar 2018

@author: Eimg

'''
from airport import *
import csv

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
        print('hello')