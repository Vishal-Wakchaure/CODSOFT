import tkinter as tk

def on_button_click(event):
    current = result_var.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif text == "C":
        result_var.set("")
    else:
        result_var.set(current + text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Variable to store the result
result_var = tk.StringVar()

# Entry widget to display the result
result_entry = tk.Entry(root, textvariable=result_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
result_entry.pack(fill=tk.BOTH, expand=True)

# Buttons for arithmetic operations and numbers
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()

    for button_text in row:
        button = tk.Button(frame, text=button_text, font="Arial 16", padx=20, pady=20, bd=4, relief=tk.RAISED)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_button_click)

# Run the main event loop
root.mainloop()