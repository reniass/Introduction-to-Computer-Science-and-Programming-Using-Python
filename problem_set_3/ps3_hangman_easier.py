# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

secretWord = chooseWord(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    k = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            k += 1
    if k == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            s = s + " " + letter
        else:
            s = s + " _"
    return s


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    availableLetters = ""
    for letter in alphabet:
        if letter in lettersGuessed:
            availableLetters = availableLetters
        else:
            availableLetters = availableLetters + letter
    return availableLetters


"""
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretword)) +  " letters long.")
    print("-------------")
    guess = 8
    lettersGuessed = []
    chosen_letters = []
    while guess > 0:
        print("You have " + str(guess) + " guesses left."  )
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")
        if letter not in lettersGuessed:
            lettersGuessed.append(letter)
        if letter in secretword and letter not in lettersGuessed:
            print("Good guess: " + getGuessedWord(secretword, lettersGuessed))
            print("-------------")
        elif letter in chosen_letters:# przypadek gdy litera byla juz wybrana to jest zle
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretword, lettersGuessed))
            print("-------------")
        else: # przypadek kiedy litera nie wystepuje w odgadywanym slowie
            print("Oops! That letter is not in my word: " + getGuessedWord(secretword, lettersGuessed))
            print("-------------")
            guess -= 1
# do tablicy chosen_letters wpadaja litery ktore
        chosen_letters.append(letter)
# zrobic 2 przypadki zamiast 3 if(litera wystepuje) i else(litera nie wystepuje) i w else zrobic dwa przypadki 1 ze litera jest
# w lettersGuessed i 2 ze litera nie jest w lettersGuessed

    isWordGuessed(secretword, lettersGuessed)

hangman(secretword)
"""


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")
    guess = 8
    lettersGuessed = []
    letter = ""
    while guess > 0 and getGuessedWord(secretWord, lettersGuessed) != secretWord:
        print("You have " + str(guess) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")
        if letter in secretWord:
            if letter not in lettersGuessed:
                lettersGuessed.append(letter)
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
            else:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
        else:
            if letter not in lettersGuessed:
                lettersGuessed.append(letter)
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
                guess -= 1
            else:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else.")
        print("The word you were looking for was: " + secretWord + ".")


hangman(secretWord)