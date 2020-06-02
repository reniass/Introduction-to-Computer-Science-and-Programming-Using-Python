def isWordGuessed(secretWord, lettersGuessed):
    k = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            k += 1
    if k == len(secretWord):
        return True
    else:
        return False

print(isWordGuessed("mama", ["m", "a"]))
