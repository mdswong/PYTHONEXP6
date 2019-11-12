def Hangaroo(secretWord):
    
    lettersGuessed = []
    guesses = 5
    
    print("Welcome to Hangman!")
    print("I am thinking of a word that is ", len(secretWord), "letters long.")
    
    while guesses > 0:
        print("You have ", guesses, " guesses left.")
        print("Available Letters: ", getAvailableLetters(lettersGuessed))
        
        guess = input("Guess a letter: ")
        
        if(guess not in secretWord):
            print("Oops! That letter is not in my word. ", getGuessedWord(secretWord, lettersGuessed))
            guesses = guesses - 1
        elif (guess in lettersGuessed):
            print("Oops! You already guessed that letter. Try again!", getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Nice guess! That letter is in my word. ", getGuessedWord(secretWord, lettersGuessed))
        lettersGuessed.append(guess)
        
        if (isWordGuessed(secretWord, lettersGuessed) == True):
            print("Congratulations! You have won!")
            print("The word was ", secretWord)
            return
        
    if(guesses == 0):
        print("Sorry, you have ran out of guesses! The word was ", secretWord)
        print("Game Over!")
        return