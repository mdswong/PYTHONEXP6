"""
Create a function getGuessedWord that takes in two parameters - a string,
secretWord, and a list of letters, lettersGuessed. This function will return a string
that is comprised of letters and underscores, based on what letters in 
lettersGuessed are in secretWord. This shouldn't be too different from 
isWordGuessed.
"""

# secretWord - a string
# lettersGuessed - a list of the letters
# string - return, consists of letters and underscores

def getGuessedWord(secretWord, lettersGuessed):
    
    strng = " "
    
    for x in secretWord:
        if x in lettersGuessed:
            strng = strng + x
        else:
            strng = strng + "_"     
    return strng
