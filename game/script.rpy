define s = Character("Sylvie", color="#ff009d")
define r = Character("Robin", color="#c00606")
define n = Character("Narrator", color="#460beb")
define w = Character("Wise Man", color="#03ee36")


# backgrounds
image pic_1 = im.Scale("1.png", 1920, 1080)
image pic_2 = im.Scale("2.png", 1920, 1080)
image pic_3 = im.Scale("3.png", 1920, 1080)
image idle_1 = im.Scale("idle.jpg", 1920, 1080)
image teleport = Movie(size=(1920, 1080), channel="movie", play="Videos/tele.ogv", loop=True)

default player_score = 0

#highlights
transform darken:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    linear 0.5 matrixcolor TintMatrix("#4e4e4e") * SaturationMatrix(1.0)

transform lighten:
    linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)


# in my renpy script.rpy
label start:
    # $ player_score = 0
    $ player_name = renpy.input("what character name?")
    jump Act1


label end_game:
    python:
        import requests
        import json

        # Define the data to send to the server
        data = {'player_name': player_name, 'player_score': str(player_score)}
        # data = {'player_name': player_name, 'player_score': player_score}
        response = requests.post('http://localhost:8000/submit_score/', data=data)

        # Define the headers to include in the request
        # headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

        # # Send a POST request to the server with the player's score data
        # response = requests.post('http://localhost:8000/submit_score/', data=json.dumps(data), headers=headers)
        

        # Check if the request was successful
        if response.status_code == 200:
            # Retrieve the scores from the server and display them
            response = requests.get('http://localhost:8000/score_board/')
            if response.ok:
                try:
                    player_scores = response.json()
                    # Display the scores
                    for score in player_scores:
                        print(f"Name: {score['player_name']}, Score: {score['player_score']}")
                except json.JSONDecodeError as e:
                    print(f"Error decoding response: {e}")
            else:
                # If the request was not successful, display an error message
                print(f"Error retrieving scores: {response.status_code} {response.reason}")
        else:
            # If the request was not successful, display an error message
            print(f"Error submitting score: {response.status_code} {response.reason}")

    "Your score: [player_score]/100, would you like to submit it? note: dont submit if you dont want your data to be seen by others"

    menu:
        "Submit Your Score?":
            jump submit
        "don't submit it!":
            jump notsubmit

label submit:
    "Your score: [player_score], has been submitted. Thank you for playing!"
    return

label notsubmit:
    "Your data and score is safe!"
    return



# error:
    

    
# label start:
#     $ player_score = 10
#     $ player_name = renpy.input("what character name?")
#     jump end_game

# label end_game:
#     python:
#         import requests
#         import json

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
#                 print(f"Name: {score['player_name']}, Score: {score['player_score']}")
#         else:
#             # If the request was not successful, display an error message
#             print(f"Error submitting score: {response.status_code} {response.reason}")

#     "Your score: [player_score], would you like to submit it? note: dont submit if you dont want your data to be seen by others"

#     return

# label submit:
#     "Your score: [player_score], has been submitted. Thank you for playing!"
#     return

# label notsubmit:
#     "Your data and score is safe!"
#     return