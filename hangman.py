import random

# Word list
words = {
    "Animals": ["tiger", "elephant", "lion", "giraffe", "monkey"],
    "Food": ["pizza", "burger", "biryani", "sandwich", "pancake"],
    "Places": ["india", "paris", "london", "tokyo", "dubai"],
    "Technology": ["python", "computer", "keyboard", "internet", "robot"]
}

# Hangman drawings
hangman = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]


score = 0

print("================================")
print("       🎮 HANGMAN GAME 🎮")
print("================================")

while True:

    # Pick random category
    category = random.choice(list(words.keys()))

    # Pick random word
    word = random.choice(words[category])

    guessed = []
    wrong = 0
    hint_used = False

    print("\nCategory:", category)
    print("💡 Type 'hint' if you need help!")
    print("❤️ You have 6 lives.")

    while wrong < 6:

        # Display hangman
        print(hangman[wrong])

        # Display word
        print("Word: ", end="")

        for letter in word:
            if letter in guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        print()
        print("❤️ Lives left:", 6 - wrong)

        # Take guess
        guess = input("Guess a letter: ").lower()

        # Hint
        if guess == "hint":

            if hint_used:
                print("😅 You already used your hint!")
            else:
                for letter in word:
                    if letter not in guessed:
                        print("💡 Hint: The word contains the letter", letter)
                        hint_used = True
                        break

            continue

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only ONE letter!")
            continue

        # Check repeated guess
        if guess in guessed:
            print("😅 You already guessed that letter!")
            continue

        guessed.append(guess)

        # Correct guess
        if guess in word:
            print("🎉 Correct!")

        # Wrong guess
        else:
            wrong += 1
            print("❌ Wrong guess!")

        # Check if word is completed
        complete = True

        for letter in word:
            if letter not in guessed:
                complete = False

        if complete:
            print("\n🎉🎉 YOU WON! 🎉🎉")
            print("The word was:", word)

            score += 10
            print("🏆 Score:", score)

            break

    # Player loses
    if wrong == 6:
        print(hangman[6])
        print("\n💀 GAME OVER!")
        print("The word was:", word)
        print("🏆 Score:", score)

    # Play again
    again = input("\n🔄 Play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing! 👋")
        print("Final Score:", score)
        break