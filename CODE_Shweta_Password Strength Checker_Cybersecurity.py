import re
import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()

    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        strength += 1

    # Numbers
    if re.search(r"[0-9]", password):
        strength += 1

    # Special characters
    if re.search(r"[\W_]", password):
        strength += 1

    if strength <= 2:
        remarks = "Weak Password"
    elif strength == 3:
        remarks = "Medium Password ⚠"
    else:
        remarks = "Strong Password ✔"

    messagebox.showinfo("Result", remarks)


root = tk.Tk()
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=5)

entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack(pady=5)

btn = tk.Button(root, text="Check Strength", command=check_strength)
btn.pack(pady=10)

root.mainloop()

