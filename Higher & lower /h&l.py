import art
import game_data
import random
import time
import sys
from colorama import Fore, Back, Style, init

logo_art = art.logo

# Initialize colorama with convert=True for Windows and autoreset=True
init(convert=True, autoreset=True)

# Add this function to clean text output
def clean_print(color, text):
    print(f"{color}{text}{Style.RESET_ALL}")

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def intro():
    clean_print(Fore.CYAN, "=" * 50)
    print_slow(f"{Fore.YELLOW}Welcome to the Higher & Lower game!{Style.RESET_ALL}", 0.05)
    clean_print(Fore.CYAN, "=" * 50)
    time.sleep(0.5)
    clean_print(Fore.LIGHTBLUE_EX, logo_art)
    time.sleep(1)
    print_slow(f"{Fore.MAGENTA}Try to guess which option has a higher value!{Style.RESET_ALL}", 0.05)

def choice(game_data):
    print(Fore.CYAN + "\n" + "=" * 50)
    time.sleep(0.5)
    a = random.choice(game_data.data)
    b = random.choice(game_data.data)
    
    print(Fore.GREEN + f"\nCompare A: {a['name']}", end="")
    print(Fore.WHITE + f", a {a['description']}", end="")
    print(Fore.YELLOW + f", from {a['country']}.")
    
    print(Fore.BLUE + art.vs)
    
    print(Fore.GREEN + f"Against B: {b['name']}", end="")
    print(Fore.WHITE + f", a {b['description']}", end="")
    print(Fore.YELLOW + f", from {b['country']}.")
    
    return a, b
    
def check_answer(a, b):
    print(Fore.CYAN + "\n" + "=" * 50)
    user_guess = input(Fore.LIGHTWHITE_EX + "\nWho has more followers? Type 'A' or 'B': ").lower()
    time.sleep(0.5)
    
    if user_guess == 'b':
        user_guess = b['follower_count']
    else:
        user_guess = a['follower_count']
        
    a_followers = a['follower_count']
    b_followers = b['follower_count']
    
    if a_followers > b_followers:
        if user_guess == a_followers:
            print_slow(Fore.LIGHTGREEN_EX + "🎉 You are right!", 0.05)
            return True
        else:
            print_slow(Fore.RED + "❌ You are wrong!", 0.05)
            return False
    else:
        if user_guess == b_followers:
            print_slow(Fore.LIGHTGREEN_EX + "🎉 You are right!", 0.05)
            return True
        else:
            print_slow(Fore.RED + "❌ You are wrong!", 0.05)
            return False

def game():
    intro()
    start = input(Fore.LIGHTWHITE_EX + "\nWanted to get Started - YES OR NO? ").lower()
    if start == "yes":
        print_slow(Fore.LIGHTGREEN_EX + "\n🎮 Let's Begin!", 0.05)
        score = 0
        game_should_continue = True
        while game_should_continue:
            a, b = choice(game_data)
            is_correct = check_answer(a, b)
            if is_correct:
                score += 1
                print_slow(Fore.YELLOW + f"\n🏆 Your current score is: {score}", 0.05)
                time.sleep(1)
            else:
                game_should_continue = False
                print_slow(Fore.RED + f"\n💔 Game over! Your final score is: {score}", 0.05)
    elif start == "no":
        print_slow(Fore.LIGHTBLUE_EX + "\n👋 Maybe next time!", 0.05)
        return False

def main():
    while True:
        result = game()
        if result is False:
            print_slow(Fore.CYAN + "\n🎮 Thanks for playing! Goodbye.", 0.05)
            break
            
        play_again = input(Fore.LIGHTWHITE_EX + "\nDo you want to play again? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            print_slow(Fore.CYAN + "\n🎮 Thanks for playing! Goodbye.", 0.05)
            break
        print("\n" * 50)
        time.sleep(1)

if __name__ == "__main__":
    main()










