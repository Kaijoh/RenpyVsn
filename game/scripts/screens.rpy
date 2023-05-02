#routes x   
screen choose_route: 
    hbox: 
        xalign 0.5 
        yalign 0.5 
        yoffset 30 
        spacing 20 
        imagebutton: 
            idle "boychar2" 
            hover "boychar" 
            action Jump("variable") 
        imagebutton: 
            idle "girlchar" 
            hover "girlchar2" 
            action Jump("variable") 

screen arrows():
    hbox:
        xalign 0.86
        yalign 0.14
        add "arrow"

screen hearts():
    hbox:
        xalign 0.99
        yalign 0.02
        for i in range(max_lives):
            fixed xysize(99, 99): 
                add "background"
                add "border"
                if i < lives:
                    add "heart"
                    
screen books():
    hbox:
        xalign 0.13
        yalign 0.03
        for i in range(pages):
            fixed xysize(99, 99): 
                add "book"

screen fullbooks():
    hbox:
        xalign 0.01
        yalign 0.01
        add "fullbook"

screen addpages():
    hbox:
        xalign 0.5
        yalign 0.5
        add "addpage"