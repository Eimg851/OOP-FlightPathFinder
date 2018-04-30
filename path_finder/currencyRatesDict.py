'''
Created on 19 Mar 2018

@author: Eimg
'''
from path_finder.currencyRatesClass import *
import csv
from path_finder.currencyClass import Currency

class CurrencyRates:
    """
    Holds information on all currencies and their conversion rates to and from Euro and allow us to look up in a variety of ways
    """
    def __init__(self, csvFile):
        #Create the dictionary
        self.conversionDict = {}
        self.loadData(csvFile)
 
    def loadData(self, csvFile):
        """
        Reads data from a csv file line by line and creates a dictionary to store airport instances
        """
        try:
            with open(csvFile) as csvFile:
                reader = csv.reader(csvFile)
                print('Creating Currency Rates Instances')
                for row in reader:
                    #pass each line in csv file to the airport constructor to create an Airport instance
                    createClass = CurrencyConverter(row)
                    #Add the airport instance to the Dictionary using the IATA code as the key
                    self.conversionDict[createClass.Code]= createClass
        except IOError:
            print("Could not read file:", csvFile)
        print('Conversion Rates Look Up containing ', len(self.conversionDict), 'rates created.')
        print('\n*************************************************************************************')
        return self