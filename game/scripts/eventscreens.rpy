#routes x

screen choosechar:
    hbox:
        xalign 0.5
        yalign 0.1
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Choose your route."

screen choose_route: 
    hbox: 
        xalign 0.5 
        yalign 0.5 
        yoffset 30 
        spacing 20 
        imagebutton: 
            idle "boychar2" 
            hover "boychar" 
            action Jump("variable1") 
        imagebutton: 
            idle "girlchar" 
            hover "girlchar2" 
            action Jump("variable2") 

screen arrows():
    hbox:
        xalign 0.86
        yalign 0.14
        add "arrow"

screen hearts():
    hbox:
        xalign 0.01
        yalign 0.02
        
        for i in range(max_lives):
            fixed xysize(50, 50): 
                add "background"
                add "border"
                if i < lives:
                    add "heart"
                    
screen books():
    hbox:
        xalign 0.13
        yalign 0.03
        for i in range(pages):
            fixed xysize(99, 99): 
                add "book"

screen fullbooks():
    hbox:
        xalign 0.01
        yalign 0.01
        add "fullbook"

screen addpages():
    hbox:
        xalign 0.5
        yalign 0.5
        add "addpage"

#puzzles
screen question1():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?\nYou left _____ phone at home.\n\na. your\nb. you're"

screen question2(): 
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?\n_____ dinner last night, I watched a movie with my family.\n\na. After\nb. Before\nc. During\nd. On"

screen question3():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?\nThe teacher ____________ the students for not studying for the test.\n\na. Praised\nb. Scolded\nc. Encouraged\nd. Congratulated"

screen question4():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?\nShe was ____________ when she heard the news.\n\na. Happy\nb. Sad\nc. Excited\nd. Angry"

screen question5():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?\nThe team's performance was ____________ in the championship game.\n\na. Incredible\nb. Disappointing\nc. Excellent\nd. Outstanding"

screen question6():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "1. What is the definition of \'apprehensive'?.\n\na. feeling nervous or worried\nb. having a lot of knowledge or experience\nc. behaving in a showy way to impress others\nd. causing disgust or horror"

screen question7():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "2. What is the definition of 'conjecture'?.\n\na. a fact or piece of information that is known\nb. a conclusion based on incomplete evidence\nc. the feeling of being grateful for something\nd. a state of confusion or uncertainty"

screen question8():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "3. What is the definition of 'diligent'?.\n\na. showing great attention to detail or effort\nb. unwilling to give up or compromise\nc. characterized by a lack of order or planning\nd. having a tendency to change one's mind frequently"

screen question9():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "4. What is the definition of 'indignant'?.\n\na. feeling angry or annoyed about something unfair\nb. lacking energy or enthusiasm\nc. showing a lack of interest or concern\nd. having a tendency to avoid social situations"

screen question10():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "5. What is the definition of 'resilient'?.\n\na. having a tendency to take risks or be impulsive\nb. characterized by a lack of attention or focus\nc. showing a lack of emotion or enthusiasm\nd. able to recover quickly from difficulties or setbacks"

