from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Questions(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions(): 
    quiz.next_question()
    

if quiz.still_has_questions() == False:
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")