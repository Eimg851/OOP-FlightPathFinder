'''
Created on 21 Feabh 2018

@author: Eimg
'''
class Aircraft:
    """
    Creates an instance of the aircraft class.
    """
    __MIN_FUEL = 100 #minimum amount of fuel for take off - no matter what aircraft
                    #declared here as a private static class variable
                    
    def __init__(self, aircraft_Info=[]):
        self.__fuel = 0                 #private attribute containing current fuel in aircraft
        self.__fuelCheck = False        #this is a boolean flag for a pre-flight check.
        self._maxFuel = self.__MIN_FUEL
        self.code = aircraft_Info[0]
        self.type = aircraft_Info[1]
        self.units = aircraft_Info[2]
        self.manufacturer = aircraft_Info[3]
        self.range = aircraft_Info[4]
            
         
    def fuelCheck(self):
        if self.__fuel < self.__MIN_FUEL:
            print("[",self.flightNumber,"] Fuel Check Failed: Current fuel below safe limit:",
                  self.__fuel,
                  "less than", self.__MIN_FUEL)
            self.__fuelCheck = False
        else:
            print("[",self.flightNumber,"] Fuel Check Complete. Current Fuel Level:", self.__fuel)
            self.__fuelCheck = True
        return self.__fuelCheck
            
    def printFuelLevel(self):
        print("Current fuel:", self.__fuel)
        
    def useFuel(self, volume):
        self.__fuel = self.__fuel - volume

    def addFuel(self, volume):
        unusedFuel = 0
        if volume < 0:
            print("No syphoning fuel!")
        elif self.__fuel+volume<= self._maxFuel:
            self.__fuel = self.__fuel+volume
        elif self.__fuel + volume > self._maxFuel:
            self.__fuel = self._maxFuel
            unusedFuel = volume - self.__fuel
        return unusedFuel
    
    def __repr__(self):
        return "%s %s %s" % (self.manufacturer, self.code, self.type)
        
        