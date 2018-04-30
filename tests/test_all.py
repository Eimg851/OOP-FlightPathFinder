'''
Created on 18 Mar 2018

@author: Eimg
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from path_finder import aircraftDict, currencyRatesDict, Set_ADT,\
    weightedDirectedGraph
from path_finder.currencyClass import Currency
from path_finder.airport import Airport
from path_finder.aircraft import Aircraft
from path_finder.currencyRatesClass import CurrencyConverter
from path_finder.undirected_weighted_graph import undirectedWeightedGraph
from path_finder.queue import Queue
from path_finder.errorHandler import isValidCode, trimWhitespace
sys.path.append('.')
import pytest
from path_finder.currencyDict import CurrencyDict
from path_finder.airportAtlas import AirportAtlas
from path_finder.currencyRatesDict import CurrencyRates
from path_finder.aircraftDict import aircrafts
from path_finder.main import Application
from Set_ADT import *
from weightedDirectedGraph import *
from queue import *
from undirected_weighted_graph import *

@pytest.fixture
class TestPathFinder(unittest.TestCase):
    def test_AtlasClass(self):
        paths = {
            'currency': '..//input/countrycurrency.csv', 
            'airports': '..//input/airport.csv', 
            'conversion': '..//input/currencyrates.csv',
            'aircraft':'..//input/aircraft.csv'
            }
        CurrencyLookUp = {}
        AirportLookUp = {}
        ConversionRates = {}
        AircraftLookUp = {}
        self.assertTrue(len(AircraftLookUp) == 0) 
        self.assertTrue(len(CurrencyLookUp) == 0)
        self.assertTrue(len(ConversionRates) == 0)
        self.assertTrue(len(AircraftLookUp) == 0)
        CurrencyLookUp = CurrencyDict(paths['currency'])
        AirportLookUp = AirportAtlas(paths['airports'])
        ConversionRates = CurrencyRates(paths['conversion'])
        AircraftLookUp = aircrafts(paths['aircraft'])
        assert len(AirportLookUp.airportDict) > 0
        assert len(CurrencyLookUp.currencyDict) > 0
        assert len(ConversionRates.conversionDict) > 0
        assert len(AircraftLookUp.aircraftDictionary) > 0
             
    def test_AirportInstance(self):
        paths = {
            'currency': '..//input/countrycurrency.csv', 
            'airports': '..//input/airport.csv', 
            'conversion': '..//input/currencyrates.csv',
            'aircraft':'..//input/aircraft.csv'
            }
        AirportLookUp = AirportAtlas(paths['airports'])
        #Assign value to the variable 'code'
        code = "DUB"
        #Pass the code variable to the .getAirport method to access the dictionary
        airportInstance = AirportLookUp.getAirport(code)
        self.assertIsInstance(airportInstance, Airport)
        print(airportInstance)
        self.assertTrue(airportInstance.Name == 'Dublin')
        latitude = 53.421333
        self.assertTrue(float(airportInstance.lat) == latitude)
        
        airportInstance2 = AirportLookUp.getAirport('SYD')
        self.assertIsInstance(airportInstance2, Airport)
        self.assertTrue(airportInstance2.Name == 'Sydney Intl')
        self.assertTrue(airportInstance2.Country == 'Australia')
        
        airportInstance3 = AirportLookUp.findAirportbyName('Heathrow')
        self.assertIsInstance(airportInstance3, Airport)
        self.assertTrue(airportInstance3.Code == 'LHR')
        self.assertTrue(airportInstance3.City =='London')
        
        airportInstance4 = AirportLookUp.getAirport('CDG')
        self.assertIsInstance(airportInstance4, Airport)
        self.assertTrue(float(airportInstance4.long) == 2.55)
        airportInstance5 = ""
        self.assertNotIsInstance(airportInstance5, Airport)
        
    def test_CurrencyInstance(self):
        paths = {
            'currency': '..//input/countrycurrency.csv', 
            'airports': '..//input/airport.csv', 
            'conversion': '..//input/currencyrates.csv',
            'aircraft':'..//input/aircraft.csv'
            }
        CurrencyLookUp = CurrencyDict(paths['airports'])
        
        code = "Ireland"
        currency = CurrencyLookUp.currencyDict.getCurrency(code)
        self.assertIsInstance(currency, Currency)
        self.assertEqual(currency.Currency, 'EUR')
        
        code2 = "Australia"
        currency2 = CurrencyLookUp.currencyDict. getCurrency(code2)
        self.assertIsInstance(currency2, Currency)
        self.assertIs(currency2.Currency, 'AUD')
        
        currency3 = ""
        self.assertNotIsInstance(currency3, Currency)
    
    def test_AircraftInstance(self):
        paths = {
            'currency': '..//input/countrycurrency.csv', 
            'airports': '..//input/airport.csv', 
            'conversion': '..//input/currencyrates.csv',
            'aircraft':'..//input/aircraft.csv'
            }
        AircraftLookUp = aircraftDict(paths['airports'])
        code = "777"
        jet = AircraftLookUp.aircraftDict.getAircraft(code)
        self.assertIsInstance(jet, Aircraft)
        self.assertEqual(jet.range, 9700)
        self.assertTrue(jet.manufacturer == 'Boeing')
        
        code2 = "A330"
        jet2 = AircraftLookUp.aircraftDict.getAircraft(code2)
        self.assertIsInstance(jet2, Aircraft)
        self.assertIs(jet2.manufacturer, 'Airbus')
        self.assertIs(jet2.range, 13430)
        self.assertFalse(jet2.range == 1500)
        
        jet3 = ""
        self.assertNotIsInstance(jet3, Aircraft)
        
    def test_ConversionRatesInstance(self):
        paths = {
            'currency': '..//input/countrycurrency.csv', 
            'airports': '..//input/airport.csv', 
            'conversion': '..//input/currencyrates.csv',
            'aircraft':'..//input/aircraft.csv'
            }
        ConversionRatesLookUp = currencyRatesDict(paths['airports'])
        
        code = "EUR"
        currency1 = ConversionRatesLookUp.currencyRatesDict.getCurrency(code)
        self.assertIsInstance(currency1, CurrencyConverter) 
        self.assertEqual(currency1.Name, 'Euro')
        self.assertTrue(currency1.toEuroRate == 1)
        self.assertTrue(currency1.fromEuroRate == 1)
        self.assertFalse(currency1.toEuroRate == 0)
        
        code2 = "NZD"
        currency2 = ConversionRatesLookUp.currencyRatesDict.getCurrency(code2)
        self.assertIsInstance(currency1, CurrencyConverter) 
        self.assertEqual(currency2.Name, 'New Zealand Dollar')
        self.assertTrue(currency2.toEuroRate == 0.6989)
        self.assertTrue(currency2.fromEuroRate == 1.4315)
        self.assertFalse(currency2.toEuroRate == 1)
        
        currency3 = ""
        self.assertNotIsInstance(currency3, CurrencyConverter) 
        
    def test_Distance(self):
        paths = {
            'currency': '..//input/countrycurrency.csv', 
            'airports': '..//input/airport.csv', 
            'conversion': '..//input/currencyrates.csv',
            'aircraft':'..//input/aircraft.csv'
            }
        AirportLookUp = AirportAtlas(paths['airports'])
        distance = AirportLookUp.greatCircleDist(40.639751, -73.778925,53.421333, -6.270075)
        self.assertTrue(distance == 5103)
        
        code1 = "DUB"
        code2 = "JFK"
        distance2 = AirportLookUp.getDistanceBetweenAirports(code1, code2)
        self.assertTrue(distance2 == 5103)
        
        code3 = "LHR"
        code4 = "LHR"
        distance3 = AirportLookUp.getDistanceBetweenAirports(code3, code4)
        self.assertTrue(distance3 == 0)
        
    def test_Cost(self):   
        paths = {
            'currency': '..//input/countrycurrency.csv', 
            'airports': '..//input/airport.csv', 
            'conversion': '..//input/currencyrates.csv',
            'aircraft':'..//input/aircraft.csv'
            }
        CurrencyLookUp = {}
        AirportLookUp = {}
        ConversionRates = {}
        AircraftLookUp = {}
        CurrencyLookUp = CurrencyDict(paths['currency'])
        AirportLookUp = AirportAtlas(paths['airports'])
        ConversionRates = CurrencyRates(paths['conversion'])
        AircraftLookUp = aircrafts(paths['aircraft'])
        #check if singleLegCostWorks
        code1 = "DUB"
        code2 = "LHR"
        cost = Application.singleLegCost(code1, code2)
        self.assertTrue(cost == 448)
        cost2 = Application.singleLegCost(code2, code1)
        #start = AirportLookUp.airportDict[code2]
        #currency_of_start_country= CurrencyLookUp.getCurrency(start.Country)
        #rate = ConversionRates.conversionDict[currency_of_start_country].toEuroRate
        #self.assertTrue(cost2 == 448*rate)
        self.assertTrue(cost2 == 628.4992)
        
    def test_ErrorHandling(self):    
        #Check cvsFile error handler
        file = "this/is/not/a/file"
        atlasOfAirports = AirportAtlas(file)
        #Check  code error handler
        code = "dub"
        print(atlasOfAirports.getAirport(code))
        #Check getAirportbyName error handler
        name = 'bananas'
        print(atlasOfAirports.findAirportbyName(name))
        Application.run('..//sampleinput.csv')
        
        code = 'DUB'
        code2='111'
        code3='T'
        self.assertTrue(isValidCode(code))
        self.assertFalse(isValidCode(code2))
        self.assertFalse(isValidCode(code3))
        
        code4 = 'S F O'
        self.assertFalse(isValidCode(code4))
        newcode = trimWhitespace(code4)
        self.assertEqual(newcode, 'SFO')
        self.assertTrue(isValidCode(newcode))
        
    def test_queue(self):
        Q = Queue()
        self.assertTrue(len(Q) == 0)
        
        Q.enqueue('a')
        Q.enqueue('b')
        Q.enqueue('c')
        
        self.assertEqual(len(Q), 3)
        
        self.assertEqual(Q.front(), 'a')
        gone = Q.dequeue()
        self.assertEqual(gone, 'a')
        
        self.assertTrue(len(Q)==2)
        self.assertEqual(Q.front(), 'b')
        Q.dequeue()
        Q.dequeue()
        self.assertTrue(len(Q) == 0)
    
    def test_set(self):
        a = Set_ADT.Set()
        a.add(24)
        self.assertTrue(a.size()==1)
        
        b = Set_ADT.Set()
        b.add(24)
        b.add("toto")
        self.assertTrue(b.size()==2)
        b.remove("titi")
        self.assertTrue(b.size()==2)
        b.remove("toto")
        self.assertTrue(b.size()==1)
        
        c = Set_ADT.Set()
        self.assertTrue(c.is_empty())
        c.add(24)
        self.assertFalse(c.is_empty())
        c.remove(24)
        self.assertTrue(c.is_empty())
        c.add(24)
        c.remove(23)
        self.assertFalse(c.is_empty())
        
    def test_directedGraph(self):
        g = weightedDirectedGraph.directedWeightedGraph()
        self.assertIsEmpty(g.vertices)
        vertices = ['a', 'b', 'c', 'd']
        for v in vertices:
            g.add_vertex(v)
        self.assertTrue(len(g.vertices) > 0)
        self.assertTrue(len(g.vertices) == 4)
        
        self.assertTrue(len(g.edge) == 0)        
        g.add_edge('a', 'b', 4)
        g.add_edge('a', 'c', 6)
        g.add_edge('a', 'd', 7)
        g.add_edge('b', 'c', 9)
        g.add_edge('b', 'a', 8)
        g.add_edge('c', 'd', 2)
        self.assertEqual(len(g.edge), 6)
        
        self.assertEqual(g.weight['a', 'b'], 4)
        self.assertNotEqual(g.weight['a','b'], g.weight['b','a'])

    def test_undirectedGraph(self):
        g = undirectedWeightedGraph()
        self.assertIsEmpty(g.vertices)
        vertices = ['a', 'b', 'c', 'd']
        for v in vertices:
            g.add_vertex(v)
        self.assertTrue(len(g.vertices) > 0)
        self.assertTrue(len(g.vertices) == 4)
        
        self.assertTrue(len(g.edge) == 0)        
        g.add_edge('a', 'b', 4)
        g.add_edge('a', 'c', 6)
        g.add_edge('a', 'd', 7)
        g.add_edge('b', 'c', 9)
        g.add_edge('c', 'd', 2)
        self.assertEqual(len(g.edge), 5)
        
        self.assertEqual(g.weight['a', 'b'], 4)
        self.assertEqual(g.weight['a','b'], g.weight['b','a'])
        self.assertEqual(g.weight['b','c'], 9)
        self.assertEqual(g.weight['c','b'], 9)
        self.assertNotEqual(g.weight['c', 'd'], 3)
         
    def test_permutation(self):
        permutations = []
        self.assertEqual(len(permutations), 0)
        list = [1,2,3,4]
        permutations = Application.permutePossibleRoute(list)
        self.assertTrue(len(permutations) > 0)
        self.assertTrue(len(permutations) == 24)
        
        
        