from tkinter import *

FONT = ('Tahoma', 12, 'normal')

focus_label = NONE

def convert_miles():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_input.delete(0, END)
    km_input.insert(END, km)

def convert_km():
    km = float(miles_input.get())
    miles = round(km / 1.609, 2)
    km_input.delete(0, END)
    km_input.insert(END, miles)
    
def switch():
    global focus_label

    miles = miles_label.grid_info()
    km = km_label.grid_info()

    miles_label.grid(column=km['column'], row=km['row'])
    km_label.grid(column=miles['column'], row=miles['row'])
    km_input.delete(0, END)

    if miles['row'] > km['row']:
        focus_label = miles_label
    else:
        focus_label = km_label

def calculate_conversion():
    if focus_label == miles_label or focus_label is NONE:
        convert_miles()
        print("miles")
    elif focus_label == km_label:
        convert_km() 
        print("km")

window = Tk()
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

miles_input =  Entry(width=10)
miles_input.grid(column=2, row=1)

miles_label = Label(text='Miles', font=FONT)
miles_label.config(padx=10)
miles_label.grid(column=3, row=1)

switch_button = Button(text="Switch", command=switch)
switch_button.grid(column=2, row=2)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=1, row=3)


km_input =  Entry(width=10)
km_input.grid(column=2, row=3)

km_label = Label(text='Km', font=FONT)
km_label.config(padx=10)
km_label.grid(column=3, row=3)

calc_button = Button(text="Convert", command=calculate_conversion)
calc_button.grid(column=2, row=4)


window.mainloop()