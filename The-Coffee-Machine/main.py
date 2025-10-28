import menu
import time
import sys
from colorama import Fore, Back, Style, init
from coffee_art import coffee_machine, coffee_cup

# Initialize colorama with all options
init(autoreset=True, convert=True, strip=False)

def print_slow(text, delay=0.03):
    """Print text with typewriter effect and proper color handling"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Style.RESET_ALL)
    print()

def clean_print(color, text):
    """Print colored text with proper reset"""
    sys.stdout.write(f"{color}{text}{Style.RESET_ALL}\n")
    sys.stdout.flush()

def get_input(color, prompt):
    """Get user input with colored prompt"""
    sys.stdout.write(f"{color}{prompt}{Style.RESET_ALL}")
    sys.stdout.flush()
    return input()

def money():
    clean_print(Fore.YELLOW, "\nPlease insert coins.")
    total = float(get_input(Fore.GREEN, "How many Dollars?: "))
    total += float(get_input(Fore.GREEN, "How many quarters?: ")) * 0.25
    total += float(get_input(Fore.GREEN, "How many dimes?: ")) * 0.10
    total += float(get_input(Fore.GREEN, "How many nickels?: ")) * 0.05
    total += float(get_input(Fore.GREEN, "How many pennies?: ")) * 0.01
    return total

def process_payment(cost, money_inserted):
    if money_inserted >= cost:
        change = money_inserted - cost
        if change > 0:
            clean_print(Fore.GREEN, f"\nHere is ${change:.2f} in change.")
        time.sleep(1)
        print_slow(f"{Fore.CYAN}Preparing your coffee... ☕")
        time.sleep(1.5)
        clean_print(Fore.WHITE, coffee_cup)
        print_slow(f"{Fore.LIGHTGREEN_EX}Enjoy your Coffee! ✨")
        clean_print(Fore.YELLOW, "Thank you for your purchase! 🙏")
        return True
    else:
        clean_print(Fore.RED, "\nSorry, that's not enough money. Money refunded.")
        return False

def report(water, milk, coffee, money):
    clean_print(Fore.CYAN, "\n=== MACHINE STATUS ===")
    clean_print(Fore.BLUE, f"Water: {water}ml 💧")
    clean_print(Fore.WHITE, f"Milk: {milk}ml 🥛")
    clean_print(Fore.YELLOW, f"Coffee: {coffee}g ☕")
    clean_print(Fore.GREEN, f"Money: ${money} 💰")
    clean_print(Fore.CYAN, "===================\n")

def main():
    latte_cost = menu.MENU['latte']['cost']
    cappuccino_cost = menu.MENU['cappuccino']['cost']
    espresso_cost = menu.MENU['espresso']['cost']

    main_water = 500
    main_milk = 400
    main_coffee = 200
    main_money = 0

    clean_print(Fore.CYAN, coffee_machine)
    print_slow(f"{Fore.YELLOW}Welcome to the Coffee Machine! ☕")
    time.sleep(1)

    run = True
    while run:
        clean_print(Fore.MAGENTA, "\n" + "=" * 50)
        print_slow(f"{Fore.CYAN}What would you like to have? (espresso/latte/cappuccino)")
        choice = get_input(Fore.WHITE, ">>> ").lower()

        if choice == "espresso":
            cost = espresso_cost
            if main_water > menu.MENU['espresso']['ingredients']['water'] and main_coffee > menu.MENU['espresso']['ingredients']['coffee'] and main_milk > menu.MENU['espresso']['ingredients']['water']:
                clean_print(Fore.YELLOW, f"The cost of an espresso is ${cost:.2f}.")
                money_inserted = money()

                if process_payment(cost, money_inserted):
                    main_water -= menu.MENU['espresso']['ingredients']['water']
                    main_milk -= menu.MENU['espresso']['ingredients']['milk']
                    main_coffee -= menu.MENU['espresso']['ingredients']['coffee']
                    main_money += cost
            else:
                clean_print(Fore.RED, "Not Enough Supplies")

        elif choice == "latte":
            cost = latte_cost
            if main_water > menu.MENU['latte']['ingredients']['water'] and main_coffee > menu.MENU['latte']['ingredients']['coffee'] and main_milk > menu.MENU['latte']['ingredients']['water']:
                clean_print(Fore.YELLOW, f"The cost of a latte is ${cost:.2f}.")
                money_inserted = money()

                if process_payment(cost, money_inserted):
                    main_water -= menu.MENU['latte']['ingredients']['water']
                    main_milk -= menu.MENU['latte']['ingredients']['milk']
                    main_coffee -= menu.MENU['latte']['ingredients']['coffee']
                    main_money += cost
            else:
                print("Not Enough Supplies")

        elif choice == "cappuccino":
            cost = cappuccino_cost
            if main_water > menu.MENU['cappuccino']['ingredients']['water'] and main_coffee > menu.MENU['cappuccino']['ingredients']['coffee'] and main_milk > menu.MENU['cappuccino']['ingredients']['water']:
                print(f"The cost of a cappuccino is ${cost:.2f}.")
                money_inserted = money()

                if process_payment(cost, money_inserted):
                    main_water -= menu.MENU['cappuccino']['ingredients']['water']
                    main_milk -= menu.MENU['cappuccino']['ingredients']['milk']
                    main_coffee -= menu.MENU['cappuccino']['ingredients']['coffee']
                    main_money += cost
            else:
                print("Not Enough Supplies")

        elif choice == 'report':
            report(main_water,main_milk,main_coffee,main_money)
            continue

        elif choice == 'refill':
            clean_print(Fore.YELLOW, "=== REFILL MODE ===")
            main_milk += float(get_input(Fore.WHITE, "Amount of Milk: "))
            main_water += float(get_input(Fore.WHITE, "Amount of Water: "))
            main_coffee += float(get_input(Fore.WHITE, "Amount of coffee: "))
            report(main_water, main_milk, main_coffee, main_money)

        elif choice == 'off':
            print_slow(f"{Fore.RED}Shutting down... 🔌")
            time.sleep(1)
            print_slow(f"{Fore.YELLOW}Thank you for using our coffee machine! 👋")
            run = False
        else:
            clean_print(Fore.RED, "\nInvalid choice. Please select espresso, latte, cappuccino, report, refill, or off.")

if __name__ == "__main__":
    main()




