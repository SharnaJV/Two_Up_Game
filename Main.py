from tkinter import *
import random
from MySQL_Authentication import *
from widget_events import *

# Setting up the random generator for heads and tails results
def coin_toss():
    return random.choice(['Heads', 'Tails'])

# Setting up of the Two Up game logic without a betting function
def play_two_up(username, guess):
    coin_01 = coin_toss()
    coin_02 = coin_toss()
    result = {
        "coin_1" : f"Coin 1: {coin_01}",
        "coin_2" : f"Coin 2: {coin_02}",
        "outcome": ""
    }

    if guess == "Two Heads" and coin_01 == coin_02 == "Heads":
        result["outcome"] = "WIN!"
    elif guess == "Two Tails" and coin_01 == coin_02 == "Tails":
        result["outcome"] = "WIN!"
    elif guess == "Odds HT" and coin_01 != coin_02:
        if coin_01 == "Heads":
            result["outcome"] = "WIN!"
        else:
            result["outcome"] = "LOSE!"
    elif guess == "Odds TH" and coin_01 != coin_02:
        if coin_01 == "Tails":
            result["outcome"] = "WIN!"
        else:
            result["outcome"] = "LOSE!"
    else:
        result["outcome"] = "LOSE!"
        
    return result

def game_screen(username=None):

    def play_game():
        user_guess = prediction.get()
        username = uname_entry.get()
        result = play_two_up(username, user_guess)
        coin_1_label.config(text=result["coin_1"])
        coin_2_label.config(text=result["coin_2"])
        outcome_label_01.config(text=result["outcome"]) 
        outcome_label_02.config(text=result["outcome"])

#Results are pushed to the DB set up in MySQL_Authentication
        update_results(username, result["outcome"])

#Read the updated results and display in the GUI
        wins, losses = read_results(username)

        wins_label.config(text=f"Wins: {wins}")
        losses_label.config(text=f"Losses: {losses}")

    def username_entry(event):
        if uname_entry.get() == 'Enter your username':
            uname_entry.delete(0, "end")
            uname_entry.config(fg='black')

    def no_username_entry(_):
        if not uname_entry.get():
            uname_entry.insert(0, 'Enter your username')
            uname_entry.config(fg='grey')
        
#Creating the GUI frame        
    two_up_screen = Tk()

#Setup of game screen window is same as login window
    two_up_screen.title("Two Up")
    two_up_screen.iconbitmap("ANZAC_logo.ico")
    two_up_screen.geometry("800x450")
    two_up_screen.configure(bg="#EFE0B9")

#Setup of username entry field
    default_text = 'Enter your username'
    uname_entry = Entry(two_up_screen, bg="#FFFFFF", fg="grey", font=("Arial", 12))
    uname_entry.insert(0, default_text)
    uname_entry.bind('<FocusIn>', username_entry)
    uname_entry.bind('<FocusOut>', no_username_entry)
    uname_entry.grid(row=0, column=1, padx=10, pady=5)
    
#User predicts outcome with radio buttons
    prediction = StringVar()

    two_heads = Radiobutton(two_up_screen, text="Two Heads", variable=prediction, value="Two Heads", bg="#EFE0B9", fg="#B7521E", font=("Arial", 12))
    two_heads.grid(row=2, column=0, padx=10, pady=5)

    two_tails = Radiobutton(two_up_screen, text="Two Tails", variable=prediction, value="Two Tails", bg="#EFE0B9", fg="#B7521E", font=("Arial", 12))
    two_tails.grid(row=2, column=1, padx=10, pady=5)

    odds_ht = Radiobutton(two_up_screen, text="Odds - (Heads, Tails)", variable=prediction, value="Odds HT", bg="#EFE0B9", fg="#B7521E", font=("Arial", 12))
    odds_ht.grid(row=2, column=2, padx=10, pady=5)

    odds_th = Radiobutton(two_up_screen, text="Odds - (Tails, Heads)", variable=prediction, value="Odds TH", bg="#EFE0B9", fg="#B7521E", font=("Arial", 12))
    odds_th.grid(row=2, column=3, padx=10, pady=5)
    
#Current setup for showing coinflip results
    coin_1_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    coin_1_label.grid(row=3, column=1)

    coin_2_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    coin_2_label.grid(row=3, column=2)

    outcome_label_01 = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    outcome_label_01.grid(row=3, column=0)
    
    outcome_label_02 = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    outcome_label_02.grid(row=3, column=3)

    flip_button = Button(two_up_screen, text="FLIP!", width=15, height=2, bg="#B7521E", fg="#EFE0B9", command=play_game)
    flip_button.grid(row=4, column=2, pady=10)

#Labels for showing the wins and the losses in the GUI
    wins_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    wins_label.grid(row=5, column=1)

    losses_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    losses_label.grid(row=5, column=2)
    
    two_up_screen.mainloop()
    
game_screen()
my_db_connect.close()