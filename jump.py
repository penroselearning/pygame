
HEIGHT = 500
WIDTH = 1000

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

    female.jump += FALL
    female.y += female.jump

    if(female.y > FLOOR):
        female.y = FLOOR
        female.image = 'character_femaleperson_idle'
    else:
        female.image = 'character_femaleperson_jump'

    if keyboard.LEFT:
        #female. =
        female.y = FLOOR


def on_key_down():
    if keyboard.UP:
        female.jump = JUMP

