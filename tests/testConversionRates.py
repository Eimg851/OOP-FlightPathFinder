'''
Created on 19 Mar 2018

@author: Eimg
'''
from path_finder import currencyRatesDict

def main():
    #assign the csv file to variable named 'file'
    file = "/Users/Eimg/eclipse-Data_Structures_And_Algorithms/flight_path_finder/input/currencyrates.csv"
    #pass the file variable to the AirportAtlas class to instantiate the dictionary.
    #returned value is assigned to the variable name 'atlas'
    conversionRates = currencyRatesDict.CurrencyRates(file)
    print(conversionRates.conversionDict["GBP"].toEuroRate)
    
if __name__ == '__main__':
    main()