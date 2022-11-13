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

WORDLIST_FILENAME = "words.txt"
chance= 6
secret_word=" "
guessed_letter=[]
correct_guessed = False
match_find = False
match_list=[]
noMatch_list=[]


def guess_chance():
	if chance is None:
		num_of_chance=6
	else:
		num_of_chance=chance
	return num_of_chance



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
   # print(line)
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

def get_uniqe_letter(letters_guessed ,secret_word):
    letter = 0
    for i in letters_guessed:
        if i in secret_word:
            letter += 1
    return letter

def is_word_guessed(secret_word, letters_guessed):
    '''
      secret_word: string, the word the user is guessing; assumes all letters are

        lowercase
      letters_guessed: list (of letters), which letters have been guessed so far;
        assumes that all letters are lowercase
      returns: boolean, True if all the letters of secret_word are in letters_guessed;
        False otherwise
      '''
    letter=0
    for i in letters_guessed:
        if i in secret_word:
            letter+=secret_word.count(i)
    if letter==len(secret_word):
        correct_guessed = True
    else:
        correct_guessed = False
    return correct_guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letter_guessed_correct = []
    for i in secret_word:
        if i in letters_guessed:
            letter_guessed_correct.append(i)
    result=''
    for i in secret_word:
        if i in letter_guessed_correct:
            result+=i
        else:
            result+='_ '
    return  result




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    result=list(string.ascii_lowercase )
    for i in letters_guessed:
        result.remove(i)
    return ''.join(result)

    
    

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

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")

    global letters_guessed
    wrong_guessed=0
    letters_guessed=[]
    warning = 3


    while guess_chance()-wrong_guessed > 0:
        if is_word_guessed(secret_word, letters_guessed):
            print("-------------")
            print("Congratulations, you won!")
            chance_rem = guess_chance() - wrong_guessed
            score = chance_rem * get_uniqe_letter(letters_guessed,secret_word)
            print("Your total score for this game is:",score)
            break

        else:
            print("-------------")
            print("You have", guess_chance() - wrong_guessed, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            guess = letter=input("Please guess a letter:").lower();
            if not guess.isalpha():
                warning =warning-1
                print("Oops! That is not a valid letter. You have",warning,"warnings left:", get_guessed_word(secret_word,letters_guessed))

                if warning ==0 or warning < 0:
                    wrong_guessed+=1
                    warning =1
            elif len(guess) >1:
                print("Sorry you are allow to input one character.")

            else:
                if guess in letters_guessed:
                    print("Oops! You've already guessed that letter:", get_guessed_word(secret_word,letters_guessed))
                elif guess in secret_word and guess not in letters_guessed:
                    letters_guessed.append(guess)
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                else:
                    letters_guessed.append(guess)
                    wrong_guessed += 1
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        if guess_chance() - wrong_guessed == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.", secret_word)
            break

        else:
            continue




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
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    my_word=my_word.replace(' ','')
    if len(my_word) != len(other_word):
        match_find= False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_' and  my_word[i] !=other_word[i]  or my_word[i] is not '_' and my_word[i] is not other_word[i]:
                match_find = False
                break
            else:
                match_find = True

    return match_find


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in wordlist:
        if  match_with_gaps(my_word,i):
            match_list.append(i)
        else:
            noMatch_list.append(i)
    if len(match_list) == 0:
        print("no match Found")

    print(match_list)



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    global letters_guessed
    wrong_guessed = 0
    letters_guessed = []
    warning = 3

    while guess_chance() - wrong_guessed > 0:
        if is_word_guessed(secret_word, letters_guessed):
            print("-------------")
            print("Congratulations, you won!")
            chance_rem = guess_chance() - wrong_guessed
            score = chance_rem * get_uniqe_letter(letters_guessed,secret_word)
            print(letters_guessed)
            print("Your total score for this game is:", score)
            break

        else:
            print("-------------")
            print("You have", guess_chance() - wrong_guessed, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            guess = letter = input("Please guess a letter:").lower();
            if not guess.isalpha() and guess != '*':
                warning = warning - 1
                print("Oops! That is not a valid letter. You have", warning, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
                if warning == 0 or warning < 0:
                    wrong_guessed += 1
                    warning = 1
            elif len(guess) > 1:
                print("Sorry you are allow to input one character.")
            elif guess == '*':
                my_word=get_guessed_word(secret_word, letters_guessed)
                show_possible_matches(my_word)

            else:
                if guess in letters_guessed:
                    print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
                elif guess in secret_word and guess not in letters_guessed:
                    letters_guessed.append(guess)
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                else:
                    letters_guessed.append(guess)
                    wrong_guessed += 1
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        if guess_chance() - wrong_guessed == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.", secret_word)
            break

        else:
            continue


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word =choose_word(wordlist)
    hangman_with_hints(secret_word)
