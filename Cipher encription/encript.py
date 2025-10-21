import string
import art
import time
import sys
from colorama import Fore, Style, Back, init
from threading import Thread

init()  # Initialize colorama

def print_slow(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def loading_animation():
    symbols = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    colors = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA]
    for _ in range(3):
        for symbol in symbols:
            for color in colors:
                sys.stdout.write(f'\r{color}Processing {symbol} {Style.RESET_ALL}')
                sys.stdout.flush()
                time.sleep(0.05)
    print()

def show_shift_visualization(shift):
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    print(f"\n{Fore.CYAN}Shift Visualization:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{alphabet}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'↓' * 26}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{shifted}{Style.RESET_ALL}\n")

def ceasar(direction):
    print(f"\n{Fore.YELLOW}{'═'*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[{direction.upper()}TION MODE]{Style.RESET_ALL}".center(50))
    print(f"{Fore.YELLOW}{'═'*50}{Style.RESET_ALL}")
    
    input_word = input(f"{Fore.GREEN}📝 Enter the words to {direction}: {Style.RESET_ALL}")
    shift = int(input(f"{Fore.GREEN}🔄 Enter the shift number: {Style.RESET_ALL}"))
    
    if direction == "decript":
        shift *= -1
    
    show_shift_visualization(shift % 26)
    
    x = string.ascii_lowercase
    x_index = list(x)
    print(f"\n{Fore.CYAN}🔄 Converting", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(f"{Fore.YELLOW}➤{Style.RESET_ALL}", end="", flush=True)
    print(f"{Style.RESET_ALL}\n")
    
    loading_animation()
    print(f"{Back.BLACK}{Fore.WHITE}Result:{Style.RESET_ALL} ", end="")
    
    result = ""
    for letter in input_word:
        if letter not in x_index:
            result += letter
        else:
            position = x_index.index(letter)
            new_position = (position + shift)
            wordnew = x_index[new_position % 26]
            result += wordnew
    
    print(f"{Fore.YELLOW}{result}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'═'*50}{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}{art.logo}{Style.RESET_ALL}")
    print_slow(f"{Back.BLACK}{Fore.GREEN}🔐 Welcome to Cipher Encryption & Decryption 🔐{Style.RESET_ALL}")
    print_slow(f"{Fore.YELLOW}✨ Your Secret Message Keeper ✨{Style.RESET_ALL}")
    
    answer = True
    while True:
        if not answer:
            print_slow(f"\n{Back.RED}{Fore.WHITE}🔒 Session Ended - Goodbye! 🔒{Style.RESET_ALL}")
            break
            
        print(f"\n{Fore.CYAN}{'─'*50}{Style.RESET_ALL}")
        direction = input(f"{Fore.MAGENTA}Choose your operation:\n"
                        f"1. Type 'encript' 🔒 (Lock your message)\n"
                        f"2. Type 'decript' 🔓 (Unlock your message)\n"
                        f"Your choice: {Style.RESET_ALL}").lower()
        
        if direction in ["encript", "decript"]:
            ceasar(direction)
        else:
            print(f"{Back.RED}{Fore.WHITE}❌ Invalid input. Please type 'encript' or 'decript'.{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}{'─'*50}{Style.RESET_ALL}")
        restart = input(f"{Fore.GREEN}🔄 Another operation? (yes/no): {Style.RESET_ALL}").lower()
        answer = restart == "yes"

if __name__ == "__main__":
    main()