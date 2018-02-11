# Code to connect MS SQL via python

# In your command prompt enter following command to install pyodbc
# pip install pyodbc

import pyodbc

# Replace ServerName, DatabaseName, UserName and Password
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=ServerName;'
    r'DATABASE=DatabaseName;'
    r'UID=UserName;'
    r'PWD=Password'
    )

cursor = conn.cursor()

cursor.execute("select * from sys.database_files")
for row in cursor.fetchall():
    print(row)
