init python:
    def next_rnd_in_list( theList ):
        last_used = theList.pop(0)
        renpy.random.shuffle(theList)
        theList.append(last_used)
        return theList[0]


    question_masterlist = [ "question_001", "question_002", "question_003", "question_004", "question_005", "question_006", "question_007", "question_008", "question_009", "question_010", "question_011", "question_012", "question_013", "question_014", "question_015", "question_016", "question_017", "question_018", "question_019", "question_020",]
    question_masterlist1 = [ "bquestion_001", "bquestion_002", "bquestion_003", "bquestion_004", "bquestion_005", "bquestion_006", "bquestion_007", "bquestion_008", "bquestion_009", "bquestion_010", "bquestion_011", "bquestion_012", "bquestion_013", "bquestion_014", "bquestion_015", "bquestion_016", "bquestion_017", "bquestion_018", "bquestion_019", "bquestion_020",]
    question_masterlist2 = [ "gpquestion_001", "gpquestion_002", "gpquestion_003", "gpquestion_004", "gpquestion_005", "gpquestion_006", "gpquestion_007", "gpquestion_008", "gpquestion_009", "gpquestion_010"]
    question_masterlist3 = [ "gpquestion_011", "gpquestion_012", "gpquestion_013", "gpquestion_014", "gpquestion_015", "gpquestion_016", "gpquestion_017", "gpquestion_018", "gpquestion_019", "gpquestion_020"]
    question_masterlist4 = [ "bpquestion_001", "bpquestion_002", "bpquestion_003", "bpquestion_004", "bpquestion_005", "bpquestion_006", "bpquestion_007", "bpquestion_008", "bpquestion_009", "bpquestion_010"]
    question_masterlist5 = [ "bpquestion_011", "bpquestion_012", "bpquestion_013", "bpquestion_014", "bpquestion_015", "bpquestion_016", "bpquestion_017", "bpquestion_018", "bpquestion_019", "bpquestion_020"]
    question_masterlist6 = [ "bround2", "bround3"]
    # question_masterlist3 = [ "bquestion_001", "bquestion_002", "bquestion_003", "bquestion_004", "bquestion_005", "bquestion_006", "bquestion_007", "bquestion_008", "bquestion_009", "bquestion_010"]
    
label gquiz1():
    show screen gameUI
    show screen rewardbutton
    show screen hearts
    show screen books

    call expression next_rnd_in_list( question_masterlist1)

    if _return == "pass":
        call expression next_rnd_in_list(question_masterlist1)

        if _return == "pass":
            call expression next_rnd_in_list(question_masterlist1)
            
            if _return == "pass":
                call expression next_rnd_in_list(question_masterlist1)

                if _return == "pass":
                    call expression next_rnd_in_list(question_masterlist1)

                    if _return == "pass":
                        call expression next_rnd_in_list(question_masterlist1)

                        if _return == "pass":
                            call expression next_rnd_in_list(question_masterlist1)

                            if _return == "pass":
                                call expression next_rnd_in_list(question_masterlist1)  

                                if _return == "pass":
                                    call expression next_rnd_in_list(question_masterlist1)   
                                       
                                    if _return == "pass":
                                        call expression next_rnd_in_list(question_masterlist1)      
                
                                        if _return == "pass":
                                            n "nice you got it"
                                            jump gscoref
    
    return
                

label question_001:

    ct "question"
    menu(question="What is an adjective?"):
        "a. A word that describes a noun or pronoun":
            $ player_score += 1
            return "pass"
        "b. A word that replaces a noun":
            pass
        "c. A word that describes a verb":
            pass
        "d. A word that connects two ideas":
            pass

    $ player_score -= 1
    $ lives -= 1

    show girlupset at right with hpunch
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump question_001

label question_002:
    ct "question"
    # Answer: a) A word that describes a verb, adjective, or other adverb
    menu (question="What is an adverb?"):
        "a. A word that describes a verb, adjective, or other adverb":
            $ player_score += 1
            return "pass"
        "b. A word that connects two ideas":
            pass
        "c. A word that replaces a noun":
            pass
        "d. A word that describes a noun or pronoun":
            pass

    $ player_score -= 1
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump question_002

label question_003:
    ct "question"
    # Answer: b) beautiful
    menu (question="Which of the following is an example of an adjective?"):
        "a. quickly":
            pass
        "b. beautiful":
            $ player_score += 1
            return "pass"
        "c. they":
            pass
        "d. who":
            pass   

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_003

label question_004:
    ct "question"
    # Answer: b) slowly
    menu (question="Which of the following is an example of an adverb?"):
        "a. happy":
            pass
        "b. slowly":
            $ player_score += 1
            return "pass"
        "c. her":
            pass
        "d. we":
            pass    

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_004

label question_005:
    ct "question"
    # Answer: c) he
    menu (question="Which of the following is a pronoun?"):
        "a. happy":
            pass
        "b. quickly":
            pass
        "c. he":
            $ player_score += 1
            return "pass"
        "d. sweet":
            pass    

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_005

label question_006:
    ct "question"
    # Answer: d) they
    menu (question="Which of the following is an example of a personal pronoun?"):
        "a. myself":
            pass
        "b. this":
            pass
        "c. your":
            pass
        "d. they":
            $ player_score += 1
            return "pass"

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_006

