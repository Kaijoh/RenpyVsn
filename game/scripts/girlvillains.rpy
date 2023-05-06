#first monster

#grammar puzzle
label gfirstvillain:
    show greenmad at center with hpunch
    "OY OY OY! Look who is this."
    "A new kid? a kid from another world perhaps?"
    "I am Mr.Green the Slime."
    "Don't laugh at me kid! well anyways,,,, you are in my territory kid. now before you get a pass here you must play with me first."
    "kekekekekekekekekekekeke"
    "now lets start"
    hide greenmad with dissolve

    show screen hearts
    show screen arrows
    show screen books
    show screen fullbooks
    window hide
    ct "also before we start, see that 3 heart bar at the top right side?"
    ct "that would count as your lives, everytime you choose the wrong answer you will lose 1 life."
    ct "so make sure you read and answer all the question correctly. thats all and GOODLUCK [player_name]!"
    hide screen arrows with dissolve

    
    jump gpuzzle1

label gfirstvillainwin:
    show greensad at center with moveinbottom
    "Ughhhh.. You have beaten me in my own challenge :(. My brothers will avenge me!!!"
    hide greensad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages

    jump gAct3_2

label gfirstvillainlose:
    show greenmad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide greenmad with dissolve
    jump gpuzzle1

#second monster
#quiz
label gsecondvillain:
    show pic_12 with dissolve
    show bluemad at center with hpunch
    "OY OY OY! Look who is this."
    "the kid who beat my little brother haaaaa."
    "I am Mr.Blue the Slime."
    "Don't laugh at me kid! well anyways,,,, you are in my territory kid. now before you get the next page you must play with me first."
    "kakakakakakakakakakakakakakakakka"
    "now lets start"
    hide bluemad with dissolve
    jump gquiz1

label gsecondvillainwin:
    show bluesad at center with moveinbottom
    "Ughhhh.. You have beaten me in my own challenge :(. My brothers will avenge me!!!"
    hide bluesad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages

    jump gAct3_3
   


label gsecondvillainlose:
    show bluemad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide bluemad with dissolve
    jump gquiz1

#third monster
label gthirdvillain:
    show pic_13 with dissolve
    show redmad at center with hpunch
    "OY OY OY! Look who is this."
    "the one who beated my brothers"
    "I am Mr.Red the Slime."
    "Don't laugh at me kid! well anyways,,,, you are in my territory kid. now before you get the last pages and past here you must play with me first."
    "kukukukukukukukukukukukukukukuku"
    "now lets start"
    hide redmad with dissolve
    jump gpuzzle6

label gthirdvillainwin:
    show redsad at center with moveinbottom
    "Ughhhh.. You have beaten me in my own challenge... :()"
    hide redsad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages
    
    jump gAct3_4


label gthirdvillainlose:
    show redmad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide redmad with dissolve
    jump gpuzzle6