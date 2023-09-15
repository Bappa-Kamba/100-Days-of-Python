from tkinter import *

FONT = ('Courier', 30, 'normal')

def button_clicked():
    my_label['text'] = entry.get()

window = Tk()
window.title("My First GUI Program!")
window.minsize(width=500, height=300)

my_label = Label(text='I am a Label.', font=FONT)
my_label.grid(column=0, row=0)

button = Button(text='New Button')
button.grid(column=2, row=0)

my_button = Button(text='Click Me!', command=button_clicked)
my_button.grid(column=1, row=2)

entry = Entry(width=20)
entry.grid(column=4, row=4)



window.mainloop()

