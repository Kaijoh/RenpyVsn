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



label puzzle1:
    show screen hearts
    show screen question1
    $ answer1 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer1.lower() in ["your"]:
        $ player_score += 1
        hide screen question1
        ct "Wonderful! guess you have a knacked on this thing. Now lets spice things up ;)"
        jump puzzle2

    $ player_score -= 1
    $ lives -= 1
    hide screen question1
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle1

label puzzle2:
    show screen hearts
    show screen question2
    $ answer2 = renpy.input("Type the correct word here! (not letter of your choice .)")
    
    if answer2.lower() in ["after"]:
        hide screen question2
        ct "Awesome! you got it right!"
        ct "Explanation: The sentence describes two events that happened one after the other. (After) is the correct word to use to connect the two events."
        $ player_score += 1
        jump puzzle3

    $ player_score -= 1
    $ lives -= 1
    hide screen question2
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle2

label puzzle3:
    show screen hearts
    show screen question3

    $ answer3 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer3.lower() in ["scolded"]:
        hide screen question3
        ct "Awesome! you got it right!"
        ct "Explanation: (Scolded) means to reprimand or criticize someone for their behavior or actions. It is the most appropriate word to use in this context."
        $ player_score += 1
        jump puzzle4
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question3
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle3

label puzzle4:
    show screen hearts
    show screen question4
    $ answer4 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer4.lower() in ["sad"]:
        hide screen question4
        ct "Isane! Way to go [player_name]!"
        ct "Explanation: (Sad) means feeling or showing sorrow; unhappy. It is the most appropriate word to use in this context."
        $ player_score += 1
        jump puzzle5

    $ player_score -= 1
    $ lives -= 1

    hide screen question4
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. hehe ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle4

label puzzle5:
    show screen hearts
    show screen question5
    $ answer5 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer5.lower() in ["disappointing"]:
        hide screen question5
        ct "Wonderful [player_name]!"
        ct "Explanation: (Disappointing) means failing to meet expectations; not fulfilling hopes or desires. It is the most appropriate word to use in this context."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        jump scoref2
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question5
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle5

label scoref2:
    hide screen hearts
    "your score: [player_score]/10"
    jump progress2

label progress2:
    if player_score >= 5:
        jump firstvillainwin
    else:
        jump firstvillainlose

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


#vocabulary
label puzzle6:
    show screen hearts
    show screen question6
    $ answer6 = renpy.input("enter your asnwer here!")

    if answer6.lower() in ["a"]:
        hide screen question6
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Apprehensive' means feeling anxious or fearful about the future or something that might happen. It is often used to describe a sense of uncertainty or uneasiness."
        $ player_score += 1
        jump puzzle7
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question6
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle6

label puzzle7:
    show screen hearts
    show screen question7
    $ answer7 = renpy.input("enter your asnwer here!")

    if answer7.lower() in ["b"]:
        hide screen question7
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Conjecture' refers to a conclusion or opinion that is based on incomplete information or evidence. It is often used in academic or scientific contexts to describe a hypothesis or educated guess."
        $ player_score += 1
        jump puzzle8
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question7
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle7

label puzzle8:
    show screen hearts
    show screen question8
    $ answer8 = renpy.input("enter your asnwer here!")

    if answer8.lower() in ["a"]:
        hide screen question8
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Diligent' means working hard and being careful and thorough in one's tasks. It is often used to describe someone who is focused and committed to achieving their goals."
        $ player_score += 1
        jump puzzle9
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question8
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle8

label puzzle9:
    show screen hearts
    show screen question9
    $ answer9 = renpy.input("enter your asnwer here!")

    if answer9.lower() in ["a"]:
        hide screen question9
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Indignant' means feeling anger or irritation in response to something that is perceived as unfair or unjust. It is often used to describe a sense of moral outrage or indignation."
        $ player_score += 1
        jump puzzle10
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question9
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump puzzle9

label puzzle10:
    show screen hearts
    show screen question10
    $ answer10 = renpy.input("enter your asnwer here!")

    if answer10.lower() in ["d"]:
        hide screen question10
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Resilient' means being able to bounce back quickly from difficult or challenging situations. It is often used to describe a person or organization that is able to adapt and recover from setbacks."
        $ player_score += 1
        jump scoref3
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question10
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump scoref3

label scoref3:
    hide screen hearts
    "your final score: [player_score]/10"
    jump progress3

label progress3:
    if player_score >= 5:
        jump thirdvillainwin
    else:
        jump thirdvillainlose
