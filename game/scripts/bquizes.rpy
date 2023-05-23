label bquiz1():
    show screen gameUI
    show screen rewardbutton
    show screen hearts
    show screen books

    call expression next_rnd_in_list( question_masterlist1 )

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
                                            jump bscoref
    
    return
                

label bquestion_001:

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

    show boyupset at right with hpunch
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bquestion_001

label bquestion_002:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game

    jump bquestion_002

label bquestion_003:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_003

label bquestion_004:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_004

label bquestion_005:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_005

label bquestion_006:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_006

label bquestion_007:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_007

label bquestion_008:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_008

label bquestion_009:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_009

label bquestion_010:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_010

label bquestion_011:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_011

label bquestion_012:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_012

label bquestion_013:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_013

label bquestion_014:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_014

label bquestion_015:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_015

label bquestion_016:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_016

label bquestion_017:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_017

label bquestion_018:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_018

label bquestion_019:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_019

label bquestion_020:
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

    show boyupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide boyupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump bquestion_020

#player nagivation after the quiz
label bscoref:
    "your final score: [player_score]"
    jump bprogress1

label bprogress1:
    if player_score >= 15:
        jump bthirdvillainwin
    else:
        jump bthirdvillainlose
