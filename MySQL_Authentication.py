import mysql.connector 

#Setting up the connection to MYSQL DB
my_db_connect = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="Power2thePeopleWho8",
database="twoupapp"
)

mycursor = my_db_connect.cursor()

mycursor.execute("""
                CREATE TABLE IF NOT EXISTS gameresults (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(45),
                    win_results INT,
                    lose_results INT
                );
               """)

# The program will add 1 to either the wins or losses column depending on the outcome of each round
def update_results(username, outcome):
    try:
        if outcome == "WIN!":
            query = "INSERT INTO gameresults (username, win_results, lose_results) VALUES (%s, 1, 0)"
            mycursor.execute(query, (username,))
        else:
            query = "INSERT INTO gameresults (username, win_results, lose_results) VALUES (%s, 0, 1)"
            mycursor.execute(query, (username,))
        print("Executing query:", query)  # Added this line for debugging purposes

    except mysql.connector.Error as error:
        print("Error updating results:", error)
    finally:
        my_db_connect.commit()

# The outcome total of the rounds will show in the GUI
def read_results(username):
    try:
        query = "SELECT id, win_results, lose_results FROM gameresults WHERE username = %s"
        print("Executing query:", query)  # Added this line for debugging purposes
        mycursor.execute(query, (username,))
        result = mycursor.fetchone()
        if result:
            id, wins, losses = result
            print("ID: ", id, "Wins: ", wins, "Losses: ", losses)  # Print retrieved wins and losses
            return wins, losses
        else:
            return 0, 0
    except mysql.connector.Error as error:
        print("Error reading results: ", error)
        return None, 0, 0
    
    #Defining login function
def login(username, password):

    connection = my_db_connect
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM userlogins WHERE username_login = %s AND password_login = %s"
        cursor.execute(query,(username, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            print("Login Success")
            return True        
        else:
            print("Wrong username and/or password!")
            return False

def reg_user(username, password, email, first_name, last_name, employee_id):
    connection = my_db_connect()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO userlogins (username_login, password_login, email_login, first_name, last_name, employee_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (username, password, email, first_name, last_name, employee_id)
        
        try:
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
    else:
        return False