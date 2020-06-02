def getGuessedWord(secretWord, lettersGuessed):
    s = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            s = s + " " + letter
        else:
            s = s + " _"
    return  s

print(getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's']))