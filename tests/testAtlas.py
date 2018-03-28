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
    print(atlasOfAirports.getAirport(code))
    
    #Checking if greatCircleDist method works
    print(AirportAtlas.greatCircleDist(40.639751, -73.778925,53.421333, -6.270075))
    code1 = "DUB"
    code2 = "AAL"
    
    #Checking if getDistanceBetweenAirports method works
    print('Distance between, ',code1,' and ', code2,' is ',atlasOfAirports.getDistanceBetweenAirports(code1, code2))
    
    #Checking to see if findAirportbyName method works
    name = 'Dublin'
    print(atlasOfAirports.findAirportbyName(name))
    
    #Check cvsFile error handler
    file = "this/is/not/a/file"
    atlasOfAirports = airportAtlas.AirportAtlas(file)
    #Check  code error handler
    code = "dub"
    print(atlasOfAirports.getAirport(code))
    #Check getAirportbyName error handler
    name = 'bananas'
    print(atlasOfAirports.findAirportbyName(name))
    
if __name__ == '__main__':
    main()