from tkinter import *
import random
from MySQL_Authentication import *



# Global variables
wins = 0
losses = 0

def login_auth(username, password, login_screen, root):
    u1 = username.get()
    p1 = password.get()

    if login(u1, p1):
        print("Proceed to game_screen or other actions after successful login")
        login_screen.withdraw()  # Close the login window

        # Open the game_screen with the username
        game_screen(root, u1)

def login_form(root):
    root.title("Two Up")
    root.iconbitmap("ANZAC_logo.ico")
    root.geometry("800x450")
    root.configure(bg="#EFE0B9")

    username = StringVar()
    password = StringVar()

    Label(root, width="300", text="For returning users enter login details then click \"Login\", new users click \"Register\"",
          bg="#123907", fg="#EFE0B9").pack()

    Label(root, text="Username * ", bg="#EFE0B9").place(x=310, y=100)
    Entry(root, textvariable=username, bg="#E4B04A").place(x=390, y=100)

    Label(root, text="Password * ", bg="#EFE0B9").place(x=310, y=150)
    Entry(root, textvariable=password, show="*", bg="#E4B04A").place(x=390, y=150)

    Label(root, text="", bg="#EFE0B9", fg="#EFE0B9").place(x=400, y=180)

    Button(root, text="Login", width=10, height=1,
           bg="#B7521E", fg="#EFE0B9", command=lambda: login_auth(username, password, root, root)).place(x=320, y=200)

    Button(root, text="Register", width=10, height=1,
           bg="#B7521E", fg="#EFE0B9", command=lambda: reg_form(root)).place(x=415, y=200)

def registration(root):
    registration_screen = Toplevel(root)
    registration_screen.title("Register")
    registration_screen.geometry("400x300")
    registration_screen.configure(bg="#EFE0B9")

    username = StringVar()
    password = StringVar()

    Label(registration_screen, text="Please enter details below to register", bg="#EFE0B9").pack()
    Label(registration_screen, text="").pack()

    Label(registration_screen, text="Username * ", bg="#EFE0B9").pack()
    username_entry = Entry(registration_screen, textvariable=username, bg="#E4B04A")
    username_entry.pack()

    Label(registration_screen, text="Password * ", bg="#EFE0B9").pack()
    password_entry = Entry(registration_screen, show="*", bg="#E4B04A")
    password_entry.pack()

    Label(registration_screen, text="Email * ", bg="#EFE0B9").pack()
    email_entry = Entry(registration_screen, bg="#E4B04A")
    email_entry.pack()

    Label(registration_screen, text="First Name * ", bg="#EFE0B9").pack()
    firstname_entry = Entry(registration_screen, bg="#E4B04A")
    firstname_entry.pack()

    Label(registration_screen, text="Last Name * ", bg="#EFE0B9").pack()
    lastname_entry = Entry(registration_screen, bg="#E4B04A")
    lastname_entry.pack()

    Label(registration_screen, text="Employee ID * ", bg="#EFE0B9").pack()
    employeeid_entry = Entry(registration_screen, bg="#E4B04A")
    employeeid_entry.pack()

    Button(registration_screen, text="Register", width=10, height=1, bg="#B7521E", fg="#EFE0B9",
           command=lambda: reg_user(username_entry.get(), password_entry.get(), email_entry.get(),
                                     firstname_entry.get(), lastname_entry.get(), employeeid_entry.get())).pack()

def reg_form(root):
    register_screen = Toplevel(root)
    register_screen.title("Register Form")
    register_screen.geometry("300x200")
    Label(register_screen, text="Click Register to proceed", bg="#EFE0B9").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#B7521E", fg="#EFE0B9",
           command=lambda: registration(root)).pack()

