label bpquiz1():
    show screen gameUI
    show screen rewardbutton
    show screen hearts
    show screen books

    call expression next_rnd_in_list(question_masterlist4)

    if _return == "pass":
        call expression next_rnd_in_list(question_masterlist4)

        if _return == "pass":
            call expression next_rnd_in_list(question_masterlist4)
            
            if _return == "pass":
                call expression next_rnd_in_list(question_masterlist4)   

                if _return == "pass":
                    call expression next_rnd_in_list(question_masterlist4)    
                
                    if _return == "pass":
                        n "nice you got it"
                        jump bscoref2
    
    return

label bpquestion_001:
    show screen question1
    $ answer1 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer1.lower() in ["your"]:
        $ player_score += 1
        hide screen question1
        ct "Wonderful! guess you have a knacked on this thing. Now lets spice things up ;)"

        return "pass"

    $ player_score -= 1
    $ lives -= 1

    hide screen question1
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_001

label bpquestion_002:
    show screen question2
    $ answer2 = renpy.input("Type the correct word here! (not letter of your choice .)")
    
    if answer2.lower() in ["after"]:
        hide screen question2
        ct "Awesome! you got it right!"
        ct "Explanation: The sentence describes two events that happened one after the other. (After) is the correct word to use to connect the two events."
        $ player_score += 1
        return "pass"

    $ player_score -= 1
    $ lives -= 1

    hide screen question2
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_002

label bpquestion_003:
    show screen question3

    $ answer3 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer3.lower() in ["scolded"]:
        hide screen question3
        ct "Awesome! you got it right!"
        ct "Explanation: (Scolded) means to reprimand or criticize someone for their behavior or actions. It is the most appropriate word to use in this context."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question3
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_003

label bpquestion_004:
    show screen question4
    $ answer4 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer4.lower() in ["sad"]:
        hide screen question4
        ct "Insane! Way to go [player_name]!"
        ct "Explanation: (Sad) means feeling or showing sorrow; unhappy. It is the most appropriate word to use in this context."
        $ player_score += 1
        return "pass"

    $ player_score -= 1
    $ lives -= 1

    hide screen question4
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. hehe ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_004

label bpquestion_005:
    show screen question5
    $ answer5 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer5.lower() in ["disappointing"]:
        hide screen question5
        ct "Wonderful [player_name]!"
        ct "Explanation: (Disappointing) means failing to meet expectations; not fulfilling hopes or desires. It is the most appropriate word to use in this context."
         
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question5
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_005

label bpquestion_006:
    show screen question6
    $ answer6 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer6.lower() in ["doesn't"]:
        hide screen question6
        ct "Wonderful [player_name]!"
        ct "Explanation: In this sentence, the correct verb form to use with the pronoun he is doesn't, which is the contraction of does not."
         
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question6
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_006

label bpquestion_007:
    show screen question7
    $ answer7 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer7.lower() in ["has"]:
        hide screen question7
        ct "Wonderful [player_name]!"
        ct "Explanation: When talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."
         
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question7
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_007

label bpquestion_008:
    show screen question8
    $ answer8 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer8.lower() in ["went"]:
        hide screen question8
        ct "Wonderful [player_name]!"
        ct "Explanation: The past tense of the verb go is went. Therefore, option B is the correct sentence in the past tense."
         
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question8
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_008

label bpquestion_009:
    show screen question9
    $ answer9 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer9.lower() in ["are"]:
        hide screen question9
        ct "Wonderful [player_name]!"
        ct "Explanation: The pronoun they requires the verb form are to show the plural subject in the present tense."
         
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question9
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_009

label bpquestion_010:
    show screen question10
    $ answer10 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer10.lower() in ["didn't go"]:
        hide screen question10
        ct "Wonderful [player_name]!"
        ct "Explanation: When negating a sentence in the past tense, we use the auxiliary verb did and the base form of the main verb, which is go in this case."
         
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question10
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_010

label bscoref2:
    "your score: [player_score]"
    jump bprogress2

label bprogress2:
    if player_score == 5:
        jump bbround

    if player_score >= 3:
        jump bfirstvillainwin

    jump bfirstvillainlose



#vocabulary
label bpquiz2():
    show screen gameUI
    show screen rewardbutton
    show screen hearts
    show screen books

    call expression next_rnd_in_list(question_masterlist5)

    if _return == "pass":
        call expression next_rnd_in_list(question_masterlist5)

        if _return == "pass":
            call expression next_rnd_in_list(question_masterlist5)
            
            if _return == "pass":
                call expression next_rnd_in_list(question_masterlist5)    

                if _return == "pass":
                    call expression next_rnd_in_list(question_masterlist5)   
                     
                    if _return == "pass":
                        call expression next_rnd_in_list(question_masterlist5)    

                        if _return == "pass":
                            call expression next_rnd_in_list(question_masterlist5)    
                        
                            if _return == "pass":
                                n "nice you got it"
                                jump bscoref3
    
    return

