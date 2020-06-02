def getAvailableLetters(lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    availableLetters = ""
    for letter in alphabet:
        if letter in lettersGuessed:
            availableLetters = availableLetters
        else:
            availableLetters = availableLetters + letter
    return availableLetters

print(getAvailableLetters(["a", "c", "h", "m", "p"]))