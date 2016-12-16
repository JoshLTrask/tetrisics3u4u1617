import random, os.path
import pygame
from pygame.locals import *

"""This is a Tetris style game that the ICS3U/4U 2016/2017 class in Huntsville High School is creating.
Teacher: I. McTavish
Date: Dec 1, 2016"""

#Global Variables
SCREENRECT     = Rect((320,620),0,32)
main_dir = os.path.split(os.path.abspath(__file__))[0]
class Score:
    def __init__(self):
        self.score = 0
    def update_score(self):
        print("in update score")
    def draw(self):
        print("in draw method")
class Block:
    def __init__(self):
        print("initialize")
    def update(self):
        print("In block update")
    def draw(self):
        print("In block draw")
    def rotate(self):
        print("In block rotate")
    def check_collision(self):
        print("In check collision")
class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()

class Music:
    def __init__(self):
        self.Music = 0

    def play_music(self):
        print("in play music")

    def play_sound_right(self):
        print("in play soundright")

    def play_sound_left(self):
        print("in play sound left")

    def  play_sound_flip(self):
        print("in play sound flip")

    def play_sound_falling(self):
        print("in play sound falling")

class Game_Grid:
    def __init__(self):
        self.Game_Grid = 0

    def update(self):
        print("in update")

    def draw(self,DISPLAY):
        print("gamegriddraw")
        WHITE=(255,255,255)
        red = (255,0,0)
        blue=(155,255,255)
        black=(0,0,0)

        length = 28
        height = 28

        DISPLAY.fill(blue)
        pygame.draw.rect(DISPLAY,black, (9, 9, 302, 602))

        x=10
        y=11

        for nr in range(20):
            self.row(DISPLAY, WHITE,x,y,length,height)
            y=y+30
    def row(self,DISPLAY, colour,x,y, length, height):
        for i in range(10):
            if i % 2 == 0:
                pygame.draw.rect(DISPLAY,colour, (x+1, y, length, height))
                x = x + 30
            else:
                pygame.draw.rect(DISPLAY,colour, (x+1, y, length, height))
                x = x + 30

def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None
    game_grid = Game_Grid()
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.flip()
    clock = pygame.time.Clock()

    #load sounds ( Music must be in folder labeled "data")
    music = load_sound('Music.wav')
    if pygame.mixer:
        music = os.path.join(main_dir, 'data', 'Music.wav')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
        keystate = pygame.key.get_pressed()
        pygame.display.update()
        game_grid.draw(screen)




#call the "main" function if running this script
if __name__ == '__main__': main()

import random, os.path
import pygame
import copy
from pygame.locals import *

"""This is a Tetris style game that the ICS3U/4U 2016/2017 class in Huntsville High School is creating.
Teacher: I. McTavish
Date: Dec 1, 2016"""

#Global Variables
SCREENRECT     = Rect(0, 0, 370, 720)
main_dir = os.path.split(os.path.abspath(__file__))[0]


class Score:
    def __init__(self):
        self.score = 0
    def update_score(self):
        print("in update score")
    def draw(self):
        print("in draw method")

