# character names 
define s = Character("Sylvie", color="#ff009d") 
define r = Character("Robin", color="#c00606") 
# define n = Character("Narrator", color="#460beb") 
define w = Character("Wise Man", color="#03ee36") 

# mytext
define ct = Character(None, what_color="#FFFFFF", what_background="#000000", kind=centered, what_line_spacing=20, what_size=55, what_outlines=[(5, "#000", 0, 0 )])
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
image pic_14 = im.Scale("backgrounds/club-room.png", 1920, 1080)
image pic_15 = im.Scale("backgrounds/classroom.png", 1920, 1080)


image idle_1 = im.Scale("idle.jpg", 1920, 1080) 
image teleport = Movie(size=(1920, 1080), channel="movie", play="Videos/tele.ogv", loop=True) 

image mytext = ParameterizedText(style="something")

style something:
    outlines [(3, "#000", 0, 0 )]
    xalign 0.5
    yalign 0.5

default player_score = 3
default max_pages = 3
default pages = 0
default max_lives = 3
default lives = max_lives


label splashscreen:
    scene black 
    with Pause(1)
    show mytext "Kaijoh Channel Presents......" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    show mytext "The Lost Pages" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    return
    
label splashscreen2:
    scene black
    with Pause(1)
    show mytext "Learning a new language like English is a journey of self-discovery and personal growth."
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    show mytext "So Start your journey now!"
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    jump gender

# start of the game
label start:
    # Display a message and show an alert box when a button is clicked
    jump splashscreen2
    

label gender: 
    show pic_4 with dissolve
    menu: 
        "Ok...":
            show screen choosechar 
            call screen choose_route with dissolve
        "No thank you!": 
            return
 
label variable1: 
    hide screen choosechar
    $ player_name = renpy.input("what would you like to name your character?") 

    scene black
    n "Synopsis: The protagonist is a high school student who is struggling with English class. One day, while cleaning out the school library, they discover a mysterious book that seems to be missing some pages. As they begin to read the book, they are transported into the story and must find the missing pages in order to return to their own world."
    jump gpquiz1
    

label variable2: 
    hide screen choosechar
    $ player_name = renpy.input("what would you like to name your character?") 
    
    scene black
    n "Synopsis: The protagonist is a high school student who is struggling with English class. One day, while cleaning out the school library, they discover a mysterious book that seems to be missing some pages. As they begin to read the book, they are transported into the story and must find the missing pages in order to return to their own world."
    jump gAct1
    

label end_game:
    hide screen hearts
    hide screen books
    hide screen fullbooks
    scene black 
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

    ct "GAME OVER!......"
    "Your score: [player_score], would you like to submit it? note: dont submit if you dont want your data to be seen by others" 
 
    menu: 
        "Exite Game and submit score?": 
            jump submit 
        "Play Again?": 
            jump notsubmit 
 
label submit: 
    "Your score: [player_score], has been submitted. Thank you for playing!" 
    scene
    jump splashscreen3
 
label notsubmit: 
    "Your score: [player_score], goodluck!"

    jump splashscreen3
 
label splashscreen3:
    scene
    scene black
    show boyblush at left with dissolve
    show girlshy at right with dissolve

    with Pause(1)
    show mytext "Kaijoh Channel Presents......" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    show mytext "Credits to:" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    show mytext "ASSETS - ITCH.IO" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    show mytext "Game Engine - Ren'Py" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    show mytext "THANK YOU FOR PLAYING! :)" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    return
    
