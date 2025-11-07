import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x470")
root.config(bg="#f2f2f2")

# Entry display
entry = tk.Entry(root, width=25, font=('Arial', 18), borderwidth=2, relief="solid", justify='right')
entry.pack(pady=10, padx=10, ipady=10)

# Functions
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate(event=None):
    try:
        expression = entry.get().replace('%', '/100')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Keyboard bindings
root.bind("<Return>", calculate)
root.bind("<BackSpace>", lambda e: backspace())
root.bind("<Escape>", lambda e: clear())

# Button layout
buttons = [
    ['(', ')', '%', 'C'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '←', '+'],
    ['=']
]

# Create buttons dynamically
for row in buttons:
    frame = tk.Frame(root, bg="#f2f2f2")
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        if btn_text == 'C':
            button = tk.Button(frame, text=btn_text, font=('Arial', 18), bg="#f44336", fg="white", command=clear)
        elif btn_text == '=':
            button = tk.Button(frame, text=btn_text, font=('Arial', 18), bg="#4CAF50", fg="white", command=calculate)
        elif btn_text == '←':
            button = tk.Button(frame, text=btn_text, font=('Arial', 18), bg="#2196F3", fg="white", command=backspace)
        else:
            button = tk.Button(frame, text=btn_text, font=('Arial', 18),
                               command=lambda val=btn_text: click(val))
        button.pack(side='left', expand=True, fill='both', padx=1, pady=1)

root.mainloop()

