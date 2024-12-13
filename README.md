Wordle Code: 
Goal of code: 
    Our goal is to create a playable wordle with a visual color feed back and solves it with a solver.
    The solver code is a feature we added after the midterm. 

    Key Features of the game: 
    1. Randomly select a target word.
    2. Provide feedback with colors indicating correct/misplaced/incorrect letters.
    3. Limit attempts to six and display results after each guess.
    4. Enhance user experience with visual feedback

Designing the structure of the code: 
  Core Functions:
printboard(board): To display the current game state.
wordle_game(): To handle game logic and user input.

  Data Structures:
A dictionary (board) to store guesses and feedback.
Lists (letter_found, letter_in) to track green and yellow letters.

  Feedback Rules:
Use G for correct letters in correct positions.
Use Y for correct letters in incorrect positions.
Use - for incorrect letters.

Scenarios: 
  1. Ensure the guess is valid
  2. Comparing player's guess with target word
       Example:  Target word: glass
                 Guess word: class
                 Feedback: -GGGG

Challenges: 
  1. Repearing words: making sure that repeating letters in guess word are crossed off when guessing for a word that only have that one letter 
     Example:  Target word: glass
               Guess word: silly
               Therefore: cross the two "l" off in the guess "silly"

Wordle Solver Code: 
  Goal of code: 
  1. Make a guess
  2. Get feedback
  3. Narrowing down its options until finally solved
