'''
Created on 11 Apr 2018

@author: Eimg
'''
from path_finder.aircraft import Aircraft
import csv

class aircrafts:
    """
    Holds information on all currencies and their conversion rates to and from Euro and allow us to look up in a variety of ways
    """
    def __init__(self, csvFile):
        #Create the dictionary
        self.aircraftDictionary = {}
        self.loadData(csvFile)
 
    def loadData(self, csvFile):
        """
        Reads data from a csv file line by line and creates a dictionary to store aircraft instances
        """
        try:
            with open(csvFile) as csvFile:
                reader = csv.reader(csvFile)
                print('Creating Aircraft Instances')
                for row in reader:
                    if row[0] != 'code':
                        #pass each line in csv file to the aircraft constructor
                        createClass = Aircraft(row)
                        #Add the airrraft instance to the Dictionary using the aircraft code as the key
                        self.aircraftDictionary[createClass.code]= createClass
        except IOError:
            print("Could not read file:", csvFile)
        print('Aircraft Look Up containing ', len(self.aircraftDictionary), 'aircrafts created.')
        print('\n*************************************************************************************')
        return self
    
    def getAircraft(self, code):
        """
        Returns airport objects stored in a Dictionary
        """
        return(self.aircraftDictionary[code])