label Act1:

    show pic_5
    # The game starts here.
    # show girl3 at center, darken
    # window hide
    ct "Act 1:"
    n "The protagonist is cleaning out the school library when they come across a mysterious book...."

    hide pic_5

    show pic_6

    # show girl3 at right with dissolve

    player_name "ohhhhhh! what is this?"

    player_name "i haven't seen anything like this before"

    # hide girl3 with dissolve

    n "the protagonist picked up the book."

    menu:
        "open the book":
            pass

        "don't open the book and return it":
            "Your final score [player_score]"
            jump end_game

    player_name "'The Lost Pages'? It looks pretty old...and it's missing some pages too."
    
    # show girl3 at right, darken
    # show girl4 at left, lighten
    # with dissolve

    n "The protagonist starts to read the book and suddenly gets transported into the story world."

    hide pic_6
    # show girl3 at right, lighten with dissolve
    show pic_7 with hpunch

    player_name "Whoa! What's happening? This is amazing...and kind of scary too."
    
    show teleport
    "......"

    hide teleport
    hide pic_7

    show pic_8

    n "The protagonist meets a friendly character, named Robin, who offers to help them navigate this new world."
    
    show robinnormal at left with moveinleft

    r "Greetings! I'm Robin, and I'm here to help you on your journey. You've entered the world of 'The Lost Pages', a land filled with magic and mystery."
    show robinnormal at left, darken

    show girlsmile at right with moveinright

    player_name "Wow, this is incredible. But I don't know how to get back home. And what's this about missing pages?"
    show girlsmile at right, darken

    show robinsurprised at left

    r "Ah, yes. The book you entered is missing some important pages. We need to find them if you want to return to your own world."
    show robinsurprised at left, darken

    show girlsmile at right, lighten

    menu:
        "Let's find the missing pages!":
            jump Act2
        "I'm too scared. Can't we just leave?":
            jump end_game

    hide pic_8

    # menu:
    #     "Open Map":
    #         $ location = renpy.call_screen("MapScreen", _layer="screens")
    #     "Continue?":
    #         jump Act2

label Act2:
    scene
    show pic_9
    # window hide
    ct "Act 2: Search for the Missing Pages"
    n "The protagonist and Robin set off on a quest to find the missing pages. Along the way, they meet various characters and encounter challenges."

    show girlsmile at right with dissolve

    player_name "This is amazing! I can't believe I'm actually in a book. But where do we start looking for the missing pages?"
    show girlsmile at right, darken
    

    show robinnormal at left with dissolve
    r  "We should start by visiting the Wise One. He knows everything about this world."
    hide girlsmile with dissolve
    hide robinnormal with dissolve

    n "They travel to the Wise One's castle and meet him."

    show pic_10

    show wisemsurprised at center with dissolve
    w "Greetings, travelers. I know why you're here. You're searching for the missing pages. I'm afraid I cannot help you directly, but I can offer you some advice."
    hide wisemsurprised with dissolve
    show wisemsurprised at left, darken

    show girlsmile at right with dissolve
    player_name "Please, Wise One. We need your help."
    show girlsmile at right, darken

    show wisemnormal at left with moveoutright
    w "Very well. To find the missing pages, you must first journey to the Forbidden Forest. But beware, it's a dangerous place."
    show wisemnormal at left, darken
    
    show robinnormal at Position(xpos=0.8,xanchor=0.8, ypos=1.0,yanchor=1.0) with moveinright
    r "Thank you for the help Sir."

    scene
    show pic_11
    n "The protagonist and Robin venture into the Forbidden Forest, facing obstacles and challenges along the way."

    menu:

        "Let's keep going!":
            jump Act3

        "I'm too scared. Let's turn back.":
            "Your final score [player_score]"
            jump end_game
    
