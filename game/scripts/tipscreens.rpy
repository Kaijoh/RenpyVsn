screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t2():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t2w")


screen t2w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t2a"), ToggleScreen("t2w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t2a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t3():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t3w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t3a"), ToggleScreen("t3w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t3a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t4():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t4w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t4a"), ToggleScreen("t4w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t4a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




screen t1():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tip"
        action ShowMenu("t1w")


screen t1w():
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                              \t!!!WARNING!!!\t\n\n         Your are about to view the correct answer \nwhich will hinder in your journey on learning english!\n\n                DO YOU STILL WISH TO CONTINUE? "

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        imagebutton:
            idle  "yes"
            action [ToggleScreen("t1a"), ToggleScreen("t1w")]

        imagebutton:
            idle  "no"
            action Return()
    
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen t1a():
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Answer! \n\nWhen talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()




