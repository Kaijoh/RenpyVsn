

label Act1:

    show pic_1
    # The game starts here.
    show tia mouth_c eye_full brow_down ex_blush at center, darken
    n "The protagonist is cleaning out the school library when they come across a mysterious book...."

    show tia mouth_c eye_full brow_down ex_blush at right with dissolve
    player_name "What's this? 'The Lost Pages'? It looks pretty old...and it's missing some pages too."
    
    show tia mouth_c eye_full brow_down ex_blush at right, darken
    show tia mouth_s eye_half brow_up ex_none at left, lighten
    with dissolve

    n "The protagonist starts to read the book and suddenly gets transported into the story world."

    show tia mouth_c eye_full brow_down ex_blush at right, lighten with dissolve

    hide pic_1

    show teleport
    pause
    player_name "Whoa! What's happening? This is amazing...and kind of scary too."
    hide teleport

    show pic_2
    n "The protagonist meets a friendly character, named Robin, who offers to help them navigate this new world."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images directory.

    r "Greetings! I'm Robin, and I'm here to help you on your journey. You've entered the world of 'The Lost Pages', a land filled with magic and mystery."

    player_name "Wow, this is incredible. But I don't know how to get back home. And what's this about missing pages?"

    r "Ah, yes. The book you entered is missing some important pages. We need to find them if you want to return to your own world."
    hide pic_2

    show pic_3

    menu:
        "Let's find the missing pages!":
            $ player_score += 1
        "I'm too scared. Can't we just leave?":
            $ player_score += -1

    show tia mouth_c eye_full brow_down ex_blush at right
    show tia mouth_s eye_half brow_up ex_none at left
    with dissolve

    hide pic_3

    # These display lines of dialogue.

    player_name "ohhhhhh! what is this?"

    player_name "i haven't seen anything like this before"

    n "the protagonist picked up the book."

    menu:

        "open the book":
            $ player_score += 1
            jump Act2

        "don't open the book and return it":
            $ player_score += -1
            "Your final score [player_score]"
            jump end_game

    # menu:
    #     "Open Map":
    #         $ location = renpy.call_screen("MapScreen", _layer="screens")
    #     "Continue?":
    #         jump Act2

label Act2:
    
    "Act 2: Search for the Missing Pages"
    n "The protagonist and Robin set off on a quest to find the missing pages. Along the way, they meet various characters and encounter challenges."

    player_name "This is amazing! I can't believe I'm actually in a book. But where do we start looking for the missing pages?"

    r  "We should start by visiting the Wise One. He knows everything about this world."

    "They travel to the Wise One's castle and meet him."

    w "Greetings, travelers. I know why you're here. You're searching for the missing pages. I'm afraid I cannot help you directly, but I can offer you some advice."

    player_name "Please, Wise One. We need your help."

    w "Very well. To find the missing pages, you must first journey to the Forbidden Forest. But beware, it's a dangerous place."

    n "The protagonist and Robin venture into the Forbidden Forest, facing obstacles and challenges along the way."

    menu:

        "Let's keep going!":
            $ player_score += 1
            jump Act3

        "I'm too scared. Let's turn back.":
            $ player_score += -1
            "Your final score [player_score]"
            jump end_game



    
label Act3:

    "Act 3: Learning English Concepts"

    n "As they search for the missing pages, the protagonist encounters various English concepts and learns about them through fun and interactive puzzles."

    player_name "Hey Robin, what's a simile?"

    r "It's a figure of speech that compares two things using 'like' or 'as'. For example, 'her eyes sparkled like diamonds'."

    player_name "Oh, I get it! That's pretty cool."

    n "They come across a puzzle where they must match vocabulary words with their definitions."

    menu:

        "I want to try the puzzle!":
            $ player_score += 1
            jump Act3

        "I'm not interested in the puzzle.":
            $ player_score += -1
            "Your final score [player_score]"
            jump end_game


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


