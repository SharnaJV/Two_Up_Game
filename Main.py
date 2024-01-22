from tkinter import *
import random
from MySQL_Authentication import *
from widget_events import *

#Defining login function
def login_auth():
    uname_input = username.get()
    pwd_input = password.get()

    if login(uname_input,pwd_input):
        print("Proceed to game_screen or other actions after successful login")
        game_screen(login_screen,uname_input)
        
#Creating the user authentication screen
def login_form():
    global login_screen
    login_screen = Tk()
    login_screen.title("Two Up")
    login_screen.iconbitmap("ANZAC_logo.ico")
    login_screen.geometry("800x450")
    login_screen.configure(bg="#EFE0B9")

    global message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()
    
#Intro message
    Label(login_screen,width="300", text="For returning users enter login details then click \"Login\", new users click \"Register\"",
    bg="#123907",fg="#EFE0B9").pack()
    
#Username elements
    Label(login_screen, text="Username * ", bg="#EFE0B9").place(x=310,y=100)
    Entry(login_screen, textvariable=username, bg="#E4B04A").place(x=390,y=100)
    
#Password elements
    Label(login_screen, text="Password * ", bg="#EFE0B9").place(x=310,y=150)
    Entry(login_screen, textvariable=password ,show="*", bg="#E4B04A").place(x=390,y=150)
    
    Label(login_screen, text="",textvariable=message, bg="#EFE0B9", fg="#EFE0B9").place(x=400,y=180)
    
#Login Button
    Button(login_screen, text="Login", width=10, height=1,
    bg="#B7521E", fg="#EFE0B9", command=login_auth).place(x=320,y=200)

#Register Button
    Button(login_screen, text="Register", width=10, height=1,
    bg="#B7521E", fg="#EFE0B9", command=reg_form).place(x=415,y=200)

    login_screen.mainloop()

def registration():
    global registration_screen
    registration_screen = Tk()
    registration_screen.title("Register")
    registration_screen.geometry("400x300")
    registration_screen.configure(bg="#EFE0B9")
    
    global email
    global first_name
    global last_name 
    global employee_id
    email = StringVar()
    first_name = StringVar()
    last_name = StringVar()
    employee_id = StringVar()

    Label(registration_screen, text="Please enter details below to register", bg="#EFE0B9").pack()
    Label(registration_screen, text="").pack()

    Label(registration_screen, text="Username * ", bg="#EFE0B9").pack()
    Entry(registration_screen, textvariable=username, bg="#E4B04A").pack()

    Label(registration_screen, text="Password * ", bg="#EFE0B9").pack()
    Entry(registration_screen, textvariable=password, show="*", bg="#E4B04A").pack()

    Label(registration_screen, text="Email * ", bg="#EFE0B9").pack()
    Entry(registration_screen, textvariable=email, bg="#E4B04A").pack()

    Label(registration_screen, text="First Name * ", bg="#EFE0B9").pack()
    Entry(registration_screen, textvariable=first_name, bg="#E4B04A").pack()

    Label(registration_screen, text="Last Name * ", bg="#EFE0B9").pack()
    Entry(registration_screen, textvariable=last_name, bg="#E4B04A").pack()

    Label(registration_screen, text="Employee ID * ", bg="#EFE0B9").pack()
    Entry(registration_screen, textvariable=employee_id, bg="#E4B04A").pack()

    Button(registration_screen, text="Register", width=10, height=1, bg="#B7521E", fg="#EFE0B9", command=reg_user).pack()

    registration_screen.mainloop()
    
def reg_form():
    global register_screen
    register_screen = Tk()
    register_screen.title("Register Form")
    register_screen.geometry("300x200")
    Label(register_screen, text="Click Register to proceed", bg="#EFE0B9").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#B7521E", fg="#EFE0B9", command=registration).pack()

# Setting up the random generator for heads and tails results
def coin_toss():
    return random.choice(['Heads', 'Tails'])

# Setting up of the Two Up game logic without a betting function
def play_two_up(username,guess):
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

def game_screen(login_screen, username):
    wins = 0
    losses = 0
    
    def play_game():
        nonlocal wins, losses
        guess = prediction.get().strip()
        uname_input = username.get()
        # username = uname_entry.get()
        print("Debug: Username =", uname_input)
        print("Debug: Guess =", guess)       

        if not username:
            # Display an error message or handle this case
            print("Please enter a valid username.")
            return

#       if username and guess:
        if guess:
            print("Username:", username)
            print("Guess:", guess)            
           
            result = play_two_up(uname_input, guess)
            coin_1_label.config(text=result["coin_1"])
            coin_2_label.config(text=result["coin_2"])
            outcome_label_01.config(text=result["outcome"]) 
            outcome_label_02.config(text=result["outcome"])
            
#Update the wins and the losses based on outcome of each round
            if result["outcome"] == "WIN!":
                wins += 1
            else:
                losses += 1      
                     
# #Results are pushed to the DB set up in MySQL_Authentication
            # print("Username:", username)
            print("Outcome:", result["outcome"])
            update_results(uname_input, result["outcome"])

# #Read the updated results and display in the GUI
            wins, losses = read_results(uname_input)
            wins_label.config(text=f"Wins: {wins}")
            losses_label.config(text=f"Losses: {losses}")
        else:
            # Display an error message or handle the case where
            # username or guess is empty
            print("Username or guess is empty. Please enter both.")
        
#Creating the GUI frame        
    two_up_screen = Tk()

#Setup of game screen window is same as login window
    two_up_screen.title("Two Up")
    two_up_screen.iconbitmap("ANZAC_logo.ico")
    two_up_screen.geometry("800x450")
    two_up_screen.configure(bg="#EFE0B9")

#Setup of username entry field
    
    uname_entry = Entry(two_up_screen, bg="#FFFFFF", fg="grey", font=("Arial", 12), text=username, textvariable=username)
    uname_entry.grid(row=0, column=0, padx=10, pady=5)
    
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
    
from tkinter import *
from MySQL_Authentication import login, reg_user

login_form()    
game_screen()
my_db_connect.close()