# Wordle game
#
# Portfolio project #1 
#
# By: Andrew Higginbotham
#
# This is a text based Wordle game using over 5700 5 letter words compiled by
# Stanford University. It allows the user to guess up to 6 guesses returning the
# correctly guessed characters in the correct places (In GREEN). It will also show the correct
# misplaced characters (in YELLOW). Incorrect characters will leave a RED underscore.

# Import required libraries Random, CSV Libraries
from random import randint
import csv
from colorama import Fore
import os

# Variable Declarations

wordle_word = ""
valid_guess_length = 5
guess_valid = True

# 5 Letter Word Dictionary
# extracted from Stanford University sgb-word.txt
# and is saved in the directory as 5_letter_words.csv


# Game Functions


# RANDOM WORD GENERATOR
#
# This function will read the 5_letter_word.csv file, capture the number of words
# in the file and return a random word as wordle_word
# Feel free to add your own 5 letter words to the file (maybe local slang words)
# for an extra twist to the game.
#
def wordle_word_choice():
    with open('5_letter_words.csv') as word:
        row_count = sum(1 for row in word)
        rnd_index = randint(1, row_count)
        word.seek(0)
        csv_reader = csv.reader(word)
        for index, row in enumerate(csv_reader):
             if index == rnd_index:
                wordle_word = (row[1])
                return wordle_word.upper()

# Display Current Results
# This functions is used to take the incorrect result and display it to the screen 
# with the correct colors and underscores so the player gets and appropriate hint
# to continue playing the game successfully.
#
def display_current_results(wordle_word, guess):
    guess_list =""

    for letter in range(0, 5):
        if guess[letter] in wordle_word:
            if guess[letter] != wordle_word[letter]:
                new_letter = (Fore.YELLOW + (str(guess[letter])) + Fore.WHITE)
                guess_list += new_letter
            else:
                # guess[letter] == wordle_word[letter]:
                new_letter = (Fore.GREEN + (str(guess[letter])) + Fore.WHITE)
                guess_list += new_letter
        else:
            new_letter = (Fore.RED + "_" + Fore.WHITE)
            guess_list += new_letter
    print("Your current guess: " + guess_list)

# Check qualification of guess
# This function will check the guess for the proper lenght 
# of 5 characters, if not valid will return False
#
def check_guess(guess):
    if len(guess) != valid_guess_length:
        return False
        
# Function to check if guess is a valid
# word within the dictionary
#
def valid_dictionary(guess):
    search_word = guess.lower()
    with open('5_letter_words.csv', 'r') as search_list:
        reader = csv.reader(search_list, delimiter=',')
        for line in reader:
            if search_word in line:
                return True
            
    
    
            

# Game Play Module
# 
def game_play():
    # Define local variables
    guess = "" # this is your guess
    guess_list = "" # this is the resulting guess
    guess_number = 1 # this is the number of guesses left
    #valid_guess_length = 5
    wordle_word = wordle_word_choice() # Get a random 5 letter word
    #guess_valid = True
    
    # Welome Screen Graphics
    os.system("cls")
    print("")
    print("")
    print("                Welcome to " + Fore.GREEN + "W" + Fore.YELLOW + "O" + Fore.RESET + "R" + Fore.GREEN + "D" + Fore.YELLOW +"L" + Fore.RESET + "E")
    print("")
    print("Wordle is a 5 letter word guessing game. You have")
    print("6 guesses to guess the correct random word. If your")
    print("guess shows a " + Fore.GREEN + "GREEEN " + Fore.RESET + "letter that letter is correct")
    print("and in the correct place. If the letter is " + Fore.YELLOW + "YELLOW")
    print(Fore.RESET + "the letter is correct just in the wrong spot.")
    print("If there is a red " + Fore.RED + "_" + Fore.RESET + ", the letter is incorrect and")
    print("not in the word")
    print("")
    
    #print(wordle_word)
    # User guesses
    while guess_number < 7:
        # First check for valid number of letters in guess
        guess = input("Enter your guess " + str(guess_number)+ ": ")
        guess = guess.upper()
        
         
        if check_guess(guess) == False:
            print("Invalid number of letters in guess, try again!")
        
        elif valid_dictionary(guess) != True:
            print("Word not in dictionary, try again!")
        
        else:
            if guess == wordle_word:
                print("Congratulations, You WON!")
                new_game = input("Would you like to play a new game? Y/N: ")
                if (new_game.upper() == "Y"):
                    game_play()
                else:
                    break
            guess_number += 1
            display_current_results(wordle_word, guess) # Display current guess resuts
    
    print("The word was:" + wordle_word)
    new_game = input("Sorry you lost. Try again? Y/N: ")
    if (new_game.upper() == "Y"):
        game_play()


         


# testing Area 
game_play()