def game_screen(root, username):
    global wins, losses
    wins = 0
    losses = 0

    def play_game():
        global wins, losses

        p3 = prediction.get()
        print("Prediction:", p3)
        # play_two_up(p3)
        if username == '':
            print("Please enter a valid username.")
            return

        if p3:
            result = play_two_up(username, prediction)

            coin_1_label.config(text=result["coin_1"])
            coin_2_label.config(text=result["coin_2"])
            outcome_label_01.config(text=result["outcome"])
            outcome_label_02.config(text=result["outcome"])

            if result["outcome"] == "WIN!":
                wins += 1
            else:
                losses += 1

            print("Username:", username)
            print("Outcome:", result["outcome"])
            update_results(username, result["outcome"])

            # wins, losses = read_results(username)

            wins_label.config(text=f"Wins: {wins}")
            losses_label.config(text=f"Losses: {losses}")
        else:
            print("Prediction is empty. Please enter a prediction.")

    two_up_screen = Toplevel(root)
    two_up_screen.title("Two Up")
    two_up_screen.iconbitmap("ANZAC_logo.ico")
    two_up_screen.geometry("800x450")
    two_up_screen.configure(bg="#EFE0B9")

    prediction = StringVar()

    two_heads = Radiobutton(two_up_screen, text="Two Heads", variable=prediction, value="Two Heads", bg="#EFE0B9",
                            fg="#B7521E", font=("Arial", 12))
    two_heads.grid(row=2, column=0, padx=10, pady=5)

    two_tails = Radiobutton(two_up_screen, text="Two Tails", variable=prediction, value="Two Tails", bg="#EFE0B9",
                            fg="#B7521E", font=("Arial", 12))
    two_tails.grid(row=2, column=1, padx=10, pady=5)

    odds_ht = Radiobutton(two_up_screen, text="Odds - (Heads, Tails)", variable=prediction, value="Odds HT",
                          bg="#EFE0B9", fg="#B7521E", font=("Arial", 12))
    odds_ht.grid(row=2, column=2, padx=10, pady=5)

    odds_th = Radiobutton(two_up_screen, text="Odds - (Tails, Heads)", variable=prediction, value="Odds TH",
                          bg="#EFE0B9", fg="#B7521E", font=("Arial", 12))
    odds_th.grid(row=2, column=3, padx=10, pady=5)

    coin_1_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    coin_1_label.grid(row=3, column=1)

    coin_2_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    coin_2_label.grid(row=3, column=2)

    outcome_label_01 = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    outcome_label_01.grid(row=3, column=0)

    outcome_label_02 = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    outcome_label_02.grid(row=3, column=3)

    flip_button = Button(two_up_screen, text="FLIP!", width=15, height=2, bg="#B7521E", fg="#EFE0B9",
                         command=play_game)
    flip_button.grid(row=4, column=2, pady=10)

    wins_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    wins_label.grid(row=5, column=1)

    losses_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    losses_label.grid(row=5, column=2)

    username_label = Label(two_up_screen, text=f"Username: {username}", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    username_label.grid(row=6, column=2)

def coin_toss():
    return random.choice(['Heads', 'Tails'])

def play_two_up(username, prediction):
    u2 = username
    p3 = prediction.get()
    print("Prediction:", p3)
    coin_01 = coin_toss()
    coin_02 = coin_toss()
    print("Coin 1:", coin_01)
    print("Coin 2:", coin_02)
    result = {
        "coin_1": f"Coin 1: {coin_01}",
        "coin_2": f"Coin 2: {coin_02}",
        "outcome": ""
    }

    if p3 == "Two Heads" and coin_01 == coin_02 == "Heads":
        result["outcome"] = "WIN!"
    elif p3 == "Two Tails" and coin_01 == coin_02 == "Tails":
        result["outcome"] = "WIN!"
    elif p3 == "Odds HT" and coin_01 != coin_02:
        if coin_01 == "Heads":
            result["outcome"] = "WIN!"
        else:
            result["outcome"] = "LOSE!"
    elif p3 == "Odds TH" and coin_01 != coin_02:
        if coin_01 == "Tails":
            result["outcome"] = "WIN!"
        else:
            result["outcome"] = "LOSE!"
    else:
        result["outcome"] = "LOSE!"

    print("Prediction:", p3)
    print("Username:", u2)
    return result

if __name__ == "__main__":
    root = Tk()
    login_form(root)
    root.mainloop()