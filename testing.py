from colorama import Fore

wordle_word = "about"
guess = "store"

guess_list =""

for letter in range(0, 5, 1):
    if guess[letter] in wordle_word:
        if guess[letter] != wordle_word[letter]:
            new_letter = (Fore.YELLOW + (str(guess[letter])) + Fore.WHITE)
            guess_list += new_letter
        if guess[letter] == wordle_word[letter]:
            new_letter = (Fore.GREEN + (str(guess[letter])) + Fore.WHITE)
            guess_list += new_letter
    else:
        new_letter = (Fore.RED + "_" + Fore.WHITE)
        guess_list += new_letter
    
        

print(guess_list)
            
            

        

