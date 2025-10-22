import art
logo1 = art.logo

import time
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def animate_text(text, color=Fore.WHITE, delay=0.002):
    for ch in text:
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        time.sleep(delay)
    if not text.endswith("\n"):
        print(Style.RESET_ALL)

animate_text(logo1, Fore.CYAN, 0.0005)
animate_text("Welcome to the Biding Game\n\n", Fore.YELLOW, 0.01)

bids = {}
continue_bidding = True
while continue_bidding:
    name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    bid_amount = int(input(Fore.GREEN + "Enter your bid amount: $" + Style.RESET_ALL))
    bids[name] = bid_amount
    animate_text(f"Thanks {name}! Your bid of ${bid_amount} has been recorded.\n", Fore.CYAN, 0.01)
    more_bidders = input(Fore.YELLOW + "Are there any other bidders? Type 'yes' or 'no': " + Style.RESET_ALL).lower()
    if more_bidders == 'no':
        continue_bidding = False
        break
    if more_bidders == 'yes':
        continue_bidding = True
        print("\n" * 50)
        animate_text(logo1, Fore.CYAN, 0.0005)

bidder = max(bids, key=bids.get)
animate_text("\nCalculating the highest bid", Fore.MAGENTA, 0.03)
for _ in range(6):
    sys.stdout.write(Fore.MAGENTA + ".")
    sys.stdout.flush()
    time.sleep(0.35)
print()
animate_text(f"\nThe winner is ", Fore.YELLOW, 0.03)
animate_text(f"{bidder}", Fore.GREEN + Style.BRIGHT, 0.06)
animate_text(f" with a bid of ${bids[bidder]}\n", Fore.YELLOW, 0.03)
animate_text("\nThanks for playing! 🎉\n", Fore.CYAN, 0.01)