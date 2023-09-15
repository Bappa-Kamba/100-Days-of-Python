from tkinter import *
from tkinter import messagebox
from generator import generate
import pyperclip
import json


filename = "DAY-29\\data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = generate()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website_name = website_entry.get().title()
    email = username_entry.get().lower()
    password = password_entry.get()

    data_dict = {
        website_name : {
            "email" : email,
            "password" : password,
        }
    }

    if len(website_name) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Blank Fields",
                            message="Please fill out all fields.")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered:\n\nEmail: {email}\nPassword: {password}\
                                        \nIs it ok to save?")
        if is_ok:

            try:
                with open(file=filename, mode="r") as file:
                    data = json.load(file)
                    print(data)
                    data.update(data_dict)
            except FileNotFoundError:
                with open(filename, mode='w') as file:
                    json.dump(data_dict, file, indent=4)
            else:                
                with open(file=filename, mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def find_password():
    website_name = website_entry.get()
    try:
        with open(filename) as file:
            data = json.load(file)
            result = data[website_name]
    
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found.")

    except KeyError:
        messagebox.showerror("Error", "Details for the website do not exist.")

    else:        
        messagebox.showinfo(f'{website_name}', 
                            f"Email: {result['email']}\nPassword: {result['password']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image_canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="DAY-29\\logo.png")
image_canvas.create_image(100, 100, image=logo)
image_canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=17, highlightthickness=0)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(command=find_password)
search_button.config(text="Search", highlightthickness=0, width=10)
search_button.grid(row=1, column=2)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)

username_entry = Entry()
username_entry.config(width=35, highlightthickness=0)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'Test@example.com')

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=17, highlightthickness=0)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.config(highlightthickness=0, width=15)
generate_button.grid(column=2, row=3)

save_button = Button(text="Add", command=save, highlightthickness=0)
save_button.config(width=30)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
