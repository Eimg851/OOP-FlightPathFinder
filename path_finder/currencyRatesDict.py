'''
Created on 19 Mar 2018

@author: Eimg
'''
from path_finder.currencyRatesClass import *
import csv

class CurrencyRates:
    """
    Holds information on all currencies and their conversion rates to and from Euro and allow us to look up in a variety of ways
    """
    def __init__(self, csvFile):
        #Create the dictionary
        self.conversionDict = {}
        #calling loadData method
        self.loadData(csvFile)
 
    def loadData(self, csvFile):
        #open the csv file and read line by line
        try:
            with open(csvFile) as csvFile:
                reader = csv.reader(csvFile)
                for row in reader:
                    #pass each line in csv file to the airport constructor to create an Airport instance
                    createClass = Rates(row)
                    #Add the airport instance to the Dictionary using the IATA code as the key
                    self.conversionDict[createClass.Code]= createClass
                #Checking if dictionary is storing the objects
                #print(self.airportDict["DUB"])
        except IOError:
            print("Could not read file:", csvFile)
        return self