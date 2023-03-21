screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        background "map.jpg"
        xsize 1920
        ysize 1080
        button:
            xpos 1000
            ypos 500
            text "Act 1"
            action Jump("Act1")