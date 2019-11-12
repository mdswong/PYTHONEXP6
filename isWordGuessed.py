def isWordGuessed(secretWord, lettersGuessed):
    
    strng = 0
    
    for x in secretWord:
        if x in lettersGuessed:
            strng = strng + 1
        else:
            return False
    return True