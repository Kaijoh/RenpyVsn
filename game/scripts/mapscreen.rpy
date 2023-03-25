screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        background im.Scale("map.jpg", 1920, 1080)
        xsize 1920
        ysize 1080
        button:
            xpos 1000
            ypos 500
            text "Act 1"
            action Jump("Act1")