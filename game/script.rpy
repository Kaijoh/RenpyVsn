# character names 
define s = Character("Sylvie", color="#ff009d") 
define r = Character("Robin", color="#c00606") 
# define n = Character("Narrator", color="#460beb") 
define w = Character("Wise Man", color="#03ee36") 

# text
define ct = Character(None, what_color="#FFFFFF", what_background="#000000", kind=centered, what_line_spacing=20, what_size=75, what_outlines=[(5, "#000", 0, 0 )])
define n = Character(None, what_color="#FFFFFF", what_background="#000000", kind=centered, what_line_spacing=20, what_size=45, what_outlines=[(5, "#000", 0, 0 )])
 
# backgrounds 
image pic_1 = im.Scale("1.png", 1920, 1080) 
image pic_2 = im.Scale(".png", 1920, 1080) 
image pic_3 = im.Scale("3.png", 1920, 1080) 

image pic_4 = im.Scale("backgrounds/school-gate.png", 1920, 1080)
image pic_5 = im.Scale("backgrounds/library.png", 1920, 1080)
image pic_6 = im.Scale("backgrounds/book-floora.jpg", 1920, 1080)
image pic_7 = im.Scale("backgrounds/book-open.jpg", 1920, 1080)
image pic_8 = im.Scale("backgrounds/forest.png", 1920, 1080)
image pic_9 = im.Scale("backgrounds/hiking-trail.png", 1920, 1080)
image pic_10 = im.Scale("backgrounds/garden-rainy.jpg", 1920, 1080)
image pic_11 = im.Scale("backgrounds/rainforest.png", 1920, 1080)
image pic_12 = im.Scale("backgrounds/magical-cave.png", 1920, 1080)
image pic_13 = im.Scale("backgrounds/ruins.jpg", 1920, 1080)

image idle_1 = im.Scale("idle.jpg", 1920, 1080) 
image teleport = Movie(size=(1920, 1080), channel="movie", play="Videos/tele.ogv", loop=True) 

#highlights 
transform darken: 
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0) 
    linear 0.5 matrixcolor TintMatrix("#4e4e4e") * SaturationMatrix(1.0) 
 
transform lighten: 
    linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0) 

# transform xzoom -1:
 
image heart:
    "heart.png"
    zoom 5.80
image background:
    "background.png"
    zoom 5.80
image border:
    "border.png"
    zoom 5.80

image book:
    "book.png"
    zoom 0.2
image fullbook:
    "fullbook.png"
    zoom 0.1
image addpage:
    "addpage.png", addpage_bounce
    zoom 0.1

image arrow:
    "arrow.png", arrow_bounce

transform arrow_bounce:
    xoffset  40
    yoffset -40
    block:
        ease .25 xoffset 10 yoffset 10
        ease .25 xoffset -40 yoffset 40
        repeat

transform addpage_bounce:
    xoffset  40
    yoffset -40
    block:
        ease .25 xoffset 10 yoffset 10
        ease .25 xoffset -40 yoffset 40
        repeat


# init:
#     $ max_lives = 3
#     $ lives = max_lives

#     $ max_pages = 3
#     $ pages = 0

default player_score = 0
default max_pages = 3
default pages = 0
default max_lives = 3
default lives = max_lives

# start of the game
label start:
    # Display a message and show an alert box when a button is clicked
    show pic_4 with dissolve
    menu:
        "First choose your avatar.":
            jump gender
    

label gender: 
    menu: 
        "Ok...": 
            call screen choose_route with dissolve
        "No thank you!": 
            jump variable
    return
 
label variable: 
    $ player_name = renpy.input("what would you like to name your character?") 
    jump Act1
    return 


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
        "Exite Game and submit score?": 
            jump submit 
        "Play Again?": 
            jump notsubmit 
 
label submit: 
    "Your score: [player_score], has been submitted. Thank you for playing!" 
    return 
 
label notsubmit: 
    "goodluck"
    return 
 
 
 
# error: 
     
 
     
# label start: 
#     $ player_score = 10 
#     $ player_name = renpy.input("what character name?") 
#     jump end_game 
 
# label end_game: 
#     python: 
#         import requests 
#