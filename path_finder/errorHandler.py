'''
Created on 19 Mar 2018

@author: Eimg
'''
def isValidCode(code):
    """
    Checks if code entered is a valid. A valid code contains 3 uppercase letters.
    """
    for character in code:
        if len(code) == 3 and character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return True
        else:
            return False

def trimWhitespace(code):
    """
    Removes white space from input
    """
    #Replaces spaces in the string and stores in variable trimmedCode
    trimmedCode = code.replace(" ", "")
    return trimmedCode