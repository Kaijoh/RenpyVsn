label test:
    show pic_10
    show screen gameUI
    show screen rewardbutton
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
    

screen rewardbutton():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "stat2"
        action ShowMenu("rewardshop")

$ player_score = 0



screen rewardshop():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                   EXCHANGE REWARD.\n\nYou can exchange your book page here for a \npermanent additional heart that will help you\nin your jouney "
    vbox:
        xalign 0.5
        yalign 0.5
        yoffset 30 
        spacing 20 

        imagebutton: 
            idle "exchange2" 
            hover "exchange" 
            if pages >= 1:
                action [SetVariable("pages", pages - 1), SetVariable("max_lives", max_lives + 1), SetVariable("lives", lives + 1), ToggleScreen("adisplay"), ToggleScreen("rewardshop"), ]
            else:
                action ToggleScreen("adisplay")
                

        # imagebutton: 
        #     idle "exchange2" 
        #     hover "exchange" 
        #     if lives >= 1 and player_score >= 1:
        #         action [SetVariable("player_score", player_score + 1), SetVariable("lives", lives - 1)]
                  
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen adisplay():
    vbox:
        add "addh"
        xalign 0.5
        yalign 0.7

    imagebutton:
        xalign 0.5
        yalign 0.01
        xoffset -30
        yoffset 30
        idle "close"
        action [ToggleScreen("adisplay"), ToggleScreen("rewardshop")]
    
screen adisplay2():
    on show:
        with hpunch(0.5):
            pass

    # imagebutton:
    #     xalign 0.5
    #     yalign 0.01
    #     xoffset -30
    #     yoffset 30
    #     idle "close"
    #     action [ToggleScreen("adisplay2"), ToggleScreen("rewardshop")]
    


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