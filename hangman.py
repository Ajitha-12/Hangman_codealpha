import random
easy_words = ["cat", "dog", "book", "tree", "fish","easy"]
medium_words = ["python", "planet", "flower", "window", "school","medium"]
hard_words = ["hangman", "developer", "challenge", "difficult", "algorithm"]
def get_valid_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in guessed_letters:
            print("🔁You already guessed that letter.")
        else:
            return guess
def choose_difficulty():
    print("🎮Choose difficulty: easy / medium / hard")
    while True:
        level = input("Enter difficulty level: ").lower()
        if level == "easy":
            return random.choice(easy_words)
        elif level == "medium":
            return random.choice(medium_words)
        elif level == "hard":
            return random.choice(hard_words)
        else:
            print("❌ Invalid input. Please choose: easy / medium / hard.")
def play_hangman():
    word = choose_difficulty()
    guessed_letters = []
    correct_letters = ["_" for _ in word]
    attempts = 6
    print("\n🎯 Let's start the Hangman Game!")
    print("🔤 Guess the word, one letter at a time.")
    print("You have 6 incorrect guesses.\n")
    while attempts > 0 and "_" in correct_letters:
        print("Word:", " ".join(correct_letters))
        print("Guessed letters:", ", ".join(guessed_letters))
        print(f"❗Remaining incorrect attempts: {attempts}")
        guess = get_valid_letter(guessed_letters)
        guessed_letters.append(guess)
        if guess in word:
            print("✅Congratulations,Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    correct_letters[i] = guess
        else:
            print("❌Try again!Wrong guess!")
            attempts -= 1
        print("-" * 30)
    if "_" not in correct_letters:
        print("🎉Congratulations! You guessed the word:", word)
    else:
        print("💀Game Over! The word was:", word)
play_hangman()