label Act3:
    # window hide
    ct "Act 3: Learning English Concepts"

    n "As they search for the missing pages, the protagonist encounters various English concepts and learns about them through fun and interactive puzzles."

    show girlsurprised at right with moveinright
    player_name "Hey Robin, what's a simile?"
    show girlsurprised at right, darken

    show robinsmirk at left with moveinleft
    r "It's a figure of speech that compares two things using 'like' or 'as'. For example, 'her eyes sparkled like diamonds'."
    show robinsmirk at left, darken

    show girlshy at right, lighten
    player_name "Oh, I get it! That's pretty cool."
    
    hide girlsurprised with dissolve
    hide robinsmirk with dissolve
    hide girlshy with dissolve

    n "They come across a puzzle where they must match vocabulary words with their definitions."

    # Vocabulary puzzle

    n "................"

    jump firstvillain

label Act3_2:
    #quiz
    n "the protagonist and robin continued their journey to the magical cave....."
    jump secondvillain

label Act3_3:
    #grammar puzzle
    jump thirdvillain

label Act3_4:
    # Wise One's castle
    #show
    show wisemsurprised at left with moveinleft
    w "Well done, my young travelers. You have found all of the missing pages. And not only that, you have also learned much about the English language."
    show wisemsurprised at left, darken

    show girlshy2 at right with moveinright
    player_name "Thank you, Wise One. But how do we get back to our own world?"
    show girlshy2 at right, darken
    
    show wisemsurprised at left, lighten
    w "Simply open the book to the last page and say 'I wish to return'."
    hide wisemsurprised with moveoutleft

    hide girlshy2 with moveoutright

    show girlsmile at center with dissolve
    player_name "I wish to return."
    hide girlsmile with moveouttop

    show teleport

    hide teleport
    # Add transition effect here, such as dissolve or fadeout.

label Act4:
    scene
    # window hide
    show pic_8 with dissolve
    ct "Act 4: Conclusion...."

    n "The protagonist returns to reality and reflects on their adventure."
    
    show girlsmile at right with moveinright
    player_name "Wow, that was incredible. I can't believe I actually went on a quest to find missing pages in a book. And I learned so much about English language too."
    hide girlsmile with moveoutright
    menu:
        "I want to learn more about English language!":
            pass
        "I'm good for now, thanks.":
            pass
    
    show girlsmile at center with dissolve
    player_name "Hey, I wonder if there are more books like this. Maybe I can learn even more."
    hide girlsmile with dissolve
    scene
    jump Act5

label Act5:
    # window hide
    ct "Act 5: A New Challenge"

    n "............."

    n "The protagonist goes back to school and is excited to apply their newfound knowledge."

    show girlsurprised at right with moveinright
    player_name "I can't wait to show my English teacher everything I learned. Maybe I'll even get an A on my next quiz!"

    player_name "Ohhh i almost forgot, there is an upcomming quiz for our english class next week"

    show girlsmile at right
    player_name "Thats great i will test my newfound knowledge on that day."
    
    player_name "I'm in! This is the perfect chance to prove myself."
    hide girlsurprised
    hide girlsmile

    n "The protagonist go home and starts studying even harder."

label Act6:
    # window hide
    ct "Act 6: The Quiz"

    n "The day of the quiz arrives and the protagonist is nervous but confident."
    
    show girlsmile at right with moveinright
    player_name "I've got this. I know all about adjectives, adverbs, and pronouns. Bring it on!"
    hide girlsmile with moveoutright

    n "The protagonist started answering all the questions in the test paper."

    menu:
        "i think i did great on the quiz":
            jump cho1
        "for some reason i think i did not study enough.":
            jump cho2

    

label cho1:

    player_name "I did it! I got perfect score! All that studying really paid off."
    jump Act7

    

label cho2:
    player_name "I didn't got a perfect score, but I learned a lot from the experience. And I'll keep practicing so I can do better next time."
    

label Act7:
    # window hide
    ct "Act 7: Moving Forward..."

    n "The protagonist looks back on their journey and feels proud of how far they've come."

    player_name "I can't believe I went on an adventure in a book and then competed in an English language competition. I feel so much more confident now."

    menu:
        "...":
            pass
        "...":
            pass

    

label cho3:
    player_name "Me too! I want to keep improving my English skills and maybe even learn a new language."
    jump Actclosing
    

label cho4:
    player_name "That sounds like a great idea. Who knows where my next adventure will take me."
    jump Actclosing
    
label Actclosing:
    scene
    jump end_game