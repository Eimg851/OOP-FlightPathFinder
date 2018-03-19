'''
Created on 19 Mar 2018

@author: Eimg
'''
def isValidCode(code):
    """
    Checks if code entered is a valid IATA code
    """
    for character in code:
        if len(code) == 3 and character in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
        else:
            return False