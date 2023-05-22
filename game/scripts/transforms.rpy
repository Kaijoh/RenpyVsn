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
        ease .25 xoffset 40 yoffset 40
        ease .25 xoffset -10 yoffset 10
        repeat

transform addpage_bounce:
    xoffset  40
    yoffset -40
    block:
        ease .25 xoffset 10 yoffset 10
        ease .25 xoffset -40 yoffset 40
        repeat

transform bround_bounce:
    xoffset  50
    yoffset -50
    block:
        ease .25 xoffset 50 yoffset 50
        ease .25 xoffset -50 yoffset 50
        repeat


#images for the transforms
# bonus

image cat:
    "cat.png"
    zoom 0.30
image dog:
    "dog.png"
    zoom 0.30
image cheetah:
    "cheetah.png"
    zoom 0.30
image duck:
    "duck.png"
    zoom 0.30

image g1:
    "g1.png"
    zoom 0.22
image g2:
    "g2.png"
    zoom 0.22
image g3:
    "g3.png"
    zoom 0.22
image g4:
    "g4.png"
    zoom 0.22

image dm:
    "duckme.png"
    zoom 0.40

image broundp:
    "bimage.png", bround_bounce
    zoom 0.20



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
    xzoom -0.99
    "arrow.png", arrow_bounce

image addh:
    "addheart.png", addpage_bounce