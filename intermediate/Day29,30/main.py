from tkinter import *
from tkinter import messagebox
import random
import json

FONT_NAME = "Courier"
YELLOW = "#f7f5dd"

# ---------------------------------- Search --------------------------------------#


def search_password():
    website = website_input.get()

    if website != "":
        try:
            with open("password_data.json", "r") as file:
                # read data in password_data.json first
                web_data = json.load(file)
                if website in web_data:
                    web_email = web_data[website]["email"]
                    web_password = web_data[website]["password"]
                    messagebox.showinfo(title="Website Data", message=f"Here is your account in {website}\n"
                                                                      f"email: {web_email}\n"
                                                                      f"password: {web_password}")
                else:
                    messagebox.showinfo(title="No exists such website", message="There is no account data for the websi"
                                                                                "te")
        except FileNotFoundError:
            print("There is no such website data")

    else:
        messagebox.showinfo(title="Empty warning", message="Please don't leave empty space")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    """generate password by combining letters, numbers and symbols """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    random_letters = random.sample(letters,nr_letters)
    result_letters = ''.join(random_letters)

    random_numbers = random.sample(numbers,nr_numbers)
    result_numbers = ''.join(random_numbers)

    random_symbols = random.sample(symbols,nr_symbols)
    result_symbols = ''.join(random_symbols)

    password_easy = result_letters + result_numbers + result_symbols

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    password_hard = list(password_easy)
    random.shuffle(password_hard)

    result_hard_password = ''.join(password_hard)
    password_input.insert(0, result_hard_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Empty warning", message="Please don't leave the empty space.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail: {email}\n"
                                                              f"Password: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("password_data.json", "r") as file:
                    # read data in password_data.json first
                    data = json.load(file)
            except FileNotFoundError:
                with open("password_data.json", "w") as file:
                    # create password_data.json and write new_data inside
                    json.dump(new_data, file, indent=4)
            else:
                # update the existing data with new_data
                data.update(new_data)

                with open("password_data.json", "w") as file:
                    # write data into password_data.json
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

# Website Label
website_text = Label(text="Website: ", bg=YELLOW)
website_text.config(padx=5, pady=5)
website_text.grid(row=1, column=0)

# Email/Username Label
email_text = Label(text="Email/Username: ", bg=YELLOW)
email_text.config(padx=5, pady=5)
email_text.grid(row=2, column=0)

# Password Label
password_text = Label(text="Password:", bg=YELLOW)
password_text.config(padx=5, pady=5)
password_text.grid(row=3, column=0)

# Website entry
website_input = Entry(width=27)
website_input.focus()
website_input.grid(row=1, column=1)

# Email entry
email_input = Entry(width=40)
email_input.insert(0, "huanghank2000@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

# Password Entry
password_input = Entry(width=27)
password_input.grid(row=3, column=1)

# search button
search_button = Button(text="Search", width=10, command=search_password)
search_button.grid(row=1, column=2)

# generate button
generate_button = Button(text="Generate", width=10, command=password_generator)
generate_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", width=39, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()