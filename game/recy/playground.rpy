label test:
    show pic_10
    show screen gameUI
    pause




#bonus round 
label bonus1:
    show screen hearts
    show screen question1
    $ answer1 = renpy.input("Type your answer here!")

    if answer1.lower() in ["cat"]:
        $ max_lives +=1
        $ lives += 1
        hide screen question1
        ct "Wonderful! guess you have a knacked on this thing. Now lets spice things up ;)"
        jump bonus1

    $ lives -= 1
    hide screen question1
    show girlupset at right with moveinbottom
    ct "uhhhhh you miss the bonus round :'("
    hide girlupset with dissolve

    jump bonus1

screen gameUI():
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "stat"
        action ShowMenu("StatsUI")

# screen StatsUI():
#     add "pic_4"
#     frame:
#         xalign 0.5
#         yalign 0.5
#         ypadding 30
#         xpadding 30
#         hbox:

#             spacing 40

#             vbox:
#                 spacing 10
#                 text "Name:" size 40
#                 text "Score" size 40
#                 text "Lives" size 40
#                 text "Pages" size 40
            
#             vbox:
#                 spacing 10
#                 text '[player_name]' size 40
#                 text '[player_score]' size 40
#                 text '[lives]' size 40
#                 text '[pages]' size 40
#     imagebutton:
#         xalign 1.0
#         yalign 0.0
#         xoffset -30
#         yoffset 30
#         idle "close"
#         action Return()

screen StatsUI():
    hbox:
        xalign 0.5
        yalign 0.5
        frame:
            add "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (750,370)
            margin (0,0,0,0)
            vbox:
                xalign 0.25
                yalign 0.3
                spacing 10
                text "PLAYER STATS" size 40
                text "Name:" size 40
                text "Score:" size 40
                text "Lives:" size 40
                text "Pages:" size 40
            
            vbox:
                
                xalign 0.85
                yalign 0.3
                spacing 10
                text '       ' size 40
                text '[player_name]' size 40
                text '[player_score]' size 40
                text '[lives]' size 40
                text '[pages]' size 40

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()
            
            

#bonus screens

screen bonus1():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "..."

#score 

screen pscore():
    hbox:
        xalign 0.02
        yalign 0.2
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (10,20)
            margin (0,0,0,0)
            text "Score: [player_score]"

screen plive():
    hbox:
        xalign 0.02
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (10,20)
            margin (0,0,0,0)
            text "+[lives]"