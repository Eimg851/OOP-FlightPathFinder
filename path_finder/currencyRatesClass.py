'''
Created on 19 Mar 2018

@author: Eimg
'''
class CurrencyConverter:
    """
    CurrencyCoverter Class: CurrencyConverter reads in from CSV file to be stored in the Currency Rates Dictionary.
    """
    #Creating empty container
    def __init__(self, conversionInfo=[]):
        self.Name = conversionInfo[0]
        self.Code = conversionInfo[1]
        self.toEuroRate = conversionInfo[2]
        self.fromEuroRate = conversionInfo[3]
        
    def __str__(self):
        """
        Returns the instance in human readable form
        """
        return "Name: %s\nCode: %s\ntoEuroRate: %s\nfromEuroRate: %s" % (self.Name, self.Code, self.toEuroRate, self.fromEuroRate)
    