# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # Recursive implementation

    if secretWord == "":
        return ""
    elif secretWord[0] in lettersGuessed:
        return secretWord[0] + getGuessedWord(secretWord[1 : ], lettersGuessed)
    else:
        return "_ " + getGuessedWord(secretWord[1 : ], lettersGuessed)

    # Iterative implementation

    # final = ""
    # for i in secretWord:
    #     if i not in lettersGuessed:
    #         final += "_ "
    #     else:
    #         final += i
    # return final

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # >>> print(string.ascii_lowercase)
    # abcdefghijklmnopqrstuvwxyz

    # Using List comprehension

    return "".join([x for x in string.ascii_lowercase if x not in lettersGuessed])

    # Iterative implementation

    # final = ""
    # for i in string.ascii_lowercase:
    #     if i not in lettersGuessed:
    #         final += i
    # return final

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
    # FILL IN YOUR CODE HERE...

    lives = 8
    LettersGuessed = []

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {0} letters long.".format(len(secretWord)))

    while lives != 0:
        if isWordGuessed(secretWord, LettersGuessed):
            break
        print("-------------")
        print("You have {0} guesses left.".format(lives))

        print("Available letters: {0}".format(getAvailableLetters(LettersGuessed)))

        letter_guessed = (input("Please guess a letter: ")).lower()

        if letter_guessed in LettersGuessed:
            print("Oops! You've already guessed that letter: {0}".format(getGuessedWord(secretWord, LettersGuessed)))
            continue

        LettersGuessed += [letter_guessed]

        if letter_guessed in secretWord:
            print("Good guess: {0}".format(getGuessedWord(secretWord, LettersGuessed)))
            continue
        else:
            print("Oops! That letter is not in my word: {0}".format(getGuessedWord(secretWord, LettersGuessed)))

        lives -= 1
    print("-------------")
    if isWordGuessed(secretWord, LettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was {0}.".format(secretWord))
    return


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
