import mysql.connector

#Setting up the connection to MYSQL DB
my_db_connect = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Power2thePeopleWho8",
    database="twoupapp"
)
mycursor = my_db_connect.cursor()

#The program will add 1 to either the wins or losses column depending on the outcome of each round
def update_results(username, outcome):
    try:
        if outcome == "WIN!":
            query = "UPDATE gameresults SET win_results = win_results + 1 WHERE username = %s"
            mycursor.execute(query, (username,))
        else:
            query = "UPDATE gameresults SET lose_results = lose_results + 1 WHERE username = %s"
            mycursor.execute(query, (username,))
        print("Executing query:", query)  # Add this line for debugging purposes
        # mycursor.execute(query, (username,))
    except mysql.connector.Error as error:
        print("Error updating results:", error)
    finally:
        my_db_connect.commit()

#The outcome total of the rounds will show in the GUI
def read_results(username):
    try:
        query = "SELECT win_results, lose_results FROM gameresults WHERE username = %s"
        print("Executing query:", query)  # Add this line for debugging purposes
        mycursor.execute(query, (username,))
        result = mycursor.fetchone()
        if result:
            wins, losses = result
            print("Wins:", wins, "Losses:", losses)  # Print retrieved wins and losses
            return wins, losses
        else:
            return 0, 0
    except mysql.connector.Error as error:
        print("Error reading results:", error)
        return 0, 0