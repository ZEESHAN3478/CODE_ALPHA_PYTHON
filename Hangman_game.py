import random

# Predefined words list
words = ["python", "java", "computer", "program", "developer"]

# Random word selectr
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

display_word = ["_"] * len(word)

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_wrong - wrong_guesses)

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The correct word was:", word)