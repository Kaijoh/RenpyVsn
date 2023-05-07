label bpuzzle1:
    show screen hearts
    show screen question1
    $ answer1 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer1.lower() in ["your"]:
        $ player_score += 1
        hide screen question1
        ct "Wonderful! guess you have a knacked on this thing. Now lets spice things up ;)"
        jump bpuzzle2

    $ player_score -= 1
    $ lives -= 1
    hide screen question1
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle1

label bpuzzle2:
    show screen hearts
    show screen question2
    $ answer2 = renpy.input("Type the correct word here! (not letter of your choice .)")
    
    if answer2.lower() in ["after"]:
        hide screen question2
        ct "Awesome! you got it right!"
        ct "Explanation: The sentence describes two events that happened one after the other. (After) is the correct word to use to connect the two events."
        $ player_score += 1
        jump bpuzzle3

    $ player_score -= 1
    $ lives -= 1
    hide screen question2
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle2

label bpuzzle3:
    show screen hearts
    show screen question3

    $ answer3 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer3.lower() in ["scolded"]:
        hide screen question3
        ct "Awesome! you got it right!"
        ct "Explanation: (Scolded) means to reprimand or criticize someone for their behavior or actions. It is the most appropriate word to use in this context."
        $ player_score += 1
        jump bpuzzle4
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question3
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle3

label bpuzzle4:
    show screen hearts
    show screen question4
    $ answer4 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer4.lower() in ["sad"]:
        hide screen question4
        ct "Isane! Way to go [player_name]!"
        ct "Explanation: (Sad) means feeling or showing sorrow; unhappy. It is the most appropriate word to use in this context."
        $ player_score += 1
        jump bpuzzle5

    $ player_score -= 1
    $ lives -= 1

    hide screen question4
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. hehe ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle4

label bpuzzle5:
    show screen hearts
    show screen question5
    $ answer5 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer5.lower() in ["disappointing"]:
        hide screen question5
        ct "Wonderful [player_name]!"
        ct "Explanation: (Disappointing) means failing to meet expectations; not fulfilling hopes or desires. It is the most appropriate word to use in this context."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        jump bscoref2
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question5
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle5

label bscoref2:
    "your score: [player_score]"
    jump bprogress2

label bprogress2:
    if player_score >= 5:
        jump bfirstvillainwin
    else:
        jump bfirstvillainlose


#vocabulary
label bpuzzle6:
    show screen hearts
    show screen question6
    $ answer6 = renpy.input("enter the letter of the correct answer here.")

    if answer6.lower() in ["a"]:
        hide screen question6
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Apprehensive' means feeling anxious or fearful about the future or something that might happen. It is often used to describe a sense of uncertainty or uneasiness."
        $ player_score += 1
        jump bpuzzle7
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question6
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle6

label bpuzzle7:
    show screen hearts
    show screen question7
    $ answer7 = renpy.input("enter the letter of the correct answer here.")

    if answer7.lower() in ["b"]:
        hide screen question7
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Conjecture' refers to a conclusion or opinion that is based on incomplete information or evidence. It is often used in academic or scientific contexts to describe a hypothesis or educated guess."
        $ player_score += 1
        jump bpuzzle8
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question7
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle7

label bpuzzle8:
    show screen hearts
    show screen question8
    $ answer8 = renpy.input("enter the letter of the correct answer here.")

    if answer8.lower() in ["a"]:
        hide screen question8
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Diligent' means working hard and being careful and thorough in one's tasks. It is often used to describe someone who is focused and committed to achieving their goals."
        $ player_score += 1
        jump bpuzzle9
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question8
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle8

label bpuzzle9:
    show screen hearts
    show screen question9
    $ answer9 = renpy.input("enter the letter of the correct answer here.")

    if answer9.lower() in ["a"]:
        hide screen question9
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Indignant' means feeling anger or irritation in response to something that is perceived as unfair or unjust. It is often used to describe a sense of moral outrage or indignation."
        $ player_score += 1
        jump bpuzzle10
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question9
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bpuzzle9

label bpuzzle10:
    show screen hearts
    show screen question10
    $ answer10 = renpy.input("enter the letter of the correct answer here.")

    if answer10.lower() in ["d"]:
        hide screen question10
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Resilient' means being able to bounce back quickly from difficult or challenging situations. It is often used to describe a person or organization that is able to adapt and recover from setbacks."
        $ player_score += 1
        jump bscoref3
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question10
    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump scoref3

label bscoref3:
    "your final score: [player_score]"
    jump bprogress3

label bprogress3:
    if player_score >= 5:
        jump bthirdvillainwin
    else:
        jump bthirdvillainlose
