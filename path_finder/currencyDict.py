'''
Created on 19 Mar 2018

@author: Eimg
'''
import csv
from path_finder.currencyClass import *
from errorHandler import isValidCode

class Currency:
    """
    Holds information on all currencies and allow us to look up in a variety of ways
    """
    def __init__(self, csvFile):
        #Create the dictionary
        self.currencyDict = {}
        #calling loadData method
        self.loadData(csvFile)
 
    def loadData(self, csvFile):
        #open the csv file and read line by line
        try:
            with open(csvFile) as csvFile:
                reader = csv.reader(csvFile)
                for row in reader:
                    #pass each line in csv file to the airport constructor to create an Airport instance
                    createClass = currency(row)
                    #Add the airport instance to the Dictionary using the IATA code as the key
                    self.currencyDict[createClass.Country]= createClass
                #Checking if dictionary is storing the objects
                #print(self.airportDict["DUB"])
        except IOError:
            print("Could not read file:", csvFile)
        return self
    
    def getCurrency(self, code):
        """
        Returns airport objects stored in a Dictionary
        """
        if isValidCode(code) == True:
            #access the dictionary using the code as a key
            return(self.airportDict[code].Currency)
        else:
            return("You have not entered a valid code.")