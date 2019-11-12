def getGuessedWord(secretWord, lettersGuessed):
    
    strng = " "
    
    for x in secretWord:
        if x in lettersGuessed:
            strng = strng + x
        else:
            strng = strng + "_"     
    return strng