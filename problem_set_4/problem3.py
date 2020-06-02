WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    for letter in word:
        new_hand[letter] -= 1

    return new_hand

def isValidWord(hand, word, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    v = 0
    new_hand = hand.copy()
    for letter in word:
        if letter in new_hand:
            v += 1
            new_hand[letter] -= 1
            if new_hand[letter] == 0:
                del new_hand[letter]
        else:
            break

    if word in wordList and v == len(word):
        return  True
    else:
        return  False



print(isValidWord({'m' : 1, 'o' : 1, 't' : 1, 'h' : 1, 'e' : 1, 'r': 1}, 'mother', loadWords()))
print(isValidWord({'u': 1, 'r': 1, 'p': 2, 'a': 3, 't': 1, 'e': 1}, 'rapture', loadWords()))

