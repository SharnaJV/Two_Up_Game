import mysql.connector

# Setting up the connection to MYSQL DB
my_db_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Power2thePeopleWho8",
    database="twoupapp"
)

def create_tables():
    with my_db_connect.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gameresults (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(45),
                win_results INT,
                lose_results INT
            );
            
            CREATE TABLE IF NOT EXISTS userlogins (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username_login VARCHAR(45),
                password_login VARCHAR(45),
                email_login VARCHAR(45),
                first_name VARCHAR(45),
                last_name VARCHAR(45),
                employee_id INT
            );
        """)
        my_db_connect.commit()

# The program will add 1 to either the wins or losses column depending on the outcome of each round
def update_results(username, outcome):

#beginning of andre's working code
    # try:
    #     with my_db_connect.cursor() as cursor:
    #         if outcome == "WIN!":
    #             # Use INSERT to add a new row
    #             query = "INSERT INTO gameresults (username, win_results, lose_results) VALUES (%s, 1, 0)"
    #             cursor.execute(query, (username,))
    #         else:
    #             # Use INSERT to add a new row
    #             query = "INSERT INTO gameresults (username, win_results, lose_results) VALUES (%s, 0, 1)"
    #             cursor.execute(query, (username,))
    #         print("Executing query:", query)  # Add this line for debugging purposes
    #     my_db_connect.commit()
    # except mysql.connector.Error as error:
    #     print("Error updating results:", error)
#end of andre's working code

    try:
        with my_db_connect.cursor() as cursor:
            # Check if the user already exists in the gameresults table
            query_check_user = "SELECT * FROM gameresults WHERE username = %s;"
            cursor.execute(query_check_user, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                # Update the existing row
                if outcome == "WIN!":
                    query_update = "UPDATE gameresults SET win_results = win_results + 1 WHERE username = %s;"
                else:
                    query_update = "UPDATE gameresults SET lose_results = lose_results + 1 WHERE username = %s;"

                cursor.execute(query_update, (username,))
            else:
                # Insert a new row for the user
                if outcome == "WIN!":
                    query_insert = "INSERT INTO gameresults (username, win_results, lose_results) VALUES (%s, 1, 0);"
                else:
                    query_insert = "INSERT INTO gameresults (username, win_results, lose_results) VALUES (%s, 0, 1);"

                cursor.execute(query_insert, (username,))
            # Consume any remaining results
            cursor.fetchall()
            
            print("Executing query:", cursor.statement)  # Add this line for debugging purposes

        my_db_connect.commit()
    except mysql.connector.Error as error:
        print("Error updating results:", error)


#The outcome total of the rounds will show in the GUI
def read_results(username):
    try:
        # Extract the value from the Entry widget if it's a Tkinter Entry
        # username_value = username.get() 
        with my_db_connect.cursor() as cursor:
            query = "SELECT  win_results, lose_results FROM gameresults WHERE username = %s"
            print("Executing query:", query)  # Add this line for debugging purposes
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                wins, losses = result
                print("Wins:", wins, "Losses:", losses)  
                return wins, losses
            else:
                return  0, 0
    except mysql.connector.Error as error:
        print("Error reading results:", error)

def login(u1, p1):
    try:
        with my_db_connect.cursor() as cursor:
            query = "SELECT * FROM userlogins WHERE username_login = %s AND password_login = %s"
            cursor.execute(query, (u1, p1))
            user = cursor.fetchone()
            if user:
                print("Login Success")
                return True        
            else:
                print("Wrong username and/or password!")
                return False
    except mysql.connector.Error as error:
        print("Error during login:", error)

def reg_user(username_login, password_login, email_login, first_name, last_name, employee_id):
    try:
        print("Received values:")
        print("Username:", username_login)
        print("Password:", password_login)
        print("Email:", email_login)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Employee ID:", employee_id)
        with my_db_connect.cursor() as cursor:
            query = "INSERT INTO userlogins (username_login, password_login, email_login, first_name, last_name, employee_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (username_login, password_login, email_login, first_name, last_name, employee_id)
            cursor.execute(query, values)
            my_db_connect.commit()
            return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# Example usage
# create_tables()
# update_results("user1", "WIN!")
# read_results("user1")
# login("user1", "password123")
# reg_user("user2", "password456", "user2@example.com", "John", "Doe", 789)
