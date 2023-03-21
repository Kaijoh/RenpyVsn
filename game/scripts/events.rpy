label Act1:

    show pic_1
    # The game starts here.
    "The protagonist is cleaning out the school library when they come across a mysterious book...."
    
    "What's this? 'The Lost Pages'? It looks pretty old...and it's missing some pages too."

    "The protagonist starts to read the book and suddenly gets transported into the story world."

    "Whoa! What's happening? This is amazing...and kind of scary too."

    "The protagonist meets a friendly character, named Robin, who offers to help them navigate this new world."
    hide pic_1

    show pic_2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images directory.

    "Greetings! I'm Robin, and I'm here to help you on your journey. You've entered the world of 'The Lost Pages', a land filled with magic and mystery."

    "Wow, this is incredible. But I don't know how to get back home. And what's this about missing pages?"

    "Ah, yes. The book you entered is missing some important pages. We need to find them if you want to return to your own world."
    hide pic_2

    show pic_3

    "The player is presented with a choice...."

    menu:
        "Let's find the missing pages!":
            $ PlayerScore += 1
        "I'm too scared. Can't we just leave?":
            $ PlayerScore += 0

    show tia mouth_c eye_full brow_down ex_blush at right
    with dissolve

    hide pic_3

    # These display lines of dialogue.

    "ohhhhhh! what is this?"

    "i haven't seen anything like this before"

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

    "aaaaaaa"

    return
    
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
