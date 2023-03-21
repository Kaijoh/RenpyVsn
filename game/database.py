import mysql.connector

def connect():
    # Replace the placeholders with your database credentials
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='vsn'
    )
    return conn
