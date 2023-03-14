import random

# List of possible words, you can keep on adding your words as per you need in the below list
words = ["apple", "banana", "cherry", "orange", "lemon"]

# Choose a random word from the list
word = random.choice(words)

# Create a list to store the letters guessed by the player
guessed_letters = []

# Set the number of tries allowed
max_attempts = 6

# Main game loop
while True:
    # Print the current status of the word
    status = ""
    for letter in word:
        if letter in guessed_letters:
            status += letter
        else:
            status += "_"
    print("Current word: ", status)

    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter. 🤦️")

    # Check if the letter is in the word
    elif guess in word:
        print("Correct!👏 👏 👏")
        guessed_letters.append(guess)

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print("Congratulations, you won!😍")
            break

    # If the letter is not in the word
    else:
        print("Incorrect.😭 😭 😭")
        guessed_letters.append(guess)
        max_attempts -= 1

        # Check if the player has run out of attempts
        if max_attempts == 0:
            print("Sorry, you lost. The word was", word)
            break
