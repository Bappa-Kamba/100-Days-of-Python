from tkinter import *
from os import path

image_path = path.abspath('DAY-28/tomato.png')

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 30, "bold")
TIMER_FONT = ("Courier", 50, "normal")
WORK_MIN = 0.12
SHORT_BREAK_MIN = 0.12
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    image_canvas.itemconfig(timer_text, text=f"{0:02}:{0:02}")
    timer_label.config(text="Timer", font=TIMER_FONT, bg=YELLOW, fg=GREEN)
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_secs)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(int(short_break_secs))
    else:
        timer_label.config(text="Work!", fg=GREEN)
        count_down(int(work_secs))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):

    minutes = time // 60
    seconds = time % 60

    image_canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        start_timer()
        global marks
        work_sessions = reps // 2
        marks = ""
        for _ in range(work_sessions):
            marks += "✅"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label()
timer_label.config(text="Timer", font=TIMER_FONT, bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=0)


image_canvas = Canvas(width=300, height=300, highlightthickness=0, bg=YELLOW)
tomato_image = PhotoImage(file=image_path)
image_canvas.create_image(150, 150, image=tomato_image)
timer_text = image_canvas.create_text(155, 170, text="00:00", font=FONT, fill="white")
image_canvas.grid(column=2, row=1)

start_button = Button()
start_button.config(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=2)


reset_button = Button()
reset_button.config(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=3, row=2)

checkmarks = Label()
checkmarks.config(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=2, row=3)


window.mainloop()
