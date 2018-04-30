'''
Created on 14 Feabh 2018

@author: Eimg
'''
import sys

class Set:
    """
    Set: A unique collection of unordered items
    """
    __my_array = []
    __size_my_array = 0
    
    def __init__(self):
        """
        Constructs an instance of a set
        """
        self.__my_array = []
        self.__size_my_array = 0
        
    def size(self):
        """
        Returns the length of the set
        """
        return len(self.__my_array)
    
    def is_empty(self):
        """
        Returns true or false depending on whether or not set is empty
        """
        return len(self.__my_array) == 0
    
    def contains(self, elem):
        """
        Returns true or false depending on whether or not a set contains an item
        """
        contains = False
        for i in range(0,len(self.__my_array)):
            if self.__my_array[i] == elem:
                contains = True
        return contains
        
    def add(self, elem):
        """
        Adds an element to the set
        """
        adding = True
        for i in range(0,len(self.__my_array)):
            if self.__my_array[i] == elem:
                adding = False
                break;
        if adding == True:
            self.__my_array.append(elem)
            self.__size_my_array +=1
        
    def remove(self, elem):
        """
        Removes an element from the set
        """
        for i in range(0, len(self.__my_array)-1):
            if self.__my_array[i] == elem:
                self.__my_array.pop([i])
                self.__size_my_array -= 1
                    
    def union(self, b):
        """
        Joins the elements in two sets without duplicates
        """
        common = False
        for i in range(0, b.__size_my_array-1):
            for j in range(0,len(self.__my_array)-1):
                if b.__my_array[i] == self.__my_array[j]:
                    common = True
                    break
                if common == False:
                    self.add(b.__my_array[i])
                    break
                
    def intersection(self, b):
        """
        Keeps only the elements common to two sets
        """
        common = False
        for i in range(0,b.__size_my_array-1):
            j=0
            while common == False:
                if self.__my_array[j] == b.__my_array[i]:
                    common == True
            if common == False:  
                self.remove(self.__my_array[i])
    
    def difference(self, b):
        """
        Keeps the elements contained in the called set that are not in the passed instance
        """
        common = False
        for i in range(0, len(self.__my_array)-1):
            for j in range(0,b.__size_my_array-1):
                if self.__my_array[i] == b.__my_array[j]:
                    common = True
                    break
                if common == True:
                    self.remove(i)
        
    def to_string(self):
        """
        Returns the set in human readable form
        """
        return self.__my_array