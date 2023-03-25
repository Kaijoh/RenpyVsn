define s = Character("Sylvie", color="#ff009d")
define r = Character("Robin", color="#c00606")

# backgrounds
image pic_1 = im.Scale("1.png", 1920, 1080)
image pic_2 = im.Scale("2.png", 1920, 1080)
image pic_3 = im.Scale("3.png", 1920, 1080)
image idle_1 = im.Scale("idle.jpg", 1920, 1080)
image teleport = Movie(size=(1920, 1080), channel="movie", play="Videos/tele.ogv", loop=True)


label start:
    $ player_score = 10
    $ player_name = renpy.input("what character name?")
    jump end_game

label end_game:
    python:
        import requests
        import json

        # Define the data to send to the server
        data = {'player_name': player_name, 'player_score': player_score}

        # Define the headers to include in the request
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

        # Send a POST request to the server with the player's score data
        response = requests.post('http://localhost:8000/submit_score/', data=json.dumps(data), headers=headers)
        

        # Check if the request was successful
        if response.status_code == 200:
            # Retrieve the scores from the server and display them
            response = requests.get('http://localhost:8000/score_board/')
            player_score = response.json()

            # Display the scores
            for score in player_score:
                print(f"Name: {score['player_name']}, Score: {score['player_score']}")
        else:
            # If the request was not successful, display an error message
            print(f"Error submitting score: {response.status_code} {response.reason}")

    "Your score: [player_score], would you like to submit it? note: dont submit if you dont want your data to be seen by others"

    return

label submit:
    "Your score: [player_score], has been submitted. Thank you for playing!"
    return

label notsubmit:
    "Your data and score is safe!"
    return
           


# label end_game:
#     # add the code to submit the player's score here
#     python:
#         data = {'player_name': player_name, 'player_score': player_score}
#         response = requests.post('http://localhost:8000/score_board/', data=data)
#         response.raise_for_status()

#     "Your score:[player_score], has been submitted. Thank you for playing!"

#     # retrieve scores from server and display them
#     python:
#         response = requests.get('http://localhost:8000/score_board/')
#         player_scores = response.json()

#         # display the scores
#         for score in player_scores:
#             "Name: {score['player_name']}, Score: {score['player_score']}"


# now i have this error down below:


# label end_game:
#     python:
#         # Define the data to send to the server
#         data = {'player_name': player_name, 'player_score': player_score}

#         # Define the headers to include in the request
#         headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

#         # Send a POST request to the server with the player's score data
#         response = requests.post('http://localhost:8000/submit_score/', data=json.dumps(data), headers=headers)

#         # Check if the request was successful
#         if response.status_code == 200:
#             # Retrieve the scores from the server and display them
#             response = requests.get('http://localhost:8000/score_board/')
#             player_scores = response.json()

#             # Display the scores
#             for score in player_scores:
#                 print("Name: {score['player_name']}, Score: {score['player_score']}")
#         else:
#             # If the request was not successful, display an error message
#             print("Error submitting score: {response.status_code} {response.reason}")













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
#     # your game code here

#     # update the player_score variable with the score at the end of the game
#     $ player_score = 1000

#     # send the score to the web server
#     data = {'player_name': player_name, 'player_score': player_score}
#     response = requests.post('http://localhost:8000/score_board/', data=data)

#     # display a message to the player that the score has been submitted
#     "Your score has been submitted. Thank you for playing!"



# label start:

#     show idle_1

#     # call variables

#     hide idle_1

#     jump Act2

#     return

# # label variables:

#     $ player_name = renpy.input("What is your name?")

#     $ player_score = 0  # move this line above the function call



# code my renpy.project:
# init python:
#     import requests
#     import json

# label start:
#     $ player_score = 10
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
#     python:
#         import json

#         # Define the data to send to the server
#         data = {'player_name': player_name, 'player_score': player_score}

#         # Define the headers to include in the request
#         headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

#         # Send a POST request to the server with the player's score data
#         response = requests.post('http://localhost:8000/score_board/', data=json.dumps(data), headers=headers)

#         # Check if the request was successful
#         if response.status_code == 200:
#             # Retrieve the scores from the server and display them
#             response = requests.get('http://localhost:8000/score_board/')
#             print(response.content)
#             player_score = response.json()

#             # Display the scores
#             for score in player_scores:
#                 "Name: {score['player_name']}, Score: {score['player_score']}"
#         else:
#             # If the request was not successful, display an error message
#             "Error submitting score: {response.status_code} {response.reason}"


# init python:
#     import requests
#     import json