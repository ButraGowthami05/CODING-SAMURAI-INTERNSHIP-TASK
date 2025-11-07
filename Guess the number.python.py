import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x500")
root.config(bg="#D4DADD")

# Generate random number
number_to_guess = random.randint(1, 100)

# Function to check user's guess
def check_guess():
    try:
        guess = int(entry.get())
        if guess < number_to_guess:
            result_label.config(text="Too Low! Try again.")
        elif guess > number_to_guess:
            result_label.config(text="Too High! Try again.")
        else:
            result_label.config(text="🎉 Correct! You guessed it!")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Function to reset the game
def reset_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    entry.delete(0, tk.END)
    result_label.config(text="Game reset! Try a new number.")

# GUI widgets
title_label = tk.Label(root, text="Guess the Number (1–100)", font=("Arial", 14, "bold"), bg="#2FA7A9")
title_label.pack(pady=10)

entry = tk.Entry(root, width=10, font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Guess", command=check_guess, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
check_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, bg="#FF5722", fg="white", font=("Arial", 10, "bold"))
reset_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#F0F8FF")
result_label.pack(pady=20)

root.mainloop()
