import google.generativeai as genai
import api
import sys
import time
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

api_keyai = api.API_KEY

genai.configure(api_key=api_keyai)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

def print_slow(text, color=Fore.WHITE, delay=0.03):
    """Print text with a typing effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def print_banner():
    """Print welcome banner"""
    banner = """
    ╔═══════════════════════════════════════╗
    ║     QUIZ AI - GOOGLE GEMINI 2.0       ║
    ║     Type 'exit' to quit               ║
    ╚═══════════════════════════════════════╝
    """
    print(Fore.CYAN + Style.BRIGHT + banner)
    time.sleep(0.5)

# Clear screen and show banner
print("\033[H\033[J")  # Clear screen
print_banner()

while True:
    # User prompt with color
    sys.stdout.write(Fore.GREEN + Style.BRIGHT + "You: " + Style.RESET_ALL)
    sys.stdout.flush()
    user_input = input()
    
    if user_input.lower() == "exit":
        print_slow("\n👋 Thank you for using Quiz AI! Goodbye!", Fore.YELLOW, 0.02)
        time.sleep(0.5)
        break
    
    if not user_input.strip():
        print(Fore.RED + "⚠ Please enter a message!" + Style.RESET_ALL)
        continue
    
    # Show thinking animation
    sys.stdout.write(Fore.MAGENTA + "🤔 AI is thinking")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")
    
    try:
        response = chat.send_message(user_input)
        print(Fore.CYAN + Style.BRIGHT + "AI: " + Style.RESET_ALL, end="")
        print_slow(response.text, Fore.CYAN, 0.01)
        print("\n" + Fore.YELLOW + "─" * 50 + Style.RESET_ALL + "\n")
    except Exception as e:
        print(Fore.RED + f"❌ Error: {str(e)}" + Style.RESET_ALL)
    
    time.sleep(0.2)

