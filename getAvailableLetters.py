def getAvailableLetters(lettersGuessed):
    
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    strng = " "
    
    for x in alpha:
        if x not in lettersGuessed:
            strng = strng + x
    return strng