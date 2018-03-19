'''
Created on 19 Mar 2018

@author: Eimg
'''
class Currency:
    """
    CurrencyCoverter Class: CurrencyConverter reads in from CSV file to be stored in the Currency Rates Dictionary.
    """
    #Creating empty container
    def __init__(self, currencyInfo=[]):
        self.Country= currencyInfo[0]
        self.Currency = currencyInfo[14]
        return self
        
    def __str__(self):
        return "Contry: %s\nCurrency: %s" % (self.Country, self.Currency)
    
class currency(Currency):
    def __init__(self, currencyInfo=[]):
        Currency.__init__(self, currencyInfo)  