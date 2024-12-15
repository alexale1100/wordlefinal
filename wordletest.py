from wordlesolver import *

# test valid guess

def test_invalid_guess():
    output_of_game = wordle_solver(["asde", "spine"], "spine")
    # assert output_of_game[1] == ”Invalid guess. Please enter a valid 5-letter word.“

# test winning the game

def test_correct_guess():
    target_word = "spine"
    output_of_game = wordle_solver(["glass", "glass", "ready", "ready", "spine"], target_word)
    # assert output_of_game[1] == f”Congratulations! You‘ve guessed the word ’{target_word}‘!“


# test failing the game
def test_fail_game():
    words_to_guess = ["hello", "ready", "ready", "ready", "ready", "ready"]
    target_word = "drive"
    output_of_game = wordle_solver(words_to_guess, target_word)
    # assert output_of_game[1] == ”Game over! The word was ’{target_word}‘.“


print("test invalid guess")
test_invalid_guess()

print("test correct guess")
test_correct_guess()

print("test fail game")
test_fail_game()
