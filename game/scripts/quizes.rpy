label quiz1:
    show screen fullbooks
    show screen books
    
    ct "Question Number 1..."
    menu (question="1. What is an adjective?"):
        "a. A word that describes a noun or pronoun":
            $ player_score += 1
            jump quiz2
        "b. A word that replaces a noun":
            pass
        "c. A word that describes a verb":
            pass
        "d. A word that connects two ideas":
            pass
    # show 
    $ player_score -= 1
    $ lives -= 1
    show girlupset at right with hpunch
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump quiz1

label quiz2:
    # Answer: a) A word that describes a verb, adjective, or other adverb
    ct "Question Number 2..."
    menu (question="2. What is an adverb?"):
        "a. A word that describes a verb, adjective, or other adverb":
            $ player_score += 1
            jump quiz3
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


    jump quiz2

label quiz3:
    # Answer: b) beautiful
    ct "Question Number 3..."
    menu (question="3. Which of the following is an example of an adjective?"):
        "a. quickly":
            pass
        "b. beautiful":
            $ player_score += 1
            jump quiz4
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
    
    jump quiz3

label quiz4:
    # Answer: b) slowly
    ct "Question Number 4..."
    menu (question="4. Which of the following is an example of an adverb?"):
        "a. happy":
            pass
        "b. slowly":
            $ player_score += 1
            jump quiz5
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
    
    jump quiz4

label quiz5:
    # Answer: c) he
    ct "Question Number 5..."
    menu (question="5. Which of the following is a pronoun?"):
        "a. happy":
            pass
        "b. quickly":
            pass
        "c. he":
            $ player_score += 1
            jump quiz6
        "d. sweet":
            pass   

    $ player_score -= 1
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump quiz5

label quiz6:
    # Answer: d) they
    ct "Question Number 6..."
    menu (question="6. Which of the following is an example of a personal pronoun?"):
        "a. myself":
            pass
        "b. this":
            pass
        "c. your":
            pass
        "d. they":
            $ player_score += 1
            jump quiz7  

    $ player_score -= 1
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump quiz6

label quiz7:
    # Answer: c) my
    ct "Question Number 7..."
    menu (question="7. Which of the following is an example of a possessive pronoun"):
        "a. they":
            pass
        "b. me":
            pass
        "c. my":
            $ player_score += 1
            jump quiz8
        "d. he":
            pass   

    $ player_score -= 1
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game
    
    jump quiz7

label quiz8:
    # Answer: a) this
    ct "Question Number 8..."
    menu (question="8. Which of the following is an example of a demonstrative pronoun?"):
        "a. this":
            $ player_score += 1
            jump quiz9
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
    
    jump quiz8

label quiz9:
    # Answer: b) anyone
    ct "Question Number 9..."
    menu (question="9. Which of the following is an example of an indefinite pronoun?"):
        "a. those":
            pass
        "b. anyone":
            $ player_score += 1
            jump quiz10
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
    
    jump quiz10

label quiz10:
    # Answer: d) all of the above
    ct "Question Number 10..."
    menu (question="10. Which of the following is an example of a reflexive pronoun?"):
        "a. herself":
            pass
        "b. ourselves":
            pass
        "c. himself":
            pass
        "d. all of the above":
            $ player_score += 1
            jump scoref 

    $ player_score -= 1
    $ lives -= 1

    show girlupset at right with moveinbottom
    ct "You got it wrong. Please review it again or do some research. ^_^..."
    hide girlupset with dissolve

    if lives <= 0:
        jump end_game

    jump quiz10

#player nagivation after the quiz
label scoref:
    hide screen hearts
    "your final score: [player_score]/10"
    jump progress1

label progress1:
    if player_score >= 7:
        jump secondvillainwin
    else:
        jump secondvillainlose
