'''
Created on 4 Apr 2018

@author: Eimg
'''
from path_finder import currencyDict
from path_finder import airportAtlas
from path_finder import currencyRatesDict

import sys
import csv
from path_finder.routePlanner import singleLegCost
from locale import currency
  

class Journey:
    def __init__(self, application):
        self.application = application
        
        
    def do_somehting(self):
        self.application.CurrencyLookUp.getCurrency("Australia")
        
          
class Application:
    """
    Application class: Application class creates the dictionaries and methods to plan journeys
    """
    def __init__(self, paths):
        self.CurrencyLookUp = currencyDict.CurrencyDict(paths['currency'])
        self.AirportLookUp = airportAtlas.AirportAtlas(paths['airports'])
        self.CoversionRates = currencyRatesDict.CurrencyRates(paths['conversion'])
    
    '''def run(self path_to_test): '''
        
    def run(self):
        #reading thet test csv
        code = ["DUB", "LHR", "JFK", "CDG", "DUB"]
        cost = self.multiLegCost(code)
        #computing journay
        #checking constraints
        #printing outputs.
        print(cost)
        J = Journey(self)
         
    def singleLegCost(self, startAirport, EndAirport):
        #take code 1 and code 2 find the corresponding country in the airport dict
        start = self.AirportLookUp.getAirport(startAirport)
        end = self.AirportLookUp.getAirport(EndAirport)
        #find their currency using the currency dict
        currency_of_start_country= self.CurrencyLookUp.getCurrency(start.Country)
        #if currency is not euro find conversion rate
        if currency_of_start_country != "EUR":
            cost_per_KM = float(self.CoversionRates.conversionDict[currency_of_start_country].toEuroRate)
        else:
            cost_per_KM = 1
        #compute circle dist between two airports
        print(cost_per_KM)
        distance = self.AirportLookUp.getDistanceBetweenAirports(startAirport, EndAirport)
        #multiply distance in km ( amount of fuel needed) by euro equivalent of currency
        cost = cost_per_KM * distance
        return cost
    
    def multiLegCost(self, list_of_airports=[]):
        cost = 0
        sum_of_all = 0
        for i in range(0, len(list_of_airports)-1):
            cost = self.singleLegCost(list_of_airports[i], list_of_airports[i+1])
            print("from",list_of_airports[i], "to",  list_of_airports[i+1], "costs: ", cost )
            sum_of_all += cost
        return sum_of_all
    
        
    '''
    class application(self, file1, file2, file3):
    def __init__(self, file1, file2, file3):
        Application.__init__(self, file1, file2, file3)  ''' 
    

    
if __name__ == '__main__':
    #path_to_test = sys.argv[1]
    paths = {
        'currency': '/Users/Eimg/eclipse-Data_Structures_And_Algorithms/flight_path_finder/input/countrycurrency.csv', 
        'airports': '/Users/Eimg/eclipse-Data_Structures_And_Algorithms/flight_path_finder/input/airport.csv', 
        'conversion': '/Users/Eimg/eclipse-Data_Structures_And_Algorithms/flight_path_finder/input/currencyrates.csv'
        }
    app = Application(paths)
    app.run()
    #app.run(path_to_test)