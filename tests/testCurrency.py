'''
Created on 19 Mar 2018

@author: Eimg
'''
from path_finder import currencyDict, routePlanner
from path_finder.routePlanner import *

def main():
    #assign the csv file to variable named 'file'
    file = "/Users/Eimg/eclipse-Data_Structures_And_Algorithms/flight_path_finder/input/countrycurrency.csv"
    #pass the file variable to the AirportAtlas class to instantiate the dictionary.
    #returned value is assigned to the variable name 'atlas'
    currency = currencyDict.Currency(file)
    print(currency.currencyDict["Australia"])
    
    code1 = 'Ireland'
    curr1 = currency.getCurrency(code1)
    code2 = 'Australia'
    curr2 = currency.getCurrency(code2)
    print(code1, ' uses: ',curr1)
    print(code2, ' uses: ',curr2)
    
if __name__ == '__main__':
    main()