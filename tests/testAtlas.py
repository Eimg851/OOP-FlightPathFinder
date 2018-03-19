'''
Created on 18 Mar 2018

@author: Eimg
'''
from path_finder import airport
from path_finder import airportAtlas
from path_finder.airportAtlas import *


def main():
    #assign the csv file to variable named 'file'
    file = "/Users/Eimg/eclipse-Data_Structures_And_Algorithms/flight_path_finder/input/airport.csv"
    #pass the file variable to the AirportAtlas class to instantiate the dictionary.
    #returned value is assigned to the variable name 'atlas'
    atlasOfAirports = airportAtlas.AirportAtlas(file)
    #Assign value to the variable 'code'
    code = "DUB"
    #Pass the code variable to the .getAirport method to access the dictionary
    atlasOfAirports.getAirport(code)
    print(AirportAtlas.greatCircleDist(53.421333, -6.270075, 51.4775, -0.461389))
    code1 = "DUB"
    code2 = "LHR"
    print(atlasOfAirports.getDistanceBetweenAirports(code1, code2))
    
    
    
if __name__ == '__main__':
    main()