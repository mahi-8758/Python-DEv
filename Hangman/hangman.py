import input_word
import placeholder
import time  # For adding dramatic pauses

def print_slowly(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def play_hangman():
    stages = [
    # Stage 0 (Game Over - 0 lives left)
    r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """,
    # Stage 1 (1 life left)
    r"""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    # Stage 2 (2 lives left)
    r"""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    # Stage 3 (3 lives left)
    r"""
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # Stage 4 (4 lives left)
    r"""
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # Stage 5 (5 lives left)
    r"""
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    # Stage 6 (Initial state - 6 lives left)
    r"""
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
    ]
    # Get the word to guess from input_word module
    word = input_word.guessedword
    gameover = False
    correct_letter = []  # Store correctly guessed letters
    life = 6  # Total lives

    # Welcome screen
    print("\n" + "="*50)
    print_slowly("🎮 Welcome to HANGMAN - The Game of Life and Death! 💀")
    print("="*50 + "\n")

    while not gameover:
        print("\n" + "-"*30)
        print(f"❤️  Lives Remaining: {'❤️ ' * life}")
        print("-"*30)
        
        display = ""
        guesses = input("\n🎯 Make your guess (enter a letter): ").lower()
        
        if guesses not in word:
            life -= 1
            print("\n❌ Wrong guess!")
            print_slowly("The hangman draws closer to his fate...", 0.05)
            print(stages[life])
            
            if life == 0:
                print("\n" + "="*50)
                print_slowly("💀 GAME OVER - The hangman meets his end! 💀")
                print(f"📖 The word was: {word}")
                print("="*50)
                gameover = True
                continue

        # Update display
        for letter in word:
            if letter == guesses:
                display += letter
                if letter not in correct_letter:
                    correct_letter.append(letter)
            elif letter in correct_letter:
                display += letter
            else:
                display += "_"

        print(f"\n📝 Word Progress: {' '.join(display)}")

        if all(letter in correct_letter for letter in word):
            print("\n" + "="*50)
            print_slowly("🎉 CONGRATULATIONS! You've saved the hangman! 🎊")
            print_slowly("🏆 You're the CHAMPION! 🏆")
            print("="*50)
            gameover = True

# Game start
print("\n" + "*"*60)
print_slowly("🎯 THE HANGMAN GAME 🎯")
print("*"*60)
gamerun = input("\n🎮 Ready to play? (yes/no): ").strip().lower()

if gamerun == 'yes':
    play_hangman()
else:
    print("\n" + "-"*30)
    print_slowly("👋 Maybe next time then!")
    print_slowly("See you soon, brave player! 🌟")
    print("-"*30)