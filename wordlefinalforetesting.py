import random
from wordlist import wordlist 

def get_feedback(guess, target_word):
    """
    Generate feedback for the guessed word compared to the target word.
    Feedback:
    - 'G' for correct letter in the correct position (Green)
    - 'Y' for correct letter in the wrong position (Yellow)
    - '_' for incorrect letter (Gray)
    """
    feedback = ["_"] * 5
    target_list = list(target_word)

    # First pass: Find 'G' (correct position)
    for i, char in enumerate(guess):
        if char == target_word[i]:
            feedback[i] = "G"
            target_list[i] = None  # Mark as used

    # Second pass: Find 'Y' (wrong position)
    for i, char in enumerate(guess):
        if feedback[i] == "_" and char in target_list:
            feedback[i] = "Y"
            target_list[target_list.index(char)] = None  # Mark as used

    return "".join(feedback)

def filter_wordlist(wordlist, guess, feedback):
    """
    Refine the wordlist based on the feedback.
    - Eliminate words that don't match the feedback for the guess.
    """f
    filtered_words = []
    for word in wordlist:
        if get_feedback(guess, word) == feedback:
            filtered_words.append(word)
    return filtered_words

def wordle_solver(wordlist, target_word):
    """
    Solve the Wordle puzzle.
    - wordlist: list of possible words
    - target_word: the word to guess
    """
    possible_words = wordlist.copy()
    attempts = 6  # Number of allowed attempts

    print("Starting Wordle Solver...\n")

    for attempt in range(1, attempts + 1):
        # Pick a guess (can optimize here by selecting words intelligently, but for simplicity, use the first word)
        guess = possible_words[0]
        print(f"Attempt {attempt}: Guess = {guess}")

        # Get feedback for the guess
        feedback = get_feedback(guess, target_word)
        print(f"Feedback: {feedback}")

        if feedback == "GGGGG":
            print(f"Solved! The word is '{guess}' in {attempt} attempts.")
            return

        # Filter the wordlist based on the feedback
        possible_words = filter_wordlist(possible_words, guess, feedback)

        if not possible_words:
            print("No more possible words. Solver failed.")
            return

    print(f"Failed to solve Wordle within {attempts} attempts. The word was '{target_word}'.")

# Example usage
if __name__ == "__main__":
    # Define a wordlist (this is a small example, but in real use, you can use a larger wordlist)
    # wordlist = [
    #     "apple", "brick", "chair", "glass", "table", "ocean", "crane", "shiny", "track", "stone", "mango", "grape"
    # ]
    wordlist = wordlist

    # Define the target word (this is the word the solver needs to guess)
    # target_word = "crane"  # Change to the word you want to guess
    target_word = random.choice(wordlist).lower()

    # Solve the Wordle puzzle
    wordle_solver(wordlist, target_word)
