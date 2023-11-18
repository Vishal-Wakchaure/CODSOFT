import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    characters = ''
    if 'uppercase' in complexity:
        characters += string.ascii_uppercase
    if 'lowercase' in complexity:
        characters += string.ascii_lowercase
    if 'digits' in complexity:
        characters += string.digits
    if 'special' in complexity:
        characters += string.punctuation

    if not characters:
        messagebox.showinfo('Error', 'Please select at least one complexity option.')
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    complexity = []
    if uppercase_var.get():
        complexity.append('uppercase')
    if lowercase_var.get():
        complexity.append('lowercase')
    if digits_var.get():
        complexity.append('digits')
    if special_var.get():
        complexity.append('special')

    password = generate_password(length, complexity)

    if password:
        result_label.config(text=f'Generated Password: {password}')
    else:
        result_label.config(text='')

# Create main window
window = tk.Tk()
window.title('Password Generator')

# Create and place widgets
length_label = tk.Label(window, text='Password Length:')
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=10)

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(window, text='Uppercase', variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky='w')

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(window, text='Lowercase', variable=lowercase_var)
lowercase_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky='w')

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(window, text='Digits', variable=digits_var)
digits_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky='w')

special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(window, text='Special Characters', variable=special_var)
special_checkbox.grid(row=4, column=0, padx=10, pady=5, sticky='w')

generate_button = tk.Button(window, text='Generate Password', command=generate_and_display_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text='')
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
