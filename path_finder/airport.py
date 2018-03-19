'''
Created on 18 Mar 2018

@author: Eimg

'''
class Airport:
    """
    Airport class: Airports read in from CSV file to be stored in the Airport atlas.
    """
    #Creating empty container
    def __init__(self, airportInfo=[]):
        self.ID = airportInfo[0]
        self.Name = airportInfo[1]
        self.City = airportInfo[2]
        self.Country = airportInfo[3]
        self.Code = airportInfo[4]
        self.ICAO = airportInfo[5]
        self.lat = airportInfo[6]
        self.long = airportInfo[7]
        self.altitude = airportInfo[8]
        self.offsetHours = airportInfo[9]
        self.DST = airportInfo[10]
        self.timezone = airportInfo[11]
      
    def __str__(self):
        return "ID: %s,\nName: %s,\nCity: %s,\nCountry: %s,\nCode: %s,\nICAO: %s,\nlat: %s,\nlong: %s,\naltitude: %s,\noffsetHours: %s,\nDST: %s,\ntimezone: %s " % (self.ID, self.Name, self.City, self.Country, self.Code, self.ICAO, self.lat, self.long, self.altitude, self.offsetHours, self.DST, self.timezone)
    
class airport(Airport):
    def __init__(self, airportInfo=[]):
        Airport.__init__(self, airportInfo)   