label question_007:
    # Answer: c) my
    ct "Question"
    menu (question="Which of the following is an example of a possessive pronoun"):
        "a. they":
            pass
        "b. me":
            pass
        "c. my":
            $ player_score += 1
            return "pass"
        "d. he":
            pass 

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_007

label question_008:
    # Answer: a) this
    ct "Question"
    menu (question="Which of the following is an example of a demonstrative pronoun?"):
        "a. this":
            $ player_score += 1
            return "pass"
        "b. him":
            pass
        "c. herself":
            pass
        "d. ourselves":
            pass     

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_008

label question_009:
    # Answer: b) anyone
    ct "Question"
    menu (question="Which of the following is an example of an indefinite pronoun?"):
        "a. those":
            pass
        "b. anyone":
            $ player_score += 1
            return "pass"
        "c. these":
            pass
        "d. both":
            pass   

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_009

label question_010:
    ct "question"
    # Answer: d) all of the above
    
    menu (question="Which of the following is an example of a reflexive pronoun?"):
        "a. herself":
            pass
        "b. ourselves":
            pass
        "c. himself":
            pass
        "d. all of the above":
            $ player_score += 1 
            return "pass"

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_010

label question_011:
    ct "question"
    # Answer: d) The red car drove by.

    menu (question="Which of the following sentences contains an adjective?"):
        "a. She sang beautifully.":
            pass
        "b. He walked quickly.":
            pass
        "c. They arrived early.":
            pass
        "d. The red car drove by.":
            $ player_score += 1 
            return "pass"

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_011

label question_012:
    ct "question"
    # Answer: c) They studied hard for the exam.
    
    menu (question="Which of the following sentences contains an adverb?"):
        "a. She wore a pretty dress.":
            pass
        "b. He is a fast runner.":
            pass
        "c. They studied hard for the exam.":
            $ player_score += 1 
            return "pass"
        "d.  The cat chased the mouse.":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_012

label question_013:
    ct "question"
    # Answer: b) The teacher gave us homework.
    
    menu (question="Which of the following sentences contains a pronoun?"):
        "a. The sun is shining brightly.":
            pass
        "b. The teacher gave us homework.":
            $ player_score += 1 
            return "pass"
        "c. The children played in the park.":
            pass
        "d. She is a doctor.":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_013

label question_014:
    ct "question"
    # Answer: c) They are going to the store.
    
    menu (question="Which of the following sentences contains a personal pronoun?"):
        "a. My sister loves to read.":
            pass
        "b. This is my favorite book.":
            pass
        "c. They are going to the store.":
            $ player_score += 1 
            return "pass"
        "d. He is a good friend.":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_014

label question_015:
    ct "question"
    # Answer: b) Her shoes are pink.
    
    menu (question="Which of the following sentences contains a possessive pronoun?"):
        "a. I have a cat.":
            pass
        "b. Her shoes are pink.":
            $ player_score += 1 
            return "pass"
        "c. Their dog barks a lot.":
            pass
        "d. Our house is big.":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_015

label question_016:
    ct "question"
    # Answer: a) This is my favorite song.
    
    menu (question="Which of the following sentences contains a demonstrative pronoun?"):
        "a. This is my favorite song.":
            $ player_score += 1 
            return "pass"
        "b. She likes to dance.":
            pass
        "c. They went to the beach.":
            pass
        "d. He is a kind person.":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_016

label question_017:
    ct "question"
    # Answer: a) Everyone should do their best.
    
    menu (question="Which of the following sentences contains an indefinite pronoun?"):
        "a. Everyone should do their best.":
            $ player_score += 1 
            return "pass"
        "b. My aunt likes to read mystery novels.":
            pass
        "c. The bicycle belongs to the girl in the blue dress.":
            pass
        "d. He is a doctor and a teacher.":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_017

label question_018:
    ct "question"
    # Answer: a) I gave myself a pat on the back.
    
    menu (question="Which of the following sentences contains a reflexive pronoun?"):
        "a. I gave myself a pat on the back.":
            $ player_score += 1 
            return "pass"
        "b. She made the cake for herself.":
            pass
        "c. He fixed the car by himself.":
            pass
        "d. They talked to each other for hours.":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_018

label question_019:
    ct "question"
    # Answer: b) She sings beautifully and loudly.
    
    menu (question="Which of the following sentences contains both an adjective and an adverb?"):
        "a. The dog barked loudly.":
            pass
        "b. She sings beautifully and loudly.":
            $ player_score += 1 
            return "pass"
        "c. He ran quickly to the store.":
            pass
        "d. They danced gracefully.":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_019

label question_020:
    ct "question"
    # Answer: c) She and he played tennis.
    
    menu (question="Which of the following sentences contains a pronoun used as a subject?"):
        "a. Him and I went to the store.":
            pass
        "b. They gave the book to her and me.":
            pass
        "c. She and he played tennis.":
            $ player_score += 1 
            return "pass"
        "d. Whom did you invite to the party?":
            pass

    $ player_score -= 1     
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump question_020

#player nagivation after the quiz
label gscoref:
    "your final score: [player_score]"
    jump gprogress1

label gprogress1:
    if player_score >= 15:
        jump gthirdvillainwin
    else:
        jump gthirdvillainlose
