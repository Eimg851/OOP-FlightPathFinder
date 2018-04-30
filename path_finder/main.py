'''
Created on 4 Apr 2018

@author: Eimg
'''
import currencyDict
import airportAtlas
import currencyRatesDict
import aircraftDict
import Set_ADT
import weightedDirectedGraph
import queue
import undirected_weighted_graph
import csv
from Set_ADT import Set
import itertools
from errorHandler import *
import gui

class Journey:
    def __init__(self, application):
        self.application = application
        
class Application:
    """
    Application class: Application class creates the dictionaries and methods to plan journeys
    """
    def __init__(self, paths):
        self.CurrencyLookUp = currencyDict.CurrencyDict(paths['currency'])
        self.AirportLookUp = airportAtlas.AirportAtlas(paths['airports'])
        self.ConversionRates = currencyRatesDict.CurrencyRates(paths['conversion'])
        self.AircraftLookUp = aircraftDict.aircrafts(paths['aircraft'])
        
    def run(self):
        """
        Takes input file from csv and explores optional flight paths for each journey
        """
        code = []
        #reading the test csv
        with open('..//input/input.csv') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                #Analyse each row individually
                if self.checkInputValidity(row):
                    if len(row) >= 6:
                        self.exploreOptionalFlightPath(row)
                    else:
                        #Checks to see if row has less than 6 airports if True, it prompts the user to decide whether or not to continue permuting best path
                        decision = input('There are less than 5 airports in this journey, would you like to find the shortest path anyway? (Y/N):')
                        if decision == "Y" or decision =="y":
                            self.exploreOptionalFlightPath(row)
                        else:
                            continue
                else:
                    print('ERROR: ',row,' - Airport/Aircraft code in input file is not valid')
                    print('\n*************************************************************************************\n')
                    
    def checkInputValidity(self, row):
        """
        Checks if input in the input csv is valid
        """
        for airport in range(0, len(row)-1):
            code = trimWhitespace(row[airport])
            #Replace airport code with trimmed version
            row[airport] = code
            #Check if the code is valid or if it exists in the airport dictionary or the aircraft dictionary
            if isValidCode(code) == False or code not in self.AirportLookUp.airportDict or row[-1] not in self.AircraftLookUp.aircraftDictionary:
                return False
        return True      
    
    
    def exploreOptionalFlightPath(self,listOfAirports):
        """
        Stores the list of airports on this route in a set and computes the cheapest path
        """
        #Creating a set to store the airports to be visited
        itinerary = Set_ADT.Set()
        #Store the first airports - i.e. the starting point in a variable
        start = listOfAirports[0]
        #Store the aircraft in a variable aircraft
        aircraftCode = listOfAirports[-1]
        aircraft = self.AircraftLookUp.getAircraft(aircraftCode)
        print("Starting journey from ", start, "with", aircraft, "Max. Range: ",aircraft.range, "km")
        #iterate over the 4 airports to be visited on the route and add them to the set
        for airport in range(1, len(listOfAirports)-1):
            itinerary.add(listOfAirports[airport])   
        #Permute all possible combinations of flight plan between the 4 visiting airports and store in a list
        ListOfPossibleRoutes = self.permutePossibleRoute(itinerary.to_string())
        #Add the starting airport to the set
        itinerary.add(start)
        #Pass the set to a directed weighted graph constructor that will hold the values of each singleLegCost as a weight between airports
        costOfFlightGraph = self.defineCost(itinerary.to_string())
        #Create a weighted undirected graph to store the distance of each singleLegTrip as a weight between airports
        flightDistanceGraph = self.defineDistance(itinerary.to_string())
        #Check to see if aircraft for this journey has the fuel capacity to travel the routes
        if self.checkRangeCanHandleDistance(aircraft, flightDistanceGraph) == False:
            print(listOfAirports[:-1], 'flying ',aircraft, 'is not possible due to fuel range of aircraft.')
            print('\n*************************************************************************************')
        else:
            route = self.findCheapestFlightPath(ListOfPossibleRoutes, costOfFlightGraph, start, aircraft)
            self.giveFlightPathBreakdown(route, costOfFlightGraph)
            #gui.PlotGraph(route, costOfFlightGraph)
            #self.findCheapestFlightPathDijkstra(ListOfPossibleRoutes, costOfFlightGraph, start, aircraft)
     
    def checkRangeCanHandleDistance(self, aircraft, distanceGraph):
        """
        Ensures that the aircraft flying this route can handle the distance of each leg of the trip
        """
        for weight in distanceGraph.weights:
            if int(distanceGraph.weights[weight]) > int(aircraft.range):
                return False
        return True

    def findCheapestFlightPath(self, ListOfPossibleRoutes, costOfFlightGraph, start, aircraft):
        """
        Finds the cheapest path of flight to the given airports
        """
        #Initialise the max cost of a trip
        max = 100000
        for i in range (0, len(ListOfPossibleRoutes)):
            #Store the route in a list
            FullRoute = []
            #Create a queue
            Airports_to_Vists = queue.Queue()
            #Add the starting airport to the list and the queue
            FullRoute.append(start)
            Airports_to_Vists.enqueue(start)
            #Add the remaining airports to the list and queue
            for j in range(0, len(ListOfPossibleRoutes[i])):
                FullRoute.append(ListOfPossibleRoutes[i][j])
                Airports_to_Vists.enqueue(ListOfPossibleRoutes[i][j])
            #Add the starting airport to the queue and list once more (this time acting as the end airport)
            Airports_to_Vists.enqueue(start)
            FullRoute.append(start)
            #Initialise the cost
            sumOfCost = 0.0
            while Airports_to_Vists.size() > 1:
                firstAirport = Airports_to_Vists.dequeue()
                nextStopover = Airports_to_Vists.front()
                #Add the cost of this trip to the total cost
                sumOfCost += float(costOfFlightGraph.weight[(firstAirport, nextStopover)])
            #check if total coast is less than the previous max and if so assign it the max.
            if sumOfCost < max:
                    max = sumOfCost
                    route = FullRoute
        print('The best route is ' , route, 'which costs €', format(max, '.2f'), 'in total')
        return route
    
    def permutePossibleRoute(self, setOfAirports):
        """
        Permutes all possible combinations of the set of airports to visit and returns it
        """
        list_of_possible_flight_path = list(itertools.permutations(setOfAirports))
        return list_of_possible_flight_path
        
    def defineDistance(self, setOfAirports): 
        """
        Creates and returns an undirected graph to store the distance between airport on the weighted edges. 
        """
        #Creates an instance of a weighted undirected graph and adds the list of airports as nodes
        distanceOfTripGraph = undirected_weighted_graph.undirectedWeightedGraph(setOfAirports)
        #Iterate over the nodes to avoid looping of nodes
        for i in range(0, len(setOfAirports)):
            for j in range(0, len(setOfAirports)):
                if setOfAirports[i] != setOfAirports[j]:
                    #Get the distance between the two nodes(airport) and assign to the weight
                    distance = self.AirportLookUp.getDistanceBetweenAirports(setOfAirports[i], setOfAirports[j])
                    distanceOfTripGraph.add_edge(setOfAirports[i], setOfAirports[j], distance)
        return distanceOfTripGraph   
    
    def defineCost(self, setOfAirports):
        """
        Creates and returns a weighted directed graph that stores the cost of trips between each airport
        """
        #Create an instance of a weighted directed graph and add the list of airports as nodes
        costOfTripGraph = weightedDirectedGraph.directedWeightedGraph(setOfAirports)
        #Iterate over the nodes to avoid looping of nodes
        for i in range(0, len(setOfAirports)):
            for j in range(0, len(setOfAirports)):
                if setOfAirports[i] != setOfAirports[j]:
                    #Get the cost of traveling from one node(airport) to another and assign it as a weight
                    distance = self.singleLegCost(setOfAirports[i], setOfAirports[j])
                    costOfTripGraph.add_edge(setOfAirports[i], setOfAirports[j], distance)
        return costOfTripGraph
         
    def singleLegCost(self, startAirport, EndAirport):
        """
        Computes the cost of a single leg trip between two airports
        """
        #take code 1 and code 2 find the corresponding country in the airport dict
        start = self.AirportLookUp.getAirport(startAirport)
        #find their currency using the currency dict
        currency_of_start_country= self.CurrencyLookUp.getCurrency(start.Country)
        #if currency is not euro find conversion rate
        if currency_of_start_country != "EUR":
            cost_per_KM = float(self.ConversionRates.conversionDict[currency_of_start_country].toEuroRate)
        else:
            cost_per_KM = 1
        #compute circle dist between two airports
        distance = self.AirportLookUp.getDistanceBetweenAirports(startAirport, EndAirport)
        #multiply distance in km ( amount of fuel needed) by euro equivalent of currency
        cost = cost_per_KM * distance
        #print('cost from ', start.Country, 'to, ', end.Country, 'is', cost_per_KM, ' x ', distance, 'which is = ', cost)
        return cost

    def giveFlightPathBreakdown(self, route, costGraph):     
        """
        Prints the cost of each leg of the route
        """ 
        #Creating a queue
        FinalPath = queue.Queue()
        #Adding the airports on this route to the queue
        for airport in range(0, len(route)):
                FinalPath.enqueue(route[airport])
        print('Flight Path Breakdown')
        while FinalPath.size() > 1:
            firstAirport = FinalPath.dequeue()
            nextStopover = FinalPath.front()
            #Finding cost of single leg trip
            cost = float(costGraph.weight[(firstAirport, nextStopover)])
            #Printing information on trip to console
            print('-', firstAirport, '-> ', nextStopover, "€",format(cost,'.2f')) 
        print('\n*************************************************************************************')      
        
    
if __name__ == '__main__':
    #path_to_test = sys.argv[1]
    paths = {
        'currency': '..//input/countrycurrency.csv', 
        'airports': '..//input/airport.csv', 
        'conversion': '..//input/currencyrates.csv',
        'aircraft':'..//input/aircraft.csv'
        }
    app = Application(paths)
    app.run()
    #app.run(path_to_test)