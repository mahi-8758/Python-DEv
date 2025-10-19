import random

# ASCII Art for game title
print("""
    ____            _      ____                       
   / ___| ___  ___| | __ |  _ \ __ _ _ __   ___ _ __ 
   \___ \/ __|/ _ \ |/ / | |_) / _` | '_ \ / _ \ '__|
    ___) \__ \  __/   <  |  __/ (_| | |_) |  __/ |   
   |____/|___/\___|_|\_\ |_|   \__,_| .__/ \___|_|   
                                     |_|    
   ____       _                         
  / ___|  ___(_)___ ___  ___  _ __ ___ 
  \___ \ / __| / __/ __|/ _ \| '__/ __|
   ___) | (__| \__ \__ \ (_) | |  \__ \\
  |____/ \___|_|___/___/\___/|_|  |___/
""")

print("Welcome to Stone Paper Scissors!")
print("Enter your choice: stone, paper, or scissors")

# ASCII Art for choices
STONE = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = ["stone", "paper", "scissors"]
visuals = {"stone": STONE, "paper": PAPER, "scissors": SCISSORS}
computer_score = 0
player_score = 0

while True:
    player = input("\nYour turn: ").lower()
    if player not in choices:
        print("Invalid choice! Please choose stone, paper, or scissors")
        continue
        
    computer = random.choice(choices)
    
    # Display visual choices
    print(f"\nYour choice:")
    print(visuals[player])
    print(f"Computer chose:")
    print(visuals[computer])

    if player == computer:
        print("It's a tie! 🤝")
    elif player == "stone":
        if computer == "paper":
            print("You lose! 😢")
            computer_score += 1
        else:
            print("You win! 🎉")
            player_score += 1
    elif player == "paper":
        if computer == "scissors":
            print("You lose! 😢")
            computer_score += 1
        else:
            print("You win! 🎉")
            player_score += 1
    elif player == "scissors":
        if computer == "stone":
            print("You lose! 😢")
            computer_score += 1
        else:
            print("You win! 🎉")
            player_score += 1
            
    print(f"\nScores - You: {player_score} 👤, Computer: {computer_score} 🤖")
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("""
        Thanks for playing!
        
        Game Over
        ╔═══╗────╔╗
        ║╔═╗║────║║
        ║║─╚╬══╦═╝╠══╦═╗
        ║║╔═╣╔╗║╔╗║║═╣╔╝
        ║╚╩═║╚╝║╚╝║║═╣║
        ╚═══╩══╩══╩══╩╝
        """)
        break