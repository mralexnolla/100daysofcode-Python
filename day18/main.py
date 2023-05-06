from question_model import Question
from data import question_data
from quizz_brain import QuizzBrain

Question_bank = []

for question in question_data:
    quest_text = question["text"]
    quest_answer = question["answer"]
    new_question = Question(quest_text, quest_answer)
    Question_bank.append(new_question)

quiz = QuizzBrain(Question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quizz ")
print("Your final score was f{}")
