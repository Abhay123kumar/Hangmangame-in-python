import random

def select_random_word():
    word_list = ["python", "programming", "hangman", "challenge", "random", "computer", "science"]
    return random.choice(word_list)

def display_current_state(word, guessed_letters):
    display = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("Current word: ", display)
    return display

def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have a maximum of 6 incorrect guesses.\n")

    while incorrect_guesses < max_incorrect_guesses:
        display_current_state(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess. '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()
