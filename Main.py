from tkinter import *
import tkinter as tk
import random
from MySQL_Authentication import *
from PIL import Image, ImageTk
import threading


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

#Creating the animation function
def coin_flip_animation(username, prediction, canvas):
    # dimensions
    width, height = 100, 180
    
    # Load coin images
    heads_image = Image.open("heads_coin.png")
    tails_image = Image.open("tails_coin.png")
    coin_sides = ImageTk.PhotoImage(heads_image), ImageTk.PhotoImage(tails_image)
    image_width, image_height = 100, 100
    heads_image = heads_image.resize((image_width, image_height))
    tails_image = tails_image.resize((image_width, image_height))
    heads_image = ImageTk.PhotoImage(heads_image)
    tails_image = ImageTk.PhotoImage(tails_image)
    
    coin_x, coin_y = (width // 2) - 65, height // 2
    coin_velocity = 0
    gravity = 1
    jump_strength = -20
    coin_image = heads_image

    frames = 100
    show_result = False

    while frames > 0:
        coin_velocity += gravity
        coin_y += coin_velocity

        if coin_y >= height - heads_image.height():
            coin_y = height - heads_image.height()
            coin_velocity = jump_strength

            result = random.choice(["HEADS", "TAILS"])
            if coin_image == heads_image:
                coin_image = tails_image
            else:
                coin_image = heads_image

        # Clear canvas
        canvas.delete("all")
        # Render coin image on canvas
        canvas.create_image(coin_x, coin_y, anchor='nw', image=coin_image)

        frames -= 1
        canvas.update()



def draw_coin_flip(win, width, height, heads_image, tails_image):
    coin_x, coin_y = (width//2) - 65, height//2
    coin_velocity = 0
    gravity = 1
    jump_strength = -20
    coin_image = heads_image
    clock = pygame.time.Clock()

    frames = 100
    show_result = False

    # Function to render result text and image

def run_coin_flip_animation(root, username, prediction, canvas):
    # Start the animation in a separate thread
    animation_thread = threading.Thread(target=coin_flip_animation, args=(username, prediction, canvas))
    animation_thread.start()

#setting up for GUI Customization
def change_colour(widget):
    set_widget_colour(widget, "black", "white", "bold")
    widget.config(bg="black")
    for child in widget.winfo_children():
        if isinstance(child, (Radiobutton,)):
            child.config(fg="white")
        else:
            set_text_color(child, "white")
        
def set_text_color(widget, color):
    print("Widget:", widget)
    if widget.winfo_children():
        for child in widget.winfo_children():
            print("Child:", child)
            set_text_color(child, color)
    elif isinstance(widget, (Label, Button, Entry, Text)):
        print("Configuring widget:", widget)
        widget.config(fg=color)

def original_theme(widget):
    original_button_color = "#B7521E"  # Set the original button color here
    
    widget.config(bg="#EFE0B9")  # Set background color
    for child in widget.winfo_children():
        original_theme(child)
        if isinstance(child, tk.Button):
            child.config(bg=original_button_color)

def toggle_theme(widget, to_black_and_white):
    if to_black_and_white:
        change_colour(widget)
    else:
        original_theme(widget)
        
def set_widget_colour(widget, bg_colour, fg_colour, border_style):
    widget.config(bg=bg_colour)  # Set background and foreground color
    widget.option_add('*background', bg_colour)
    widget.option_add('*foreground', fg_colour)
    widget.option_add('*Button*font', ("Arial", 10, border_style, fg_colour))
    widget.option_add('*Label*font', ("Arial", 10, border_style, fg_colour))
    widget.option_add('*Text*font', ("Arial", 10, border_style,fg_colour))
    widget.option_add('*Listbox*font', ("Arial", 10, border_style, fg_colour))
    widget.option_add('*Entry*font', ("Arial", 10, border_style, fg_colour))
    widget.option_add('*Scrollbar*background', fg_colour)
    # Explicitly set foreground color for all other text-related widgets
    widget.option_add('*Menu*foreground', fg_colour)
    widget.option_add('*Message*foreground', fg_colour)
    widget.option_add('*Radiobutton*foreground', fg_colour)
    
    # Recursively set background color for all child widgets
    for child in widget.winfo_children():
        set_widget_colour(child, bg_colour, fg_colour, border_style)
    
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
    two_up_screen.geometry("900x500")
    two_up_screen.configure(bg="#EFE0B9")

    prediction = StringVar()

    two_heads = Radiobutton(two_up_screen, text="Two Heads", variable=prediction, value="Two Heads", bg="#EFE0B9",
                            fg="#B7521E", font=("Arial", 12))
    two_heads.grid(row=1, column=0, padx=10, pady=5)

    two_tails = Radiobutton(two_up_screen, text="Two Tails", variable=prediction, value="Two Tails", bg="#EFE0B9",
                            fg="#B7521E", font=("Arial", 12))
    two_tails.grid(row=1, column=1, padx=10, pady=5)

    odds_ht = Radiobutton(two_up_screen, text="Odds - (Heads, Tails)", variable=prediction, value="Odds HT",
                          bg="#EFE0B9", fg="#B7521E", font=("Arial", 12))
    odds_ht.grid(row=1, column=2, padx=10, pady=5)

    odds_th = Radiobutton(two_up_screen, text="Odds - (Tails, Heads)", variable=prediction, value="Odds TH",
                          bg="#EFE0B9", fg="#B7521E", font=("Arial", 12))
    odds_th.grid(row=1, column=3, padx=10, pady=5)

    coin_1_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    coin_1_label.grid(row=2, column=1, sticky=N)

    coin_2_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    coin_2_label.grid(row=2, column=2, sticky=N)


    outcome_label_01 = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    outcome_label_01.grid(row=3, column=0, sticky= N)

    outcome_label_02 = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    outcome_label_02.grid(row=3, column=3, sticky= N)

    two_up_screen.rowconfigure(2, weight=1)
        
    flip_button = tk.Button(two_up_screen, text="FLIP!", width=15, bg="#B7521E", fg="#EFE0B9",
                            command=lambda: run_coin_flip_animation(root, username, prediction, canvas))
    flip_button.grid(row=4, column=2, sticky="n")

    # Create a Tkinter Canvas widget to display the animation
    canvas = tk.Canvas(two_up_screen, width=200, height=200)
    canvas.grid(row=3, column=1)

    wins_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    wins_label.grid(row=4, column=1)

    losses_label = Label(two_up_screen, text="", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    losses_label.grid(row=4, column=2)

    username_label = Label(two_up_screen, text=f"Username: {username}", bg="#EFE0B9", fg="#B7521E", font=("Arial", 16))
    username_label.grid(row=5, column=2)
    
#Adding the leaderboard to the GUI

    two_up_screen.columnconfigure(4, weight=1)
    
    leaderboard_label = Label(two_up_screen, width= 30, text="Leaderboard", bg="#EFE0B9", fg="#B7521E", font=("Arial", 20), bd=1, relief="solid")
    leaderboard_label.grid(row=1, column=4, sticky=N+S+E+W)

    leaderboard_text = Text(two_up_screen, height=100, width=30, bg="#E4B04A", fg="#B7521E", font=("Arial", 14), bd=1, relief="solid")
    leaderboard_text.grid(row=2, column=4, sticky=N+E, rowspan=8)

    top_players = fetch_top_players()  # Function to fetch top players
    for i, player in enumerate(top_players, 1):
        leaderboard_text.insert(END, f"{i}. {player[0]} - Wins: {player[1]}\n\n")

    leaderboard_text.config(state=DISABLED)
    
#Adding a button that customizes the GUI
    change_colour_button = Button(two_up_screen, text="Black and White", width=20, bg="#B7521E", fg="#EFE0B9", command=lambda: toggle_theme(two_up_screen, True))
    change_colour_button.grid(row=6, column=1, pady=10)

    original_theme_button = Button(two_up_screen, text="Original Theme", width=20, bg="#B7521E", fg="#EFE0B9", command=lambda: toggle_theme(two_up_screen, False))
    original_theme_button.grid(row=6, column=2, pady=10)
    
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