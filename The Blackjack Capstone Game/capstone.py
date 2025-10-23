import random
import time
from colorama import Fore, Style, init
import art # Import directly as requested

art_logo = art.logo

# Initialize Colorama to auto-reset styles after each print
init(autoreset=True)

# --- Start of your original code, now with enhancements ---

print(Fore.GREEN + art_logo)
print(Fore.CYAN + Style.BRIGHT + "Welcome to the Blackjack table!")
print("---------------------------------")
time.sleep(1) # Added pause

card_player = []
card_dealer = []
for card in range(2):
    card_player.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
    card_dealer.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
    
sum_player = sum(card_player)
sum_dealer = sum(card_dealer)

print(Fore.YELLOW + "Your cards are: ", card_player, " with total Score", sum_player)
time.sleep(0.5) # Added pause
print(Fore.RED + "First card of dealer are: [⣾, ⡿]") # This was your original "hidden" print
time.sleep(0.5) # Added pause

move_forward = input("Type 'y' to continue, type 'n' to stop: ").lower()
print("---------------------------------") # Added spacer
play_game = True
while play_game:
    if move_forward == 'y':
        condition = 'y'
        if sum_player < 17:
            card_player.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
            sum_player = sum(card_player)
            print(Fore.YELLOW + "Score is less than 17, so you get another card.") # Added color
            time.sleep(1) # Added pause
            print(Fore.YELLOW + "Your cards are: ", card_player, " with total Score", sum_player) # Added color
            time.sleep(1) # Added pause

        elif sum_player >= 17 and sum_player < 21:
            condition = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            # This loop will now stop if condition is 'n' OR if the player busts
            while (condition == 'y'): 
                print(Fore.YELLOW + "You draw another card...") # Added flavor text
                time.sleep(1) # Added pause
                card_player.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
                sum_player = sum(card_player)
                print(Fore.YELLOW + "Your cards are: ", card_player, " with total Score", sum_player) # Added color
                time.sleep(1) # Added pause

                # --- THIS IS THE FIX --- (This was already in your provided code)
                # 1. Check if the player busted or got 21
                if sum_player >= 21:
                    condition = 'n' # Force the loop to stop
                else:
                    # 2. If not, ask again INSIDE the loop
                    condition = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        # --- Dealer's Turn ---
        print("\n" + Fore.CYAN + "Dealer's turn...") # Added header and spacing
        time.sleep(1) # Added pause

        if sum_dealer < 17:
            card_dealer.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
            sum_dealer = sum(card_dealer)
            print(Fore.RED + "Dealer's score is less than 17, so dealer gets another card.") # Added color
            time.sleep(1) # Added pause

        print(Fore.RED + "cards of dealer are: [⣾, ⡿, ⣾]") # Your original "hidden" print
        time.sleep(1) # Added pause

        # --- Final Results ---
        print("\n" + Style.BRIGHT + "--- FINAL RESULTS ---") # Added header
        time.sleep(1.5) # Added pause

        print(Fore.YELLOW + Style.BRIGHT + "Final cards of player are: ", card_player, " with total Score", sum_player) # Added color
        time.sleep(1) # Added pause
        print(Fore.RED + Style.BRIGHT + "Final cards of dealer are: ", card_dealer, " with total Score", sum_dealer) # Added color

        print(Fore.MAGENTA + Style.BRIGHT) # Set color for the result
        time.sleep(2) # Dramatic pause!

        if sum_player > sum_dealer and sum_player <= 21:
            print("Player wins! 🥳") # Added emoji
        elif sum_dealer > sum_player and sum_dealer <= 21:
            print("Dealer wins! 😭") # Added emoji
        elif sum_player > 21:
            print("Player busts! Dealer wins! 😭") # Added emoji
        elif sum_dealer > 21:
            print("Dealer busts! Player wins! 🥳") # Added emoji
        elif sum_player == sum_dealer:
            print("It's a draw! 😐") # Added emoji

        print(Style.RESET_ALL + "---------------------------------") # Added spacer
        time.sleep(1) # Added pause
        print(Fore.GREEN + art_logo) # Added color

    elif move_forward == 'n':
        print(Fore.CYAN + "You decided to walk away. See you next time!")

    else:
        if move_forward != 'y':
            print(Fore.CYAN + "See you next time!")

    play= input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play == 'y':
        play_game = True
        card_player = []
        card_dealer = []
        for card in range(2):
            card_player.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
            card_dealer.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
        print(Fore.YELLOW + "Your cards are: ", card_player, " with total Score", sum_player)
        time.sleep(0.5) # Added pause
        sum_player = sum(card_player)
        sum_dealer = sum(card_dealer)
        condition = 'y'
        if sum_player < 17:
            card_player.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
            sum_player = sum(card_player)
            print(Fore.YELLOW + "Score is less than 17, so you get another card.") # Added color
            time.sleep(1) # Added pause
            print(Fore.YELLOW + "Your cards are: ", card_player, " with total Score", sum_player) # Added color
            time.sleep(1) # Added pause

        elif sum_player >= 17 and sum_player < 21:
            condition = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            # This loop will now stop if condition is 'n' OR if the player busts
            while (condition == 'y'): 
                print(Fore.YELLOW + "You draw another card...") # Added flavor text
                time.sleep(1) # Added pause
                card_player.append(random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10]))
                sum_player = sum(card_player)
                print(Fore.YELLOW + "Your cards are: ", card_player, " with total Score", sum_player) # Added color
                time.sleep(1) # Added pause

                # --- THIS IS THE FIX --- (This was already in your provided code)
                # 1. Check if the player busted or got 21
                if sum_player >= 21:
                    condition = 'n' # Force the loop to stop
                else:
                    # 2. If not, ask again INSIDE the loop
                    condition = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    else:
        play_game = False
        print(Fore.CYAN + "Thanks for playing! Goodbye!")
