from data import question_data
from data_1 import question_data_1
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# for question in question_data:
for question in question_data_1:
    # question_text = question["text"]
    # question_answer = question["answer"]

    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
