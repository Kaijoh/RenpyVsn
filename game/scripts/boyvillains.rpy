#first monster

#grammar puzzle
label bfirstvillain:
    show greenmad at center with hpunch
    "OY OY OY! Look who is this."
    "A new kid? a kid from another world, perhaps?"
    "I am Mr.Green, the Slime."
    "Don't laugh at me kid! well anyways,,,, you are in my territory kid. Now before you get a pass here you must play with me first."
    "kekekekekekekekekekekeke."
    "Now lets start!"
    hide greenmad with dissolve

    show screen hearts
    show screen arrows
    show screen books
    window hide
    ct "Also before we start, see that 3 heart bar at the top left side?"
    ct "That would count as your lives, everytime you choose the wrong answer you will lose 1 life."
    ct "So make sure you read and answer all the question correctly. That's all and GOODLUCK [player_name]!"
    hide screen arrows with dissolve

    show blacks with dissolve 

    ct "EASY!"

    ct " GRAMMAR PUZZLE "
    
    hide blacks 
    show board with dissolve

    n "Now let's go through what grammar really is."
    
    ct "What is grammar?"
    
    n "Grammar, rules of a language governing the sounds, words, sentences, and other elements, as well as their combination and interpretation. The word grammar also denotes the study of these abstract features or a book presenting these rules."
    
    ct "What is its purpose?"
    
    n "Grammar explains the forms and structure of words (called morphology) and how they are arranged in sentences (called syntax). In other words, grammar provides the rules for common use of both spoken and written language so we can more easily understand each other."
    
    ct "Why grammar is important?"
    
    n "Grammar is important because it provides information that helps the reader's comprehension. It is the structure that conveys precise meaning from the writer to the audience. Eliminate grammatical errors from your writing, and reward your readers with clear communication."
    
    ct "LETS START! GOODLUCK!"
    hide board with dissolve


    
    jump bpquiz1

label bfirstvillainwin:
    show greensad at center with moveinbottom
    "Ughhhh.. You have beaten me in my own challenge :(. My brothers will avenge me!!!"
    "And if you want to get the next page, you must go to the magical cave."
    "That's where my brother resides and he's keeping an eye on that page. So you better watch out."
    "aight, see you kid."
    hide greensad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages

    jump bAct3_2

label bfirstvillainlose:
    show greenmad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide greenmad with dissolve
    jump bpquiz1

#second monster
#quiz
label bsecondvillain:
    show pic_12 with dissolve
    show bluemad at center with hpunch
    "OY OY OY! Look who is this."
    "The kid who beat my little brother."
    "I am Mr.Blue, the slime."
    "Don't laugh at me kid! well anyways, you are in my territory kid. Now before you get the next page you must play with me first."
    "kakakakakakakakakakakakakakakakka"
    "Now lets start"
    hide bluemad with dissolve

    window hide

    show blacks with dissolve 

    ct "MEDIUM!"

    ct " VOCABULARY PUZZLE "
    
    hide blacks 
    show board with dissolve

    n "Now let's go through what vocabulary really is."
    
    ct "What is vocabulary?"
    
    n "vocabulary, a list or collection of words or of words and phrases usually alphabetically arranged and explained or defined"
    
    ct "what is its purpose?"
    
    n "For many people, the word vocabulary is primarily associated with the number of words that a person knows; one either has a large or a small vocabulary."
    
    n "Vocabulary may indeed refer to the collection of words known by an individual or by a large group of people. It may also signify the body of specialized terms in a field of study or activity (“the vocabulary of science”). It may designate a physical object, such as a book, in which a collection of (usually alphabetized) words is defined or explained. And it may name things other than words, such as “a list or collection of terms or codes available for use,” “a set or list of nonverbal symbols” (such as marine alphabet flag signals), and “a set of expressive forms used in an art” (as in “the vocabulary of dance”)."
    
    ct "LETS START! GOODLUCK!"
    hide board with dissolve

    jump bpquiz2

label bsecondvillainwin:
    show bluesad at center with moveinbottom
    "Ughhhh... You have beaten me in my own challenge :(. My big brother will avenge me!!!"
    "But I'm not that bad, so I will tell you the next page location."
    "It's in the ruins where my third brother resides. So good luck, kid!"
    hide bluesad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages

    jump bAct3_3

label bsecondvillainlose:
    show bluemad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide bluemad with dissolve
    jump bpquiz2

#third monster
label bthirdvillain:
    show pic_13 with dissolve
    show redmad at center with hpunch
    "OY OY OY! Now look who is this."
    "the one who beated my brothers"
    "I am Mr.Red, the slime."
    "Don't laugh at me kid! well anyways,,,, you are in my territory kid. Now, before you get the last pages and past here you must play with me first."
    "kukukukukukukukukukukukukukukuku"
    "Now let's start"
    hide redmad with dissolve

    window hide

    show blacks with dissolve 

    ct "HARD!"

    ct " QUIZ "
    
    hide blacks 
    show board with dissolve

    n "Now it's time to spice things up."
    
    ct "From this point on, try to apply the knowledge you gained in the last few levels and figure out the rest."

    ct "LETS START! GOODLUCK!"
    jump bquiz1

label bthirdvillainwin:
    show redsad at center with moveinbottom
    "Ughhhh.. You have also beaten me in my own challenge... :()"
    hide redsad with dissolve

    window hide

    show screen addpages with dissolve
    $ pages = min(pages + 1, max_pages)
    pause

    hide screen addpages
    
    jump bAct3_4


label bthirdvillainlose:
    show redmad at center with moveinbottom
    "HAHAHAHAHAHAHAHAHA YOU GOT BEATEN TO A PULP, GUESS YOU HAVE TO REDO MY CHALLENGE! :P"
    hide redmad with dissolve
    jump bquiz1