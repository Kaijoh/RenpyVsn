#highlights 
transform darken: 
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0) 
    linear 0.5 matrixcolor TintMatrix("#4e4e4e") * SaturationMatrix(1.0) 
 
transform lighten: 
    linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0) 


transform arrow_bounce:
    xoffset  40
    yoffset -40
    block:
        ease .25 xoffset 10 yoffset 10
        ease .25 xoffset -40 yoffset 40
        repeat

transform addpage_bounce:
    xoffset  40
    yoffset -40
    block:
        ease .25 xoffset 10 yoffset 10
        ease .25 xoffset -40 yoffset 40
        repeat


#images for the transforms

image menubg:
    "transparent.png"
    

image stat:
    "stats_idle.png"
    zoom 0.30

image stat2:
    "stats2_idle.png"
    zoom 0.30

image exchange:
    "rewardsx.png"
    zoom 0.50

image exchange2:
    "rewardsx2.png"
    zoom 0.50

image close:
    "close_idle.png"
    zoom 0.30

image heart:
    "heart.png"
    zoom 2.90
    
image background:
    "background.png"
    zoom 2.80
    
image border:
    "border.png"
    zoom 2.80
    

image book:
    "book.png"
    zoom 0.14
image fullbook:
    "fullbook.png"
    zoom 0.1
image addpage:
    "addpage.png", addpage_bounce
    zoom 0.1

image arrow:
    "arrow.png", arrow_bounce

image addh:
    "addheart.png", addpage_bounce