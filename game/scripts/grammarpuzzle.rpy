label gpuzzle1:
    show screen hearts
    show screen question1
    $ answer1 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer1.lower() in ["your"]:
        $ player_score += 1
        hide screen question1
        ct "Wonderful! guess you have a knacked on this thing. Now lets spice things up ;)"
        jump gpuzzle2

    $ player_score -= 1
    $ lives -= 1
    hide screen question1
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle1

label gpuzzle2:
    show screen hearts
    show screen question2
    $ answer2 = renpy.input("Type the correct word here! (not letter of your choice .)")
    
    if answer2.lower() in ["after"]:
        hide screen question2
        ct "Awesome! you got it right!"
        ct "Explanation: The sentence describes two events that happened one after the other. (After) is the correct word to use to connect the two events."
        $ player_score += 1
        jump gpuzzle3

    $ player_score -= 1
    $ lives -= 1
    hide screen question2
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle2

label gpuzzle3:
    show screen hearts
    show screen question3

    $ answer3 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer3.lower() in ["scolded"]:
        hide screen question3
        ct "Awesome! you got it right!"
        ct "Explanation: (Scolded) means to reprimand or criticize someone for their behavior or actions. It is the most appropriate word to use in this context."
        $ player_score += 1
        jump gpuzzle4
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question3
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle3

label gpuzzle4:
    show screen hearts
    show screen question4
    $ answer4 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer4.lower() in ["sad"]:
        hide screen question4
        ct "Isane! Way to go [player_name]!"
        ct "Explanation: (Sad) means feeling or showing sorrow; unhappy. It is the most appropriate word to use in this context."
        $ player_score += 1
        jump gpuzzle5

    $ player_score -= 1
    $ lives -= 1

    hide screen question4
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. hehe ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle4

label gpuzzle5:
    show screen hearts
    show screen question5
    $ answer5 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer5.lower() in ["disappointing"]:
        hide screen question5
        ct "Wonderful [player_name]!"
        ct "Explanation: (Disappointing) means failing to meet expectations; not fulfilling hopes or desires. It is the most appropriate word to use in this context."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        jump gscoref2
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question5
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle5

label gscoref2:
    hide screen hearts
    "your score: [player_score]"
    jump gprogress2

label gprogress2:
    if player_score >= 5:
        jump gfirstvillainwin
    else:
        jump gfirstvillainlose


#vocabulary
label gpuzzle6:
    show screen hearts
    show screen question6
    $ answer6 = renpy.input("enter the letter of the correct answer here.")

    if answer6.lower() in ["a"]:
        hide screen question6
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Apprehensive' means feeling anxious or fearful about the future or something that might happen. It is often used to describe a sense of uncertainty or uneasiness."
        $ player_score += 1
        jump gpuzzle7
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question6
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle6

label gpuzzle7:
    show screen hearts
    show screen question7
    $ answer7 = renpy.input("enter the lette of the correct answer ")

    if answer7.lower() in ["b"]:
        hide screen question7
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Conjecture' refers to a conclusion or opinion that is based on incomplete information or evidence. It is often used in academic or scientific contexts to describe a hypothesis or educated guess."
        $ player_score += 1
        jump gpuzzle8
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question7
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle7

label gpuzzle8:
    show screen hearts
    show screen question8
    $ answer8 = renpy.input("enter the lette of the correct answer ")

    if answer8.lower() in ["a"]:
        hide screen question8
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Diligent' means working hard and being careful and thorough in one's tasks. It is often used to describe someone who is focused and committed to achieving their goals."
        $ player_score += 1
        jump gpuzzle9
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question8
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle8

label gpuzzle9:
    show screen hearts
    show screen question9
    $ answer9 = renpy.input("enter the lette of the correct answer ")

    if answer9.lower() in ["a"]:
        hide screen question9
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Indignant' means feeling anger or irritation in response to something that is perceived as unfair or unjust. It is often used to describe a sense of moral outrage or indignation."
        $ player_score += 1
        jump gpuzzle10
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question9
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpuzzle9

label gpuzzle10:
    show screen hearts
    show screen question10
    $ answer10 = renpy.input("enter the lette of the correct answer ")

    if answer10.lower() in ["d"]:
        hide screen question10
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Resilient' means being able to bounce back quickly from difficult or challenging situations. It is often used to describe a person or organization that is able to adapt and recover from setbacks."
        $ player_score += 1
        jump gscoref3
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question10
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump scoref3

label gscoref3:
    hide screen hearts
    "your final score: [player_score]"
    jump gprogress3

label gprogress3:
    if player_score >= 5:
        jump gthirdvillainwin
    else:
        jump gthirdvillainlose
