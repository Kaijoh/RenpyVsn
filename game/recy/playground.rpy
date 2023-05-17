label test:
    show pic_10








    # final(put in boy route and girl route)
    show screen gameUI
    show screen rewardbutton
    pause


label gpquiz1():
    show screen gameUI
    show screen rewardbutton
    show screen hearts
    show screen books

    call expression next_rnd_in_list( question_masterlist2)

    if _return == "pass":
        call expression next_rnd_in_list(question_masterlist2)

        if _return == "pass":
            call expression next_rnd_in_list(question_masterlist2)
            
            if _return == "pass":
                call expression next_rnd_in_list(question_masterlist2)    
            
                if _return == "pass":
                    n "nice you got it"
                    jump bscoref2
    
    return

label gpquestion_001:
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
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_001

label gpquestion_002:
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
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_002

label gpquestion_003:
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
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_003

label gpquestion_004:
    show screen question4
    $ answer4 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer4.lower() in ["sad"]:
        hide screen question4
        ct "Isane! Way to go [player_name]!"
        ct "Explanation: (Sad) means feeling or showing sorrow; unhappy. It is the most appropriate word to use in this context."
        $ player_score += 1
        return "pass"

    $ player_score -= 1
    $ lives -= 1

    hide screen question4
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. hehe ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_004

label gpquestion_005:
    show screen question5
    $ answer5 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer5.lower() in ["disappointing"]:
        hide screen question5
        ct "Wonderful [player_name]!"
        ct "Explanation: (Disappointing) means failing to meet expectations; not fulfilling hopes or desires. It is the most appropriate word to use in this context."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question5
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_005

label gpquestion_006:
    show screen question6
    $ answer6 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer6.lower() in ["doesn't"]:
        hide screen question6
        ct "Wonderful [player_name]!"
        ct "Explanation: In this sentence, the correct verb form to use with the pronoun he is doesn't, which is the contraction of does not."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question6
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_006

label gpquestion_007:
    show screen question7
    $ answer7 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer7.lower() in ["has"]:
        hide screen question7
        ct "Wonderful [player_name]!"
        ct "Explanation: When talking about the third person singular (she, he, it), we use the verb form has to indicate possession or presence."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question7
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_007

label gpquestion_008:
    show screen question8
    $ answer8 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer8.lower() in ["went"]:
        hide screen question8
        ct "Wonderful [player_name]!"
        ct "Explanation: The past tense of the verb go is went. Therefore, option B is the correct sentence in the past tense."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question8
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_008

label gpquestion_009:
    show screen question9
    $ answer9 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer9.lower() in ["are"]:
        hide screen question9
        ct "Wonderful [player_name]!"
        ct "Explanation: The pronoun they requires the verb form are to show the plural subject in the present tense."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question9
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_009

label gpquestion_010:
    show screen question10
    $ answer10 = renpy.input("Type the correct word here! (not letter of your choice .)")

    if answer10.lower() in ["didn't go"]:
        hide screen question10
        ct "Wonderful [player_name]!"
        ct "Explanation: When negating a sentence in the past tense, we use the auxiliary verb did and the base form of the main verb, which is go in this case."
        r "wow [player_name], you're so great! now lets move to the next location of the other books page." 
        $ player_score += 1
        return "pass"
    
    $ player_score -= 1
    $ lives -= 1

    hide screen question10
    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump gpquestion_010




label gpquestion_011:

label gpquestion_012:

label gpquestion_013:

label gpquestion_014:

label gpquestion_015:

label gpquestion_016:

label gpquestion_017:

label gpquestion_018:

label gpquestion_019:

label gpquestion_020:




















# in this renpy line of codes im trying to randomize the question labels so that the player wont get the same question arrangement everytime he play the game and now i want to make it that the player gets to answer all the 3 question and then he answer all the 3 question correctly he jump to the next label

#the code:

# init python:
#     def next_rnd_in_list( theList ):
#         last_used = theList.pop(0)
#         renpy.random.shuffle(theList)
#         theList.append(last_used)
#         return theList[0]


#     question_masterlist = [ "bquestion_001", "bquestion_002", "bquestion_003", "bquestion_004", "bquestion_005", "bquestion_006", "bquestion_007", "bquestion_008", "bquestion_009", "bquestion_010", "bquestion_011", "bquestion_012", "bquestion_013", "bquestion_014", "bquestion_015", "bquestion_016", "bquestion_017", "bquestion_018", "bquestion_019", "bquestion_020",]
#     question_masterlist = [ "question_001", "question_002", "question_003", "question_004", "question_005", "question_006", "question_007", "question_008", "question_009", "question_010", "question_011", "question_012", "question_013", "question_014", "question_015", "question_016", "question_017", "question_018", "question_019", "question_020",]

# label btest():
#     show screen gameUI
#     show screen rewardbutton
#     show screen hearts

