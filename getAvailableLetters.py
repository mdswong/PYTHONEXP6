"""
Create a function getAvailableLetters that takes in one parameters - a list of letters,
lettersGuessed. This function will return a string that is comprised of lowercase
English letters - all lowercase English letters that are not in lettersGuessed.
"""

# getAvailableLetters - a function that will show a list of the guessed letters
# lettersGuessed - a list of letters

def getAvailableLetters(lettersGuessed):
    
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    strng = " "
    
    for x in alpha:
        if x not in lettersGuessed:
            strng = strng + x
    return strng
