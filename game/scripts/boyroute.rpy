label bAct1:
    scene black
    window hide
    ct "Act 1:"
    with Pause(1)
    show pic_5
    n "You are cleaning out the school library when you come across a mysterious book."

    hide pic_5

    show pic_6

    player_name "ohhhhhh! what is this?"

    player_name "i haven't seen anything like this before"

    n "You picked up the book."

    menu:
        "open the book":
            pass

        "don't open the book and return it":
            "Your final score [player_score]"
            jump end_game2

    player_name "'The Lost Pages'? It looks pretty old...and it's missing some pages too."
    
    n "You start to read the book and suddenly get transported into the storyworld."

    hide pic_6
    show pic_7 with hpunch

    player_name "Whoa! What's happening? This is amazing...and kind of scary too."
    
    show teleport
    "......"

    hide teleport
    hide pic_7

    show pic_8

    n "You meet a friendly character named Robin, who offers to help them navigate this new world."
    
    show robinnormal at left with moveinleft

    r "Greetings! I'm Robin, and I'm here to help you on your journey. You've entered the world of 'The Lost Pages', a land filled with magic and mystery."
    show robinnormal at left, darken

    show boysurprised at right with moveinright

    player_name "Wow, this is incredible. But I don't know how to get back home. And what's this about missing pages?"
    show boysurprised at right, darken

    show robinsurprised at left

    r "Ah, yes. The book you entered is missing some important pages. We need to find them if you want to return to your own world."
    show robinsurprised at left, darken

    show boynormal at right, lighten

    menu:
        "Let's find the missing pages!":
            jump bAct2
        "I'm too scared. Can't we just leave?":
            jump end_game2

    hide pic_8

label bAct2:
    scene black
    window hide
    ct "Act 2: Search for the Missing Pages"
    with Pause(1)
    show pic_9
    n "You and Robin set off on a quest to find the missing pages. Along the way, they meet various characters and encounter challenges."

    show boysurprised at right with dissolve

    player_name "This is amazing! I can't believe I'm actually in a book. But where do we start looking for the missing pages?"
    show boysurprised at right, darken
    

    show robinnormal at left with dissolve
    r  "We should start by visiting the Wise One. He knows everything about this world."
    hide boysurprised with dissolve
    hide robinnormal with dissolve

    n "They travel to the Wise One's castle and meet him."

    show pic_10

    show wisemsurprised at center with dissolve
    w "Greetings, travelers. I know why you're here. You're searching for the missing pages. I'm afraid I cannot help you directly, but I can offer you some advice."
    hide wisemsurprised with dissolve
    show wisemsurprised at left, darken

    show boyworried at right with dissolve
    player_name "Please, Wise One. We need your help."
    show boyworried at right, darken

    show wisemnormal at left with moveoutright
    w "Very well. To find the missing pages, you must first journey to the Forbidden Forest. But beware, it's a dangerous place."
    show wisemnormal at left, darken
    
    show robinnormal at Position(xpos=0.8,xanchor=0.8, ypos=1.0,yanchor=1.0) with moveinright
    r "Thank you for the help Sir."

    scene black
    show pic_11
    n "You and Robin venture into the Forbidden Forest, facing obstacles and challenges along the way."

    menu:

        "Let's keep going!":
            jump bAct3

        "I'm too scared. Let's turn back.":
            "Your final score [player_score]"
            jump end_game2
    
label bAct3:
    scene black
    window hide
    ct "Act 3: Learning English Concepts"
    with Pause(1)
    show pic_11

    n "As you search for the missing pages, you encounter various English concepts and learn about them through fun and interactive puzzles."

    show boynormal at right with moveinright
    player_name "Hey Robin, what's a simile?"
    show boynormal at right, darken

    show robinsmirk at left with moveinleft
    r "It's a figure of speech that compares two things using 'like' or 'as'. For example, 'her eyes sparkled like diamonds'."
    show robinsmirk at left, darken

    show boyblush at right, lighten
    player_name "Oh, I get it! That's pretty cool."
    
    hide boynormal with dissolve
    hide robinsmirk with dissolve
    hide boyblush with dissolve

    n "They come across a puzzle where they must match vocabulary words with their definitions."

    # Vocabulary puzzle

    n "................"

    jump bfirstvillain

