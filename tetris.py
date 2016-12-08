import random, os.path
import pygame
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

        length = 33
        height = 33

        DISPLAY.fill(blue)
        pygame.draw.rect(DISPLAY,black, (9, 9, 352, 702))

        x=10
        y=11

        for nr in range(20):
            self.row(DISPLAY, WHITE,x,y,length,height)
            y=y+35
    def row(self,DISPLAY, colour,x,y, length, height):
        print("in row")
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
