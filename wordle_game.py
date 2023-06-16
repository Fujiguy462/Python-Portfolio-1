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
def display_current_results(wordle_word, guess):
    letter_position = 0
    for letter in guess:
        if letter in wordle_word:# Check to see if the letter in in the wordle word.
            #Check to see if the letter matches the same location in the word
            if letter == wordle_word[letter_position]:
                # If it is Make it Green
                guess[letter_position] = 
            # If not make it Yellow
        # Since it is not in the word change the letter to a RED underscore
    print(wordle_word)
    print(guess)


    

# Game Play Module
# 
def game_play():


    # Define local variables
    guess = [] # this is your guess
    guess_number = 1 # this is the number of guesses left
    valid_guess_length = 5
    wordle_word = wordle_word_choice() # Get a random 5 letter word
    
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
    
    # User guesses
    while guess_number < 7:
        # First check for valid number of letters in guess
        guess = input("Enter your guess " + str(guess_number)+ ": ")
        guess = guess.upper()
        if len(guess) != valid_guess_length:
            print("Invalid number of letters in guess, try again!")
        else:
            # Check to see if guess is correct
            if guess == wordle_word:
                print("Congratulations, You WON!")
                new_game = input("Would you like to play a new game? Y/N")
                if (new_game.upper() == "Y"):
                    game_play()
                else:
                    break
            guess_number += 1 
        # Display current guess resuts
        display_current_results(wordle_word, guess)

         


# testing Area 
game_play()



