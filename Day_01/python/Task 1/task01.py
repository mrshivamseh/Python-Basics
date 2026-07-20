import random

# 1. Predefined word list
words = ["python", "hangman", "security", "coding", "project"]

# 2. Randomly choose a word
word = random.choice(words)
guessed_letters = []
attempts = 6

# 3. Game loop
while attempts > 0:
    # Display current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("Word:", display_word)

    # Check if word is fully guessed
    if display_word == word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Player input
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        print("✅ Correct guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        attempts -= 1
        guessed_letters.append(guess)
        print("Attempts left:", attempts)

# 4. End game
if attempts == 0:
    print("Game Over! The word was:", word)
