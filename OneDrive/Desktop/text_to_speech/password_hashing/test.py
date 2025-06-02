import bcrypt
from tkinter import *

b'$2b$12$CtXcvwHXrB4A7lz2kFBI8eU2/jb2OEF8P41Mm9vZ4RQlJfIYb7rHy'

def validate(password):
    hashed = b'$2b$12$CtXcvwHXrB4A7lz2kFBI8eU2/jb2OEF8P41Mm9vZ4RQlJfIYb7rHy'
    password = bytes(password, encoding='utf-8')

    if bcrypt.checkpw(password, hashed):
        print("Login successful!")
    else:
        print("Invalid password :(")

root = Tk()
root.geometry("300x300")
Label(root, text="Enter Password").pack()

password_entry = Entry(root)
password_entry.pack()

button = Button(text="Validate", command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()




