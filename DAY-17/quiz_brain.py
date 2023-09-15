class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    
    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            return False
        return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").lower()
        self.check_answer(user_answer, current_question.answer.lower())

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You're correct! :-)")
            self.score += 1
            
        else:
            print("You got it wrong :-(")
        
        print(f"The correct answer is {correct_answer}")
        print(f"You're score is {self.score}/{self.question_number}")
        print()