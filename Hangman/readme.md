Hangman: A Classic Word Guessing Game in Python

This repository contains a Python implementation of the classic word-guessing game, Hangman. The game is built with a modular approach, using functions, loops, and conditional statements to create an engaging command-line experience. It features ASCII art to visualize the hangman's stages, making the game more interactive and fun.

🌟 Features

Random Word Generation: Selects a random English word for each new game using the english_words library.

Word Constraint & Hint: The game ensures the selected word is no longer than 8 letters and gives the player the first letter as a helpful hint.

Interactive Gameplay: Players guess letters one by one to uncover the secret word.

Visual Feedback: Uses ASCII art to display the hangman at different stages, corresponding to the number of incorrect guesses.

Delayed Output: Leverages Python's time library to create dramatic pauses, enhancing the user experience.

Modular Code: The logic is separated into different local modules for better organization and readability (input_word.py and placeholder.py).

📂 Project Structure

Hangman/
├── hangman.py         # Main script to run the game
├── input_word.py      # Module to fetch a random word
└── placeholder.py     # Module to process the word and create the placeholder


🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites

Python 3.x installed on your system.

Installation & Setup

Clone the repository:

git clone [https://github.com/mahi-8758/Python-DEv.git](https://github.com/mahi-8758/Python-DEv.git)
cd Python-DEv/Hangman


Create a virtual environment:
It's recommended to create a virtual environment to manage project-specific dependencies.

On Windows:

python -m venv venv
venv\Scripts\activate


On macOS/Linux:

python3 -m venv venv
source venv/bin/activate


Install the required library:
This project requires the english_words library. Install it using pip:

pip install english_words


🎮 How to Play

Once you have completed the setup, run the main game file from your terminal:

python hangman.py


The game will start, and you can begin guessing letters to find the secret word!

Connect with Me

Feel free to reach out if you have any questions or suggestions!

GitHub: [@mahi-8758](https://github.com/mahi-8758)

LinkedIn: https://www.linkedin.com/in/mahikumar1926/

Made with ❤️ by Mahi Kumar