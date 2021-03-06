# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps2/words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for elem in secret_word:
      if elem not in letters_guessed:
        return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for elem in secret_word:
      if elem not in letters_guessed:
        guessed_word.append('_ ')
        continue
      guessed_word.append(elem)
    return ''.join(guessed_word)
# print(get_guessed_word(secret_word='apple', letters_guessed=['e', 'i', 'k', 'p', 'r', 's'])) # test function get_guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = list(string.ascii_lowercase)
    for elem in letters_guessed:
      if elem in available_letters:
        available_letters.remove(elem)
    return ''.join(available_letters)
# print(get_available_letters(letters_guessed=['e', 'i', 'k', 'p', 'r', 's'])) test function get_available_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings_left = 3
    guess_left = 6    # int: numbers of guesses left.
    letters_guessed = []    # list[string]: letters that have been guessed.
    vowels = ['a', 'e', 'i', 'o']   # list[string]: letters that are vowels.
    print('''Welcome to the game Hangman!
    I am thinking of a word that is {0:d} letters long.'''.format(len(secret_word)))

    while guess_left != 0:
      print('''--------------------
      You have {0:d} guesses left.
      Available letters: {1:s}'''.format(guess_left, get_available_letters(letters_guessed)))
      user_input = str(input('Please guess a letter: ')).lower()    # ask user to enter a letter


      if len(user_input) != 1:    # check if user enters a single character
        if warnings_left != 0:
          warnings_left -= 1
          print('''Oops! Seems you enter other than a single letter. Now you have {0:d} warnings left'''.format(warnings_left))
          # user_input = str(input('Please guess a letter: ')).lower()    # ask user to enter a letter
          continue
      elif user_input not in string.ascii_lowercase:    # check if user enters other than a letter
        if warnings_left != 0:
          warnings_left -= 1
          print('''Oops! Seems you entered an invalid letter. Now you have {0:d} warnings left'''.format(warnings_left))
          # user_input = str(input('Please guess a letter: ')).lower()    # ask user to enter a letter
          continue
      elif user_input not in get_available_letters(letters_guessed):    # check if user enters a letter that has been entered before
        if warnings_left != 0:
          warnings_left -= 1
          print('''Oops! Seems the letter you entered had beed chosen before. Now you have {0:d} warnings letft'''.format(warnings_left))
          # user_input = str(input('Please guess a letter: ')).lower()    # ask user to enter a letter
          continue


      letters_guessed.append(user_input)    # append guessed letter to letters_guessed
      if user_input in secret_word and user_input not in letters_guessed[:-1]:   # show if user guessed right or not
        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
          print('''Congratulations, you won!
          Your total score for this game is:''', guess_left * len(set(secret_word)))
          return None
      else: 
        guess_left -= 1
        if user_input in vowels and user_input not in get_available_letters(letters_guessed):
          guess_left -= 1
        if guess_left <= 0 and get_guessed_word(secret_word, letters_guessed) != secret_word:
          print('Sorry, you ran out of guesses. The word was {0:s}'.format(secret_word))
          return None
        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
      

    return None


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = ''.join(my_word.split())    # delete spaces in my_word

    if len(my_word) != len(other_word):   # check if my_word and other_word is of the same length
      return False
    
    for idx in range(len(my_word)):   # check if letters my_word match letters in other_word, symbol '_' not included
      if my_word[idx] == '_':
        continue
      elif my_word[idx] != other_word[idx]:
        return False

    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = ''.join(my_word.split())    # delete spaces in my_word
    has_match_flag = False    # set match flag

    for i in wordlist:    # iterate over wordlist to see if match my_word and print matched results
      if match_with_gaps(my_word, i):
        has_match_flag = True
        print('{0:s}\t'.format(i), end='')

    if not has_match_flag:    # if no match, print no matches found
      print('No matches found.')

    return None

show_possible_matches("a_ pl_ ") 

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings_left = 3
    guess_left = 6    # int: numbers of guesses left.
    letters_guessed = []    # list[string]: letters that have been guessed.
    vowels = ['a', 'e', 'i', 'o']   # list[string]: letters that are vowels.
    print('''Welcome to the game Hangman!
    I am thinking of a word that is {0:d} letters long.'''.format(len(secret_word)))

    while guess_left != 0:
      print('''--------------------
      You have {0:d} guesses left.
      Available letters: {1:s}'''.format(guess_left, get_available_letters(letters_guessed)))
      user_input = str(input('Please guess a letter: ')).lower()    # ask user to enter a letter

      if user_input == '*':   # if user_input is '*', show possible matches with current guessed letters
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        continue

      if len(user_input) != 1:    # check if user enters a single character
        if warnings_left != 0:
          warnings_left -= 1
          print('''Oops! Seems you enter other than a single letter. Now you have {0:d} warnings left'''.format(warnings_left))
          # user_input = str(input('Please guess a letter: ')).lower()    # ask user to enter a letter
          continue
      elif user_input not in string.ascii_lowercase:    # check if user enters other than a letter
        if warnings_left != 0:
          warnings_left -= 1
          print('''Oops! Seems you entered an invalid letter. Now you have {0:d} warnings left'''.format(warnings_left))
          # user_input = str(input('Please guess a letter: ')).lower()    # ask user to enter a letter
          continue
      elif user_input not in get_available_letters(letters_guessed):    # check if user enters a letter that has been entered before
        if warnings_left != 0:
          warnings_left -= 1
          print('''Oops! Seems the letter you entered had beed chosen before. Now you have {0:d} warnings letft'''.format(warnings_left))
          # user_input = str(input('Please guess a letter: ')).lower()    # ask user to enter a letter
          continue


      letters_guessed.append(user_input)    # append guessed letter to letters_guessed
      if user_input in secret_word and user_input not in letters_guessed[:-1]:   # show if user guessed right or not
        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
          print('''Congratulations, you won!
          Your total score for this game is:''', guess_left * len(set(secret_word)))
          return None
      else: 
        guess_left -= 1
        if user_input in vowels and user_input not in get_available_letters(letters_guessed):
          guess_left -= 1
        if guess_left <= 0 and get_guessed_word(secret_word, letters_guessed) != secret_word:
          print('Sorry, you ran out of guesses. The word was {0:s}'.format(secret_word))
          return None
        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
      

    return None



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman('right')

###############
    
    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)