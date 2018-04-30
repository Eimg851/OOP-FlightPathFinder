'''
Created on 19 Mar 2018

@author: Eimg
'''
import csv
from path_finder.currencyClass import *
from path_finder.errorHandler import isValidCode

class CurrencyDict:
    """
    Holds information on all currencies and allow us to look up in a variety of ways
    """
    def __init__(self, csvFile):
        #Create the dictionary
        self.currencyDict = {}
        self.loadData(csvFile)
        
 
    def loadData(self, csvFile):
        """
        Reads data from a csv file line by line and creates a dictionary to store currency instances
        """
        try:
            with open(csvFile) as csvFile:
                reader = csv.reader(csvFile)
                print('\n*************************************************************************************\n')
                print('Creating Currency Instances')
                for row in reader:
                    if row[0] != 'name':
                        #pass each line in csv file to the airport constructor to create an Airport instance
                        createClass = Currency(row)
                        #Check to see if the currency code is valid
                        if isValidCode(createClass.Currency):
                            #Add the currency instance to the Dictionary using the currency code as the key
                            self.currencyDict[createClass.Country]= createClass
                        else:
                            #If code not valid, print error message to console.
                            print('ERROR! Could not add',createClass.Country,'to Currency Look Up as no Currency provided.')
        except IOError:
            print("Could not read file:", csvFile)
        #Log to console how many instance were created
        print('Currency Look Up containing ', len(self.currencyDict), 'countries created.')
        print('\n*************************************************************************************')
        return self
    
    def getCurrency(self, code):
        """
        Returns airport objects stored in a Dictionary
        """
        return(self.currencyDict[code].Currency)