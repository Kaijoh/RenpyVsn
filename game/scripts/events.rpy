

label Act1:

    show pic_1
    # The game starts here.
    "The protagonist is cleaning out the school library when they come across a mysterious book...."
    
    player_name "What's this? 'The Lost Pages'? It looks pretty old...and it's missing some pages too."

    "The protagonist starts to read the book and suddenly gets transported into the story world."
    hide pic_1

    show teleport
    pause
    player_name "Whoa! What's happening? This is amazing...and kind of scary too."
    hide teleport

    show pic_2
    "The protagonist meets a friendly character, named Robin, who offers to help them navigate this new world."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images directory.

    "Greetings! I'm Robin, and I'm here to help you on your journey. You've entered the world of 'The Lost Pages', a land filled with magic and mystery."

    player_name "Wow, this is incredible. But I don't know how to get back home. And what's this about missing pages?"

    r "Ah, yes. The book you entered is missing some important pages. We need to find them if you want to return to your own world."
    hide pic_2

    show pic_3

    "The player is presented with a choice...."

    menu:
        "Let's find the missing pages!":
            $ player_score += 10
        "I'm too scared. Can't we just leave?":
            $ player_score += -10

    show tia mouth_c eye_full brow_down ex_blush at right
    with dissolve

    hide pic_3

    # These display lines of dialogue.

    "ohhhhhh! what is this?"

    player_name "i haven't seen anything like this before"

    "eileen picked up the book."

    menu:

        "open the book":
            "You opened the book and found something."
        "don't open the book and return it":
            "You returned the book from where it was."

    menu:
        "Open Map":
            $ location = renpy.call_screen("MapScreen", _layer="screens")
        "Continue?":
            jump Act2
    return

label Act2:

    $ player_name = renpy.input("What is your name?")
    $ player_score = 0
    
    menu:
        "Let's find the missing pages!":
            $ player_score += 10
        "I'm too scared. Can't we just leave?":
            $ player_score += 5
            
    "This is your final score: [player_score]/100"


    # # create a cursor object to interact with the database
    # mycursor = mydb.cursor()

    # # get the player name and score from the store
    # player_name = store.player_name
    # player_score = store.player_score

    # # insert the player score data into the database
    # sql = "INSERT INTO player_scores (player_name, player_score) VALUES (%s, %s)"
    # val = (player_name, player_score)
    # mycursor.execute(sql, val)

    # # commit the changes to the database
    # mydb.commit()

    # # close the cursor and database connection
    # mycursor.close()
    # mydb.close()



    
label Act3:

    "aaaaaaa"

    return

label Act4:

    "aaaaaaa"

    return

label Act5:

    "aaaaaaa"

    return

label end:

    " Congratulation you completed the game!!"

    " Your Total Score is....[PlayerScore]/100"

    return


