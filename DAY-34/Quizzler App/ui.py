from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"

wait = NONE


class QuizUI():

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)

        self.score_text = Label(text=f"Score:{self.quiz.score}", font=(FONT_NAME, 14))
        self.score_text.config(fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Question Text",
            font=(FONT_NAME, 20, "italic"), 
            fill=THEME_COLOR,
            width=280
            
        ) 
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)   

        true_image = PhotoImage(file="DAY-34\\Quizzler App\\images\\true.png")
        false_image = PhotoImage(file="DAY-34\\Quizzler App\\images\\false.png") 

        self.true_button = Button(command=self.check_true)
        self.true_button.config(image=true_image, highlightthickness=0, bg=THEME_COLOR) 
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(command=self.check_false)
        self.false_button.config(image=false_image, highlightthickness=0, bg=THEME_COLOR) 
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("true"))
        if not self.quiz.still_has_questions():
            self.window.after(3000, self.window.quit)


    def check_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
        if not self.quiz.still_has_questions():
            self.window.after(3000, self.window.quit)

    def give_feedback(self, is_correct):
        global wait
        if is_correct:
            self.score_text.config(text=f"Score:{self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)