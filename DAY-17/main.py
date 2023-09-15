from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(
        Question(text=data["text"], answer=data["answer"])
    )

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your score was {quiz_brain.score}/{len(quiz_brain.question_list)}.")