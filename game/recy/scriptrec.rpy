# define s = Character("Sylvie", color="#ff009d")

# # backgrounds
# image pic_1 = im.Scale("1.png", 1920, 1080)
# image pic_2 = im.Scale("2.png", 1920, 1080)
# image pic_3 = im.Scale("3.png", 1920, 1080)
# image idle_1 = im.Scale("idle.jpg", 1920, 1080)
# image teleport = Movie(size=(1920, 1080), channel="movie", play="Videos/tele.ogv", loop=True)

# # characters
# image protagonist = im.Scale("tia mouth_c eye_full brow_down ex_blush.png", 1920, 1080)

# init python:
#     import requests

# label start:
#     $ player_score = 0
#     $ player_name = renpy.input("What is your name?")

# screen enter_name():
#     modal True
#     tag menu

#     frame:
#         hbox:
#             text "Enter your name: "
#             input id "name_input" length 30

#         textbutton _("Submit") action [SetVariable("player_name", name_input.text), Jump("end_game")]

# label end_game:
#     # add the code to submit the player's score here
#     data = {'player_name': player_name, 'player_score': player_score}
#     response = requests.post('http://localhost:8000/score_board/', data=data)

#     # display a message to the player that the score has been submitted
#     "Your score has been submitted. Thank you for playing!"










# init python:
#     # Import the Persistent class
#     from collections import defaultdict
#     # from renpy.store import StoreBase
#     import mysql.connector 
    

#     # establish a connection to the database
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="",
#         database="player_score"
#     )

#     class MyPersistent(StoreBase):
#         _persist_store_key = "mypersistent"

#         def __init__(self):
#             super().__init__()
#             self.my_var = ""

#     # Create a new instance of the persistent store
#     config.persist = MyPersistent()

# label start:
#     "Welcome to the game"
#     $ player_name = renpy.input("What is your name?")
#     $ player_score = renpy.random.randint(1, 50)
#     jump end_game

# label end_game:
#     python:
#         if not type(persistent.scores) == "list":
#             persistent.scores = []
#         persistent.scores.append({
#             name: player_name, 
#             score: player_score
#         })








# define s = Character("Sylvie", color="#ff009d")

# # backgrounds
# image pic_1 = im.Scale("1.png", 1920, 1080)
# image pic_2 = im.Scale("2.png", 1920, 1080)
# image pic_3 = im.Scale("3.png", 1920, 1080)
# image idle_1 = im.Scale("idle.jpg", 1920, 1080)
# image teleport = Movie(size=(1920, 1080), channel="movie", play="Videos/tele.ogv", loop=True)

# # characters
# image protagonist = im.Scale("tia mouth_c eye_full brow_down ex_blush.png", 1920, 1080)

# init python:
#     import requests

# label start:
#     $ player_score = 100
#     $ player_name = renpy.input("What is your name?")

# screen enter_name():
#     modal True
#     tag menu

#     frame:
#         hbox:
#             text "Enter your name: "
#             input id "name_input" length 30

#         textbutton _("Submit") action [SetVariable("player_name", name_input.text), Jump("submit_score")]

# label submit_score:
#     python:
#         # add the code to submit the player's score here
#         data = {'player_name': player_name, 'player_score': player_score}
#         response = requests.post('http://localhost:8000/score_board/', data=data)

#     # display a message to the player that the score has been submitted
#     "Your score has been submitted. Thank you for playing!"

# init python:
#     import requests

# label start:
#     $ player_score = 0
#     $ player_name = renpy.input("What is your name?")

# label play_game:
#     # your game code goes here
#     $ player_score = 100  # for example

# label end_game:
#     # add the code to submit the player's score here
#     data = {'player_name': player_name, 'player_score': player_score}
#     response = requests.post('http://localhost:8000/score_board/', data=data)

#     # retrieve the player's score from the web server
#     response = requests.get('http://localhost:8000/get_score/?player_name={}'.format(player_name))
#     player_score = int(response.text)

#     # display a message to the player with their score
#     "Your final score is {}".format(player_score)






# define s = Character("Sylvie", color="#ff009d")

# # backgrounds
# image pic_1 = im.Scale("1.png", 1920, 1080)
# image pic_2 = im.Scale("2.png", 1920, 1080)
# image pic_3 = im.Scale("3.png", 1920, 1080)
# image idle_1 = im.Scale("idle.jpg", 1920, 1080)
# image teleport = Movie(size=(1920, 1080), channel="movie", play="Videos/tele.ogv", loop=True)

# # characters
# image protagonist = im.Scale("tia mouth_c eye_full brow_down ex_blush.png", 1920, 1080)

# init python:
#     import requests

# label start:
#     $ player_score = 0
#     $ player_name = renpy.input("What is your name?")

# screen enter_name():
#     modal True
#     tag menu

#     frame:
#         hbox:
#             text "Enter your name: "
#             input id "name_input" length 30

#         textbutton _("Submit") action [SetVariable("player_name", name_input.text), Jump("game")]

# label game:
#     # add game logic here to calculate player_score

#     # add the code to submit the player's score here
#     data = {'player_name': player_name, 'player_score': player_score}
#     response = requests.post('http://localhost:8000/submit_score/', data=data)

#     # display a message to the player that the score has been submitted
#     "Your score has been submitted. Thank you for playing!"

# label high_scores:
#     # add the code to retrieve the high scores here
#     response = requests.get('http://localhost:8000/high_scores/')
#     high_scores = response.json()

#     # display the high scores to the player
#     text "High Scores"
#     for score in high_scores:
#         text "{}: {}".format(score['player_name'], score['player_score'])
