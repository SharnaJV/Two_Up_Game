import mysql.connector

my_db_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Power2thePeopleWho8",
    database="twoupapp"
)
print(my_db_connect)

cursor = my_db_connect.cursor()

cursor.execute("create database if not exists testbase01")

cursor.execute("""
                create table if not exists regtest(
                id int primary key,
                firstname varchar(50),
                lastname varchar(50),
                username varchar(10),
                password varchar(10)
               );
               """)
cursor.execute("""
                create table if not exists gamestest(
                regtest_id int,
                foreign key (regtest_id) references regtest(id), 
                username varchar(20),
                wins varchar(255),
                losses varchar(225)
               );
               """)

cursor.execute("show tables")
for table in cursor:
    print(table)