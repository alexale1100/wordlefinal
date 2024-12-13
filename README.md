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
Drawbacks of Code:
    1. Can only guess from available words from wordlist: although the wordlist has lots of words, basic words such as "adieu", a common first guess for many players, are not in the wordlist. Thus, players cannot guess all the possible words and there is a chance that the word they guess is a real word, but is not available in the wordlist which makes their guess invalid.

    2. No colored keyboard: in the real Wordle game on the NYT, the game comes with a keyboard that shows the player which letter is not used yet, not in the word, in the word but in the wrong place, or is correctly guessed. This visual feature aids the player in their experience with the game. In this code, the code only show the player the color of the letters in the word they guess and does not provide a keyboard.
        
Wordle Solver Code: 
  Goal of code: 
  1. Make a guess
  2. Get feedback
  3. Narrowing down its options until finally solved
