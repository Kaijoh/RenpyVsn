#first monster
#grammar puzzle
label firstvillain:
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

    
    jump puzzle1

label firstvillainwin:
    show greensad at center with moveinbottom
    "Ughhhh.. You have beaten me in my own challenge :(. My brothers will avenge me!!!"
    hide greensad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages

    jump Act3_2

label firstvillainlose:
    show greenmad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide greenmad with dissolve
    jump puzzle1

#second monster
#quiz
label secondvillain:
    show pic_12 with dissolve
    show bluemad at center with hpunch
    "OY OY OY! Look who is this."
    "A new kid? a kid from another world perhaps?"
    "I am Mr.Green the Slime."
    "Don't laugh at me kid! well anyways,,,, you are in my territory kid. now before you get a pass here you must play with me first."
    "kekekekekekekekekekekeke"
    "now lets start"
    hide bluemad with dissolve
    jump quiz1

label secondvillainwin:
    show bluesad at center with moveinbottom
    "Ughhhh.. You have beaten me in my own challenge :(. My brothers will avenge me!!!"
    hide bluesad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages

    jump Act3_3
   


label secondvillainlose:
    show bluemad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide bluemad with dissolve
    jump quiz1

#third monster
label thirdvillain:
    show pic_13 with dissolve
    show redmad at center with hpunch
    "OY OY OY! Look who is this."
    "A new kid? a kid from another world perhaps?"
    "I am Mr.Green the Slime."
    "Don't laugh at me kid! well anyways,,,, you are in my territory kid. now before you get a pass here you must play with me first."
    "kekekekekekekekekekekeke"
    "now lets start"
    hide redmad with dissolve
    jump puzzle6

label thirdvillainwin:
    show redsad at center with moveinbottom
    "Ughhhh.. You have beaten me in my own challenge :(. My brothers will avenge me!!!"
    hide redsad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages
    
    jump Act3_4


label thirdvillainlose:
    show redmad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide redmad with dissolve
    jump puzzle6