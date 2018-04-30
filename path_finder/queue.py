'''
Created on 25 Apr 2018

@author: Eimg
'''
class Queue:
    """
    Creates an instance of queue
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """
        Returns true or false depending on whether or not queue is empty
        """
        return self.items == []

    def enqueue(self, item):
        """
        Adds item to end of queue
        """
        self.items.insert(0,item)

    def dequeue(self):
        """
        Removes first item of the queue and returns it
        """
        return self.items.pop()

    def size(self):
        """
        Returns the length of the queue
        """
        return len(self.items)
    
    def front(self):
        """
        Returns the first element in the queue
        """
        return self.items[-1]
    
    def str(self):
        """
        Returns the queue in human readable form
        """
        return str(self.items)
    