#     call expression next_rnd_in_list( question_masterlist )

#     if _return == "pass":
#         call expression next_rnd_in_list(question_masterlist)

#         if _return == "pass":
#             call expression next_rnd_in_list(question_masterlist)
            
#             if _return == "pass":
#                 call expression next_rnd_in_list(question_masterlist)

#                 if _return == "pass":
#                     call expression next_rnd_in_list(question_masterlist)

#                     if _return == "pass":
#                         call expression next_rnd_in_list(question_masterlist)

#                         if _return == "pass":
#                             call expression next_rnd_in_list(question_masterlist)

#                             if _return == "pass":
#                                 call expression next_rnd_in_list(question_masterlist)  

#                                 if _return == "pass":
#                                     call expression next_rnd_in_list(question_masterlist)      
             
#                                     if _return == "pass":
#                                         n "nice you got it"
#                                         jump gscoref
                

# label bquestion_001():

#     ct "question"
#     menu(question="What is an adjective?"):
#         "a. A word that describes a noun or pronoun":
#             $ player_score += 1
#             return "pass"
#         "b. A word that replaces a noun":
#             pass
#         "c. A word that describes a verb":
#             pass
#         "d. A word that connects two ideas":
#             pass

#     $ player_score -= 1
#     $ lives -= 1

#     show girlupset at right with hpunch
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game

#     return "bquestion_001"

# label bquestion_002():
#     ct "question"
#     # Answer: a) A word that describes a verb, adjective, or other adverb
#     menu (question="What is an adverb?"):
#         "a. A word that describes a verb, adjective, or other adverb":
#             $ player_score += 1
#             return "pass"
#         "b. A word that connects two ideas":
#             pass
#         "c. A word that replaces a noun":
#             pass
#         "d. A word that describes a noun or pronoun":
#             pass

#     $ player_score -= 1
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game

#     return "bquestion_002"

# label bquestion_003():
#     ct "question"
#     # Answer: b) beautiful
#     menu (question="Which of the following is an example of an adjective?"):
#         "a. quickly":
#             pass
#         "b. beautiful":
#             $ player_score += 1
#             return "pass"
#         "c. they":
#             pass
#         "d. who":
#             pass   

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_003"

# label bquestion_004():
#     ct "question"
#     # Answer: b) slowly
#     menu (question="Which of the following is an example of an adverb?"):
#         "a. happy":
#             pass
#         "b. slowly":
#             $ player_score += 1
#             return "pass"
#         "c. her":
#             pass
#         "d. we":
#             pass    

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_004"

# label bquestion_005():
#     ct "question"
#     # Answer: c) he
#     menu (question="Which of the following is a pronoun?"):
#         "a. happy":
#             pass
#         "b. quickly":
#             pass
#         "c. he":
#             $ player_score += 1
#             return "pass"
#         "d. sweet":
#             pass    

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_005"

# label bquestion_006():
#     ct "question"
#     # Answer: d) they
#     menu (question="Which of the following is an example of a personal pronoun?"):
#         "a. myself":
#             pass
#         "b. this":
#             pass
#         "c. your":
#             pass
#         "d. they":
#             $ player_score += 1
#             return "pass"

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_006"

# label bquestion_007():
#     # Answer: c) my
#     ct "Question"
#     menu (question="Which of the following is an example of a possessive pronoun"):
#         "a. they":
#             pass
#         "b. me":
#             pass
#         "c. my":
#             $ player_score += 1
#             return "pass"
#         "d. he":
#             pass 

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_007"

# label bquestion_008():
#     # Answer: a) this
#     ct "Question"
#     menu (question="Which of the following is an example of a demonstrative pronoun?"):
#         "a. this":
#             $ player_score += 1
#             return "pass"
#         "b. him":
#             pass
#         "c. herself":
#             pass
#         "d. ourselves":
#             pass     

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_008"

# label bquestion_009():
#     # Answer: b) anyone
#     ct "Question"
#     menu (question="Which of the following is an example of an indefinite pronoun?"):
#         "a. those":
#             pass
#         "b. anyone":
#             $ player_score += 1
#             return "pass"
#         "c. these":
#             pass
#         "d. both":
#             pass   

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_009"

# label bquestion_010():
#     ct "question"
#     # Answer: d) all of the above
    
#     menu (question="Which of the following is an example of a reflexive pronoun?"):
#         "a. herself":
#             pass
#         "b. ourselves":
#             pass
#         "c. himself":
#             pass
#         "d. all of the above":
#             $ player_score += 1 
#             return "pass"

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_010"

# label bquestion_011():
#     ct "question"
#     # Answer: d) The red car drove by.

