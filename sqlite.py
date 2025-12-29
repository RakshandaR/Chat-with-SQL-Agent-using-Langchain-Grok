# creating sqlite db

import sqlite3

# connecting to sqlite 
connection = sqlite3.connect("student.db")

# creating a cursor object which is used to insert record and create table
cursor = connection.cursor()

# create the table - use sql queries to perform actions on table

table_info = """
create table Student (NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""
# execting below query will create table automatically
cursor.execute(table_info)

# insert record
cursor.execute('''Insert Into STUDENT values('Bryan', 'Data Science', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('John', 'Data Science', 'B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh', 'Data Science', 'A', 86)''')
cursor.execute('''Insert Into STUDENT values('Jacob', 'DEVOPS', 'A', 50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh', 'DEVOPS', 'A',35)''')

# showcasing records
print("Records: ")
data = cursor.execute('''Select * from Student''')

# rows will be in the form of lists so need to be traversed
for row in data:
    print(row)

# commit the changes to db
connection.commit()
connection.close()