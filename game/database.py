import mysql.connector

def connect():
    # Replace the placeholders with your database credentials
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='player_score'
    )
    return conn

import requests

def submit_score(player_name, score):
    url = 'http://localhost:8000/submit_score/'
    data = {'player_name': player_name, 'score': score}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Score submitted successfully!')
    else:
        print('Error submitting score.')
