# The Quiz Game

A command-line based trivia quiz application built in Python that tests your knowledge with True/False questions.

## Features

- **Interactive Quiz**: Answer a series of True/False questions in the terminal
- **Score Tracking**: Keep track of your score throughout the quiz
- **Answer Validation**: Immediate feedback on whether your answer is correct or incorrect
- **Question Bank**: Pre-loaded with 12 interesting trivia questions

## Project Structure

- **`main.py`**: Entry point of the application that initializes and runs the quiz
- **`data.py`**: Contains the question data as a list of dictionaries
- **`question_model.py`**: Defines the `Questions` class to structure individual questions
- **`quiz_brain.py`**: Contains the `QuizBrain` class that manages quiz logic and scoring

## How It Works

1. Questions are loaded from `data.py` and converted into `Questions` objects
2. The `QuizBrain` class manages the quiz flow, including:
   - Displaying questions one at a time
   - Checking user answers against correct answers
   - Maintaining and displaying the running score
3. The quiz continues until all questions are answered
4. A final score is displayed at the end

## How to Run

```bash
python main.py
```

Answer each question with `True` or `False` and press Enter.

## Example Output

```
Q.1: A slug's blood is green. (True/False)? True
You got it right!
Your current score is: 1/1
```