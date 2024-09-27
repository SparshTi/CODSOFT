import tkinter as tk
from tkinter import messagebox
import random


user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1
    

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")
    result_label.config(text="Choose Rock, Paper, or Scissors to start the game!")

def ask_play_again():
    response = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if response:
        result_label.config(text="Choose Rock, Paper, or Scissors to start the game!")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")
root.configure(bg="#2E2E2E")


tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16), background="#2E2E2E", foreground="white").pack(pady=10)

button_frame = tk.Frame(root, bg="#2E2E2E")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", command=lambda: play_game("Rock")).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Paper", command=lambda: play_game("Paper")).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Scissors", command=lambda: play_game("Scissors")).pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to start the game!", font=("Arial", 14), background="#2E2E2E", foreground="white")
result_label.pack(pady=10)

tk.Button(root, text="Play Again", command=ask_play_again).pack(pady=10)

user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=("Arial", 12), background="#2E2E2E", foreground="white")
user_score_label.pack(pady=5)

computer_score_label = tk.Label(root, text=f"Computer's Score: {computer_score}", font=("Arial", 12), background="#2E2E2E", foreground="white")
computer_score_label.pack(pady=5)


root.mainloop()