#     menu (question="Which of the following sentences contains an adjective?"):
#         "a. She sang beautifully.":
#             pass
#         "b. He walked quickly.":
#             pass
#         "c. They arrived early.":
#             pass
#         "d. The red car drove by.":
#             $ player_score += 1 
#             return "pass"

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_011"

# label bquestion_012():
#     ct "question"
#     # Answer: c) They studied hard for the exam.
    
#     menu (question="Which of the following sentences contains an adverb?"):
#         "a. She wore a pretty dress.":
#             pass
#         "b. He is a fast runner.":
#             pass
#         "c. They studied hard for the exam.":
#             $ player_score += 1 
#             return "pass"
#         "d.  The cat chased the mouse.":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_012"

# label bquestion_013():
#     ct "question"
#     # Answer: b) The teacher gave us homework.
    
#     menu (question="Which of the following sentences contains a pronoun?"):
#         "a. The sun is shining brightly.":
#             pass
#         "b. The teacher gave us homework.":
#             $ player_score += 1 
#             return "pass"
#         "c. The children played in the park.":
#             pass
#         "d. She is a doctor.":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_013"

# label bquestion_014():
#     ct "question"
#     # Answer: c) They are going to the store.
    
#     menu (question="Which of the following sentences contains a personal pronoun?"):
#         "a. My sister loves to read.":
#             pass
#         "b. This is my favorite book.":
#             pass
#         "c. They are going to the store.":
#             $ player_score += 1 
#             return "pass"
#         "d. He is a good friend.":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_014"

# label bquestion_015():
#     ct "question"
#     # Answer: b) Her shoes are pink.
    
#     menu (question="Which of the following sentences contains a possessive pronoun?"):
#         "a. I have a cat.":
#             pass
#         "b. Her shoes are pink.":
#             $ player_score += 1 
#             return "pass"
#         "c. Their dog barks a lot.":
#             pass
#         "d. Our house is big.":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_015"

# label bquestion_016():
#     ct "question"
#     # Answer: a) This is my favorite song.
    
#     menu (question="Which of the following sentences contains a demonstrative pronoun?"):
#         "a. This is my favorite song.":
#             $ player_score += 1 
#             return "pass"
#         "b. She likes to dance.":
#             pass
#         "c. They went to the beach.":
#             pass
#         "d. He is a kind person.":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_016"

# label bquestion_017():
#     ct "question"
#     # Answer: a) Everyone should do their best.
    
#     menu (question="Which of the following sentences contains an indefinite pronoun?"):
#         "a. Everyone should do their best.":
#             $ player_score += 1 
#             return "pass"
#         "b. My aunt likes to read mystery novels.":
#             pass
#         "c. The bicycle belongs to the girl in the blue dress.":
#             pass
#         "d. He is a doctor and a teacher.":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_017"

# label bquestion_018():
#     ct "question"
#     # Answer: a) I gave myself a pat on the back.
    
#     menu (question="Which of the following sentences contains a reflexive pronoun?"):
#         "a. I gave myself a pat on the back.":
#             $ player_score += 1 
#             return "pass"
#         "b. She made the cake for herself.":
#             pass
#         "c. He fixed the car by himself.":
#             pass
#         "d. They talked to each other for hours.":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_018"

# label bquestion_019():
#     ct "question"
#     # Answer: b) She sings beautifully and loudly.
    
#     menu (question="Which of the following sentences contains both an adjective and an adverb?"):
#         "a. The dog barked loudly.":
#             pass
#         "b. She sings beautifully and loudly.":
#             $ player_score += 1 
#             return "pass"
#         "c. He ran quickly to the store.":
#             pass
#         "d. They danced gracefully.":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_019"

# label bquestion_020():
#     ct "question"
#     # Answer: c) She and he played tennis.
    
#     menu (question="Which of the following sentences contains a pronoun used as a subject?"):
#         "a. Him and I went to the store.":
#             pass
#         "b. They gave the book to her and me.":
#             pass
#         "c. She and he played tennis.":
#             $ player_score += 1 
#             return "pass"
#         "d. Whom did you invite to the party?":
#             pass

#     $ player_score -= 1     
#     $ lives -= 1

#     show girlupset at right with moveinbottom
#     ct "You got it wrong. Please review it again or do some research. ^_^..."
#     hide girlupset with dissolve

#     if lives <= 0:
#         jump end_game
    
#     return "bquestion_020"

























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

# screen pscore():
#     hbox:
#         xalign 0.02
#         yalign 0.2
#         frame:
#             background "#4b3b3b"
#             xalign 0.5
#             yalign 0.5
#             padding (10,20)
#             margin (0,0,0,0)
#             text "Score: [player_score]"

# screen plive():
#     hbox:
#         xalign 0.02
#         yalign 0.4
#         frame:
#             background "#4b3b3b"
#             xalign 0.5
#             yalign 0.5
#             padding (10,20)
#             margin (0,0,0,0)
#             text "+[lives]"