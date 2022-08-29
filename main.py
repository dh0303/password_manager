from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- SEARCH WEBSITE FOR PW ------------------------------- #
def find_password():
    website =  web_entry.get()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f) 
            if website in data.keys():
                pw = data[website]['password']
                messagebox.showinfo(title='Matched', message=f'A match is found for {website} Password: {pw}')
            else:
                messagebox.showinfo(message=f'No details for {website} exists')
    except FileNotFoundError:
        messagebox.showinfo(message='No Data File Found')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for letter in range(nr_letters)]
    password_list.extend([random.choice(numbers) for letter in range(nr_numbers)])
    password_list.extend([random.choice(symbols) for letter in range(nr_symbols)])
    random.shuffle(password_list)

    password = ''.join(password_list)

    pyperclip.copy(password)
    pw_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()
    new_data = {website: 
        {
            "email": email,
            'password': pw
        }
    }

    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(title='oops', message="Please don't leave any fields empty")
    
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                data.update(new_data)
            
            with open('data.json', 'w') as f:
                json.dump(data, f)

        except FileNotFoundError:
           with open('data.json', 'w') as f:
            json.dump(new_data, f)

        web_entry.delete(0, END)
        pw_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# the website label
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

# the email label
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

# the password label
pw_label = Label(text='Password:')
pw_label.grid(row=3, column=0)

# web entry
web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(row=1, column=1, sticky=EW)

# email entry
email_entry = Entry(width=35)
email_entry.insert(0, 'dorahu2003@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)

# password entry
pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1, sticky=EW)

# generate password button
pw_button = Button(text='Generate Password', command=generate_password)
pw_button.grid(row=3, column=2, sticky=EW)

# add button
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

# search button
search_button = Button(text='Search', command=find_password)
search_button.grid(row=1, column=2, sticky=EW)

mainloop()