class Block:

    #initialize Block
    def __init__(self,DISPLAY):
        print('init')
        self.toUpdate = True
        self.pos = [3,0]
        self.timer = 0
        self.DISPLAY = DISPLAY
        self.filledBlocks = [] #move to global variables
        self.down = False

        self.colours = ['red','blue','lime','purple','gold','skyblue','green']
        self.shape = self.__Get_Shape()
        print('Shape :', self.shape)
        self.rotate()
        print('Shape :', self.shape)
        self.rotate()
        print('Shape :', self.shape)
        self.rotate()
        print('Shape :', self.shape)
        self.rotate()
        print('Shape :', self.shape)
        self.__draw()



    #pick random shape
    def __Get_Shape(self):
        print('New Shape')
        possible_shapes = [[[0,1],[1,1],[2,1],[3,1]],[[1,1],[1,2],[2,1],[2,2]],[[1,2],[2,1],[2,2],[3,1]],[[1,1],[2,1],[2,2],[3,1]],[[1,1],[2,1],[3,1],[3,2]]]
        shape = possible_shapes[random.randint(0,4)]
        return shape
    #Rotate Shape
    def rotate(self):
        if self.down == False:
            print('Start Rotate')
            cheetSheet = {'[0, 0]' : '[0, 3]','[0, 1]' : '[1, 3]','[0, 2]' : '[2, 3]','[0, 3]' : '[3, 3]','[1, 0]' : '[0, 2]','[1, 1]' : '[1, 2]','[1, 2]' : '[2, 2]','[1, 3]' : '[3, 2]','[2, 0]' : '[0, 1]','[2, 1]' : '[1, 1]','[2, 2]' : '[2, 1]','[2, 3]' : '[3, 1]','[3, 0]' : '[0, 0]','[3, 1]' : '[1, 0]','[3, 2]' : '[2, 0]','[3, 3]' : '[3, 0]',}
            newShape = copy.deepcopy(self.shape)
            for i in range(4):
                newShape[i] = cheetSheet[str(self.shape[i])]
                #print(newShape)

            self.shape = newShape
        self.down = True


    #Draw Shape
    def __draw(self):
        print('Start Draw')
        #green is position
        #pygame.draw.rect(self.DISPLAY,(0,255,0),(self.pos[0]*35 +11,self.pos[1]*35 + 11,33,33))

        for i in range(4): #['[1, 1]', '[2, 1]', '[3, 1]', '[3, 2]']
            pygame.draw.rect(self.DISPLAY,(0,0,255),((self.pos[0]*35 +11)+(35*int(self.shape[i][1])),(self.pos[1]*35 + 11)+(35*int(self.shape[i][4])),33,33))

    def __check_collision(self):
        print('start collision')
        #bottom of screen
        lowest = max(int(self.shape[0][4])+self.pos[1],int(self.shape[1][4])+self.pos[1],int(self.shape[2][4])+self.pos[1],int(self.shape[3][4])+self.pos[1])
        print(max(int(self.shape[0][4]),int(self.shape[1][4]),int(self.shape[2][4]),int(self.shape[3][4])))
        print('lowest :',lowest,'pos :',self.pos)
        if lowest >= 19:
            self.collide()

    def collide(self):
        print('COLLISION!')

        self.toUpdate = False
        for i in range(4):
            self.filledBlocks.append(self.shape[i])


    def update(self):
        if self.toUpdate == True:
            if self.timer == 500:
                self.pos[1] += 1
                print(self.pos)
                self.timer = 0

            Key = pygame.key.get_pressed()
            if Key[pygame.K_UP]:
                self.rotate()
            elif Key[pygame.K_RIGHT]:
                self.goRight()
            elif Key[pygame.K_LEFT]:
                self.goLeft()
            else:
                self.down = False


            self.timer += 1
            self.__check_collision()
        self.__draw()
        print(self.shape)


    def goRight(self):
        if self.down == False:
            self.pos[0] += 1
        self.down = True
    def goLeft(self):
        if self.down == False:
            self.pos[0] -= 1
        self.down = True

    def done(self):
        return(self.toUpdate)



class dummysound:
    def play(self): pass



def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()


class Music:
    def __init__(self):
        self.Music = 0

    def play_music(self):
        print("in play music")

    def play_sound_right(self):
        print("in play soundright")

    def play_sound_left(self):
        print("in play sound left")

    def  play_sound_flip(self):
        print("in play sound flip")

    def play_sound_falling(self):
        print("in play sound falling")

class Game_Grid:
    def __init__(self):
        self.Game_Grid = 0

    def update(self):
        print("in update")

    def draw(self,DISPLAY):
        #print("gamegriddraw")
        WHITE=(255,255,255)
        red = (255,0,0)
        blue=(155,255,255)
        black=(0,0,0)

        length = 33
        height = 33

        DISPLAY.fill(blue)
        pygame.draw.rect(DISPLAY,black, (9, 9, 352, 702))



        x=10
        y=11

        for nr in range(20):
            self.row(DISPLAY, WHITE,x,y,length,height)
            y=y+35
        #pygame.draw.rect(DISPLAY,red, (11, 11, 33, 33))
    def row(self,DISPLAY, colour,x,y, length, height):
        #print("in row")
        for i in range(10):
            if i % 2 == 0:
                pygame.draw.rect(DISPLAY,colour, (x+1, y, length, height))
                x = x + 35
            else:
                pygame.draw.rect(DISPLAY,colour, (x+1, y, length, height))
                x = x + 35



def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None
    game_grid = Game_Grid()
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.flip()
    clock = pygame.time.Clock()
    B = Block(screen)


    #load sounds ( Music must be in folder labeled "data")
    music = load_sound('Music.wav')
    if pygame.mixer:
        music = os.path.join(main_dir, 'data', 'Music.wav')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return

        keystate = pygame.key.get_pressed()
        pygame.display.update()
        game_grid.draw(screen)
        B.update()




#call the "main" function if running this script

if __name__ == '__main__': main()

