import random
import time
from colorama import Fore, Style, init
import art  # Assuming 'art' is a local library with 'art.logo'

# --- Setup & Constants ---

# Initialize Colorama to auto-reset styles after each print
init(autoreset=True)

art_logo = art.logo

# Define the deck of cards (11 is Ace)
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# --- Core Game Functions ---

def deal_card():
    """Returns a single random card from the deck."""
    return random.choice(CARDS)

def calculate_score(cards):
    """
    Calculates the score of a given hand.
    Handles the Ace (11 or 1) logic.
    """
    score = sum(cards)
    
    # This loop handles Aces. If the score is over 21 and there's an 11,
    # it changes the first 11 it finds to a 1 and recalculates.
    while score > 21 and 11 in cards:
        # Find the position of the Ace (11) and replace it with a 1
        ace_index = cards.index(11)
        cards[ace_index] = 1
        # Recalculate the score
        score = sum(cards)
        
    return score

def compare_scores(player_score, dealer_score, player_cards, dealer_cards):
    """Compares the final scores and prints the winner."""
    
    print(Fore.MAGENTA + Style.BRIGHT) # Set color for the result
    time.sleep(2) # Dramatic pause!

    # Check for Blackjack (2-card 21)
    player_bj = (player_score == 21 and len(player_cards) == 2)
    dealer_bj = (dealer_score == 21 and len(dealer_cards) == 2)

    if player_bj and dealer_bj:
        print("It's a draw! Both have Blackjack! 😐")
    elif player_bj:
        print("You have Blackjack! Player wins! 🥳")
    elif dealer_bj:
        print("Dealer has Blackjack! Dealer wins! 😭")
    # Check for busts
    elif player_score > 21:
        print("Player busts! Dealer wins! 😭")
    elif dealer_score > 21:
        print("Dealer busts! Player wins! 🥳")
    # Compare scores if no one busted
    elif player_score > dealer_score:
        print("Player wins! 🥳")
    elif dealer_score > player_score:
        print("Dealer wins! 😭")
    elif player_score == dealer_score:
        print("It's a draw! 😐")

# --- Main Game Round Function ---

def play_round():
    """Plays a single round of Blackjack."""
    
    print(Fore.GREEN + art_logo)
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Blackjack table!")
    print("---------------------------------")
    time.sleep(1)

    # Initialize empty hands
    card_player = []
    card_dealer = []
    
    # Deal initial hands
    for _ in range(2):
        card_player.append(deal_card())
        card_dealer.append(deal_card())
    
    # --- Player's Turn ---
    is_player_done = False
    
    while not is_player_done:
        # Calculate score *inside* the loop to account for new cards
        sum_player = calculate_score(card_player)
        sum_dealer = calculate_score(card_dealer) # Calculate dealer score but don't show it

        print(Fore.YELLOW + f"Your cards are: {card_player}, with total Score {sum_player}")
        time.sleep(0.5)
        print(Fore.RED + f"Dealer's first card is: {card_dealer[0]}")
        time.sleep(0.5)

        # Check if player has bust or got 21
        if sum_player >= 21:
            is_player_done = True # Automatically stand if 21 or bust
            if sum_player == 21:
                print(Fore.GREEN + "21! You stand.")
            else:
                print(Fore.RED + "Bust! You lose this hand.")
        else:
            # Ask player to hit or stand
            print("---------------------------------")
            condition = input(Fore.WHITE + "Type 'y' to get another card (hit), type 'n' to pass (stand): ").lower()
            
            if condition == 'y':
                print(Fore.YELLOW + "You draw another card...")
                time.sleep(1)
                card_player.append(deal_card())
            else:
                print(Fore.CYAN + "You stand.")
                is_player_done = True
        
        time.sleep(1)

    # --- Dealer's Turn ---
    # Player's turn is over, now the dealer plays.
    # Recalculate final player score one last time
    sum_player = calculate_score(card_player)
    sum_dealer = calculate_score(card_dealer)

    print("\n" + Fore.CYAN + "Dealer's turn...")
    time.sleep(1)
    
    # Reveal dealer's full hand
    print(Fore.RED + f"Dealer's hidden hand was: {card_dealer}, total Score {sum_dealer}")
    time.sleep(1.5)

    # Dealer must hit on 16 or less (standard Blackjack rule)
    while sum_dealer < 18:
        print(Fore.RED + "Dealer's score is less than 17, so dealer gets another card.")
        time.sleep(1)
        card_dealer.append(deal_card())
        sum_dealer = calculate_score(card_dealer) # Recalculate with new card (and Ace logic)
        print(Fore.RED + f"Dealer's new hand: {card_dealer}, total Score {sum_dealer}")
        time.sleep(1.5)
    
    if sum_dealer >= 17 and sum_dealer <= 21:
        print(Fore.CYAN + "Dealer stands.")
    elif sum_dealer > 21:
        print(Fore.GREEN + "Dealer busts!")

    # --- Final Results ---
    print("\n" + Style.BRIGHT + "--- FINAL RESULTS ---")
    time.sleep(1.5)

    print(Fore.YELLOW + Style.BRIGHT + f"Final cards of player are: {card_player}, with total Score {sum_player}")
    time.sleep(1)
    print(Fore.RED + Style.BRIGHT + f"Final cards of dealer are: {card_dealer}, with total Score {sum_dealer}")
    
    # Call the compare function
    compare_scores(sum_player, sum_dealer, card_player, card_dealer)


# --- Main Program Loop ---

def main():
    """Main function to run the game and handle 'play again' logic."""
    while True:
        play_round() # This function now contains one full game
        
        print(Style.RESET_ALL + "---------------------------------")
        time.sleep(1)
        
        play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            break # Exit the while loop
    
    print(Fore.CYAN + "Thanks for playing! Goodbye!")


# This makes the script runnable
if __name__ == "__main__":
    main()