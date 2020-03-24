
HEIGHT = 500

WIDTH = 1000

postures=['character_femaleperson_walk1',
'character_femaleperson_walk2',
'character_femaleperson_walk3',
'character_femaleperson_walk4',
'character_femaleperson_walk5',
'character_femaleperson_walk6',
'character_femaleperson_walk7']

x = 0
 

FLOOR = 400

female = Actor('character_femaleperson_idle',(400,FLOOR),anchor=('left','bottom'))
female.jump = 0

FALL = .6
JUMP = -7
 
def draw():
    screen.clear()
    screen.blit("backgroundcolorgrass",(0,-350))
    female.draw()

def update():

    #jumpee
    female.jump += FALL
    female.y += female.jump

    if(female.y > FLOOR):
        female.y = FLOOR
        female.image = 'character_femaleperson_idle'
    else:
        female.image = 'character_femaleperson_jump'


    #walkee

    global x

    frames_per_image = 5

    if keyboard.right:
        female.image = postures[x // frames_per_image]
        x += 1
        if x // frames_per_image >= len(postures):
            x = 0

        female.left += 4

        if female.left > WIDTH:
            female.left = -10


def on_key_down():
    if keyboard.UP:
        female.jump = JUMP