label bAct3_2:
    #grammar puzzle
    scene black
    n "You and Robin continued their journey to the magical cave."
    jump bsecondvillain

label bAct3_3:
    #quiz
    scene black
    n "You and Robin continued their journey to the ruins."
    jump bthirdvillain

label bAct3_4:
    # Wise One's castle
    show wisemsurprised at left with moveinleft
    w "Well done, my young travelers. You have found all of the missing pages. And not only that, you have also learned much about the English language."
    show wisemsurprised at left, darken

    show boyworried at right with moveinright
    player_name "Thank you, Wise One. But how do we get back to our own world?"
    show boyworried at right, darken
    
    show wisemsurprised at left, lighten
    w "Simply open the book to the last page and say 'I wish to return'."
    hide wisemsurprised with moveoutleft

    hide boyworried with moveoutright

    show boynormal at center with dissolve
    player_name "I wish to return."
    hide boynormal with moveouttop

    show teleport

    "......"

    hide teleport
    # Add transition effect here, such as dissolve or fadeout.

label bAct4:
    scene black
    window hide
    ct "Act 4: Conclusion...."
    with Pause(1)
    show pic_5 with dissolve

    n "You return to reality and reflect on your adventure."
    
    show boyconfident at right with moveinright
    player_name "Wow, that was incredible. I can't believe I actually went on a quest to find missing pages in a book. And I learned so much about English language too."
    hide boyconfident with moveoutright
    menu:
        "I want to learn more about English language!":
            pass
        "I'm good for now, thanks.":
            pass
    
    show boyblush at center with dissolve
    player_name "Hey, I wonder if there are more books like this. Maybe I can learn even more."
    hide boyblush with dissolve
    jump bAct5

label bAct5:
    scene black
    window hide
    ct "Act 5: A New Challenge"
    with Pause(1)
    
    n "the next day......"

    show pic_4 with dissolve
    n "You go back to school and are excited to apply your newfound knowledge."

    show pic_15
    show boyconfident at right with moveinright
    player_name "I can't wait to show my English teacher everything I learned. Maybe I'll even get an A on my next quiz!"

    player_name "Ohhh i almost forgot, there is an upcomming quiz for our english class next week"

    show boynormal at right
    player_name "Thats great i will test my newfound knowledge on that day."
    
    hide boyconfident
    hide boynormal

    n "You go home and start studying even harder."

label bAct6:
    scene black
    window hide
    ct "Act 6: The Quiz"
    with Pause(1)

    show pic_15 with dissolve
    n "The day of the quiz arrives, and you are nervous but confident."
    
    show boyconfident at right with moveinright
    player_name "I've got this. I know all about adjectives, adverbs, and pronouns. Bring it on!"
    hide boyconfident with moveoutright

    n "You started answering all the questions on the test paper."

    menu:
        "i think i did great on the quiz":
            jump cho1
        "for some reason i think i did not study enough.":
            jump cho2

    
label cho1:

    player_name "I did it! I got perfect score! All that studying really paid off."
    jump bAct7

label cho2:
    player_name "I didn't got a perfect score, but I learned a lot from the experience. And I'll keep practicing so I can do better next time."
    
label bAct7:
    scene black
    window hide
    ct "Act 7: Moving Forward..."
    with Pause(1)
    show pic_5 with dissolve

    n "You look back on their journey and feel proud of how far they've come."

    player_name "I can't believe I went on an adventure in a book and then competed in an English language competition."

    menu:
        "i want to study more!":
            jump cho3
        "i hope i can find another book like that.":
            jump cho4


label cho3:
    player_name "I want to keep improving my English skills and maybe even learn a new language."
    jump bActclosing
    

label cho4:
    player_name "Who knows where my next adventure will take me."
    jump bActclosing
    
label bActclosing:
    scene
    jump end_game2