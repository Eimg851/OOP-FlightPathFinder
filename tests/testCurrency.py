'''
Created on 19 Mar 2018

@author: Eimg
'''
from path_finder import currencyDict

def main():
    #assign the csv file to variable named 'file'
    file = "/Users/Eimg/eclipse-Data_Structures_And_Algorithms/flight_path_finder/input/countrycurrency.csv"
    #pass the file variable to the AirportAtlas class to instantiate the dictionary.
    #returned value is assigned to the variable name 'atlas'
    currency = currencyDict.Currency(file)
    print(currency.currencyDict["Australia"])
    
if __name__ == '__main__':
    main()