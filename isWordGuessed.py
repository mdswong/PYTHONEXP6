"""
Create a function that is named as: isWordGuessed that takes in two parameters -
a string, secretWord, and a list of letters, lettersGuessed. This function will return a 
boolean - True if secretWord if all the letters of secretWord as in lettersGuessed 
and False if not.
"""

# secretWord - a string
# lettersGuessed - a list of letters

def isWordGuessed(secretWord, lettersGuessed):
    
    strng = 0
    
    for x in secretWord:
        if x in lettersGuessed:
            strng = strng + 1
        else:
            return False
    return True
