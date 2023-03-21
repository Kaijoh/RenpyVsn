define s = Character("Sylvie", color = "#ff009d" )

#backgrounds
image pic_1 = im.Scale("1.png", 1920, 1080)
image pic_2 = im.Scale("2.png", 1920, 1080)
image pic_3 = im.Scale("3.png", 1920, 1080)
image idle_1 = im.Scale("idle.jpg", 1920, 1080)

#characters
image protagonist = im.Scale("tia mouth_c eye_full brow_down ex_blush.png", 1920, 1080)



label start:

    show idle_1

    call variables

    jump Act1

    hide idle_1
        
    return

label variables:
    
    $ PlayerScore = 0
    $ PlayerName = renpy.input("What is your name?")
    if PlayerName:
        "Nice to meet you, [PlayerName]! goodluck on your adventure!"
    else:
        jump Act1

    return