label bpquestion_011:
    show screen question11
    $ answer11 = renpy.input("enter the letter of the correct answer here.")

    if answer11.lower() in ["a"]:
        hide screen question11
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Apprehensive' means feeling anxious or fearful about the future or something that might happen. It is often used to describe a sense of uncertainty or uneasiness."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question11
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_011

label bpquestion_012:
    show screen question12
    $ answer12 = renpy.input("enter the letter of the correct answer ")

    if answer12.lower() in ["b"]:
        hide screen question12
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Conjecture' refers to a conclusion or opinion that is based on incomplete information or evidence. It is often used in academic or scientific contexts to describe a hypothesis or educated guess."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question12
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_012

label bpquestion_013:
    show screen question13
    $ answer13 = renpy.input("enter the letter of the correct answer ")

    if answer13.lower() in ["a"]:
        hide screen question13
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Diligent' means working hard and being careful and thorough in one's tasks. It is often used to describe someone who is focused and committed to achieving their goals."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question13
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_013

label bpquestion_014:
    show screen question14
    $ answer14 = renpy.input("enter the letter of the correct answer ")

    if answer14.lower() in ["a"]:
        hide screen question14
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Indignant' means feeling anger or irritation in response to something that is perceived as unfair or unjust. It is often used to describe a sense of moral outrage or indignation."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question14
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_014

label bpquestion_015:
    show screen question15
    $ answer15 = renpy.input("enter the letter of the correct answer ")

    if answer15.lower() in ["d"]:
        hide screen question15
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Resilient' means being able to bounce back quickly from difficult or challenging situations. It is often used to describe a person or organization that is able to adapt and recover from setbacks."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question15
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_015

label bpquestion_016:
    show screen question16
    $ answer16 = renpy.input("enter the letter of the correct answer ")

    if answer16.lower() in ["b"]:
        hide screen question16
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Furious' describes a state of extreme anger or rage."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question16
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_016

label bpquestion_017:
    show screen question17
    $ answer17 = renpy.input("enter the letter of the correct answer ")

    if answer17.lower() in ["b"]:
        hide screen question17
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Condemn' means to express strong disapproval or criticism towards someone "
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question17
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_017

label bpquestion_018:
    show screen question18
    $ answer18 = renpy.input("enter the letter of the correct answer ")

    if answer18.lower() in ["b"]:
        hide screen question18
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Mourn' refers to the act of feeling or expressing deep sorrow or regret, often in response to a loss or tragedy."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question18
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_018

label bpquestion_019:
    show screen question19
    $ answer19 = renpy.input("enter the letter of the correct answer ")

    if answer19.lower() in ["d"]:
        hide screen question19
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Request' means to make a formal or polite appeal or solicitation for something."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question19
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_019

label bpquestion_020:
    show screen question20
    $ answer20 = renpy.input("enter the letter of the correct answer ")

    if answer20.lower() in ["a"]:
        hide screen question20
        ct "Wonderful [player_name]!"
        ct "Explanation: 'Terrify' means to cause intense fear, fright, or distress in someone."
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question20
    show boyworried at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide boyworried with dissolve

    if lives <= 0:
        jump end_game2

    jump bpquestion_020

label bscoref3:
    "your final score: [player_score]"
    jump bprogress3

label bprogress3:
    if player_score == 12:
        jump bbroundd

    if player_score >= 8:
        jump bsecondvillainwin

    jump bsecondvillainlose


label bbround:
    window hide

    show screen bonusimage

    pause 

    hide screen bonusimage

    pause 0.5

    call expression next_rnd_in_list(question_masterlist6) 
            
    if _return == "pass":

        jump bfirstvillainwin

    elif _return == "fail":
        ct "Awhhhhh You missed the bonus round :'(. Better luck next time!"

        jump bfirstvillainlose
    
    return

label bbroundd:
    window hide

    show screen bonusimage

    pause 

    hide screen bonusimage

    pause 0.5

    call expression next_rnd_in_list(question_masterlist6) 
            
    if _return == "pass":

        jump bsecondvillainwin

    elif _return == "fail":
        ct "Awhhhhh You missed the bonus round :'(. Better luck next time!"

        jump bsecondvillainlose
    
    return