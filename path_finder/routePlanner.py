'''
Created on 19 Mar 2018

@author: Eimg
'''
from airportAtlas import *
from currencyDict import *
from currencyRatesDict import *
from path_finder import airportAtlas



def singleLegCost(atlas, startAirport, EndAirport):
    #take code 1 and code 2
    start = atlas.getAirport(startAirport)
    #airportDict.getAirport(startAirport)
    #startCountry = AirportAtlas.getAirport(airportDict, startAirport)
    endCountry = AirportAtlas.getAirport(EndAirport)
    print(start)
    #find the corresponding country in the airport dict
    #find their currency using the currency dict
    #if currency is not euro find conversion rate
    #compute circle dist between two airports
    #multiply distance in km ( amount of fuel needed) by euro equivalent of currency
    # i.e if travelling 200 km from UK to France - multiply 200 by 1.4029
    # i.e. always multiply by the euro equiv to 1 unit of their currency
