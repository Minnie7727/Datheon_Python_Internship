import random

# Hangman art stages for incorrect guesses
HANGMAN_PICS = [
    """
       +---+
           |
           |
           |
          ===""",
    """
       +---+
       O   |
           |
           |
          ===""",
    """
       +---+
       O   |
       |   |
           |
          ===""",
    """
       +---+
       O   |
      /|   |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==="""
]

def play_hangman():
    words = ["python", "developer", "internship", "program", "automation", "coding"]
    secret_word = random.choice(words)
    
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("========================================")
    print("      WELCOME TO THE HANGMAN GAME       ")
    print("========================================")

    while incorrect_guesses < max_incorrect:
        print(HANGMAN_PICS[incorrect_guesses])
        print("\n")

        # Display masked word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word.strip()}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Check for win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            print("YOU WIN!")
            break

        # Get player guess
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabet letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Incorrect! '{guess}' is not in the word.")
            incorrect_guesses += 1

    else:
        print(HANGMAN_PICS[max_incorrect])
        print(f"\nGame Over! The secret word was: {secret_word}")
        print("Better luck next time!")

if __name__ == "__main__":
    play_hangman()