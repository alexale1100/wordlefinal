import random
from wordlist import wordlist  # Import the word list from a separate module or file
from termcolor import colored, cprint

from wordlesolver import *

def printboard(board):
    # board is the dictionary
    for index, key in enumerate(board):
        letters = board[key]["letters"]
        colors = board[key]["colors"]

        # https://pypi.org/project/termcolor/ # colors to use

        for ci, letter in enumerate(letters):
            if colors[ci] == "Y":
                cprint(letter, "light_yellow", "on_black", end=" ")
            elif colors[ci] == "G":
                cprint(letter, "green", "on_black", end=" ")
            else:
                print(letter, end=" ")
            if ci == 4:
                print("")
    print()

    # make a list of letters
    # using cprint 
    # print letters in letter_in as yellow
    # print letters in letter_in as green

    # DO KEYBOARD PRINT HERE


def wordle_game():
    # Choose a random word from the word list
    target_word = random.choice(wordlist).lower()
    # target_word = "glass"
    attempts = 6  # Number of allowed attempts

    letter_found = ["-", "-", "-", "-", "-"]
    letter_in = []

    board = {"guess_one"  : {"letters":[], 
                           "colors":[]},
             "guess_two"  : {"letters":["-", "-", "-", "-", "-"], 
                           "colors":["-", "-", "-", "-", "-"]},
             "guess_three": {"letters":[], 
                           "colors":[]},
             "guess_four" : {"letters":[], 
                           "colors":[]},
             "guess_five" : {"letters":[], 
                           "colors":[]},
             "guess_six"  : {"letters":[], 
                           "colors":[]},
             }


    print("Welcome to Wordle! You have 6 attempts to guess the 5-letter word.")

    loopnum = -1
    while attempts > 0:
        loopnum += 1
        guess = input("Enter your 5-letter guess: ").lower()
        
        # Ensure the guess is valid
        if len(guess) != 5 or (guess not in wordlist):
            print("Invalid guess. Please enter a valid 5-letter word.")
            continue
        
        # Check if the player has guessed correctly
        if guess == target_word:
            print(f"Congratulations! You've guessed the word '{target_word}'!")
            break
        else:
            feedback = ["-", "-", "-", "-", "-"]
            target_copy = target_word
            for i, letter in enumerate(guess):
                if letter == target_word[i]:
                    feedback[i] = "G"
                    target_copy = target_copy[:i] + "0" + target_copy[i+1:]

                    letter_found[i] = letter
                    for k, letter_y in enumerate(letter_in):
                        if letter == letter_y:
                            letter_in.pop(k) 
                            break

                elif letter in target_copy:
                    feedback[i] = "Y"
                    letter_in.append(letter)
                    for j, tc_letter in enumerate(target_copy):
                        if letter == tc_letter:
                            target_copy = target_copy[:j] + "0" + target_copy[j+1:]
                            break
                
            for index, key in enumerate(board):
                if index == loopnum:
                    board[key]["colors"] = feedback
                    board[key]["letters"] = list(guess)

            printboard(board)
            # print("    Feedback:", feedback)
            # print("    greens", letter_found)
            # print("    yellows", letter_in)

        attempts -= 1
        print(f"Attempts remaining: {attempts}")
        # wordle_solver(wordlist, target_word)

    if attempts == 0:
        print(f"Game over! The word was '{target_word}'.")

# Run the game
if __name__ == "__main__":
    wordle_game()
