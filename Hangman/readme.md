# 🪓 HANGMAN 🎯  
*A fun and interactive word guessing game built with Python.*

## 🧩 Overview  
**HANGMAN** is a command-line based game created using Python.  
In this project, the player has to guess a hidden word, letter by letter, before the ASCII hangman figure is fully drawn!  

This project uses:
- The **`english_words`** external library to select random English words.
- Two **local Python modules**:
  - **`input_word.py`** — fetches a random word from `english_words`.
  - **`placeholder.py`** — checks the word length, provides a hint with the first letter, and warns if the word length exceeds 8 letters.

The **`hangman.py`** file integrates all these components using **functions**, **loops**, and **conditional statements**, along with **ASCII visualization** of the hangman stages.  
The **`time`** library is used to add delays for better user experience and visual appeal.

---

## 🛠️ Features  
✅ Random English word generation using `english_words`  
✅ Word length validation and automatic hint generation  
✅ ASCII art visualization of hangman stages  
✅ Step-by-step game progress display with delay effects  
✅ Modular structure using local and external libraries  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/mahi-8758/Python-DEv.git
cd Python-DEv/Hangman
````

### 2️⃣ Create a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the environment:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Required Library

Use pip to install the external dependency:

```bash
pip install english_words
```

### 4️⃣ Run the Game

Once everything is set up, start the game by running:

```bash
python hangman.py
```

---
---
## 📁 Project Structure

```
Hangman/
│
├── hangman.py           # Main game file
├── input_word.py        # Local module for random word input
├── placeholder.py       # Local module for word validation and hint
└── README.md            # Project documentation
```

---
---
## 🎮 How the Game Works

1. The game randomly selects a word from the `english_words` library.
2. The player guesses one letter at a time.
3. The hangman figure updates with each wrong guess.
4. The player wins if they guess all the letters before the figure is complete.

---

## 🧠 Concepts Used

* **Functions & Modular Programming**
* **Loops and Conditional Statements**
* **ASCII Art Rendering**
* **Time Delays for Visualization**
* **External and Local Library Integration**

---

## 🌐 Connect with Me

👨‍💻 **GitHub:** [mahi-8758](https://github.com/mahi-8758)
💼 **LinkedIn:** [Mahi Kumar](https://www.linkedin.com/in/mahikumar1926/)

---

## 📜 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

### ⭐ If you like this project, don’t forget to **star** the repo!

👉 [HANGMAN on GitHub](https://github.com/mahi-8758/Python-DEv/tree/main/Hangman)



