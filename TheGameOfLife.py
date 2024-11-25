from ctypes import alignment
import pygame

from src import menu
from src import game
from src import observer
from src import slider


pygame.init()

if not pygame.get_init():
    print("pygame init error")
    exit()

width = 1000
height = 480

# initialize loop variable
session = True

# Initializing surface
surface = pygame.display.set_mode((width,height))

# Take image as input 
img = pygame.image.load('img/Glider.png')
pauseimg = pygame.image.load('img/pause.png')
startimg = pygame.image.load('img/start.png')

pauseimg = pygame.transform.scale(pauseimg, (40, 40))
startimg = pygame.transform.scale(startimg, (40, 40))
  
# Set image as icon 
pygame.display.set_icon(img) 

# set title 
pygame.display.set_caption("John Conway's Game of Life")



# Initializing RGB Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
 
# Changing surface color
surface.fill(white)


# Create a font file by passing font file
# and size of the font
font = pygame.font.SysFont('font/Metropolis.ttf', 30)
titlefont = pygame.font.SysFont('font/Metropolis.ttf', 70)

title = titlefont.render('The Game Of Life', True, black)
titlerect = title.get_rect(center = (width / 2, 80))


fontlab = pygame.font.SysFont(None, 24)
# define texts for menu
text = ('New Game', 'Exit')

gametext = 'SPEED'

label = ['32', '16', '8']

# The pygame.display.flip() method is used 
# to update content on the display screen
pygame.display.flip()

# creating a clock object
clock = pygame.time.Clock()

# init menu object
mainmenu = menu.MainMenu(text, font, white, (width, height))
mobs = observer.MenuObserver()
mobs.attach(mainmenu)

gamemenu = menu.GameMenu(gametext,  (startimg, pauseimg), black, font)
gmobs = observer.GameMenuObserver()
gmobs.attach(gamemenu)

# variable for menu choice
action = 0

# init game object
game = game.NewGame()

slide = slider.NewSlider(100, 830, 950, 30)
slobs = observer.SliderObserver()
slobs.attach(slide)

slidemenu = slider.NewSlider(170, 630, 690, 30, label)
mslobs = observer.SliderObserver()
mslobs.attach(slidemenu)

# run window
while mainmenu.getSession():
    
    #set frame rate
    clock.tick(24)
    
    surface.fill(white)
    surface.blit(title, titlerect)
    mainmenu.display(surface, black)
    slidemenu.display(surface, black, fontlab)

    #events management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainmenu.setSession(False)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mslobs.checkInput(event.pos)
            action = mobs.checkInput(event.pos, surface)
            print(action)
            match action:
                case 0:
                    game.setCelDim(game.getMapPx(slidemenu.getLevel() - 1))
                    cell_width, cell_height, nrow, ncolumn = game.initMatrix()
                    game.setSession(True)
                case 1:
                    mainmenu.setSession(False)
        if event.type == pygame.MOUSEMOTION and slidemenu.getSliding():
            slidemenu.setCircle(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            if slidemenu.getSliding():
                slidemenu.allignCircle()
            slidemenu.setSliding(False)


    timeframe = 0    

    while game.getSession():
        game.setFps(game.getMapFps(slide.getLevel() - 1))
        
        #set frame rate and calculate time between frames
        delta = clock.tick(24) / 1000
        timeframe += delta
        
        surface.fill(white)
        
        game.display(surface)
        if gamemenu.getStart():
            if timeframe >= game.getMapFps(slide.getLevel() - 1):
                timeframe = 0
                game.nextGen()
        gamemenu.display(surface)
        slide.display(surface, black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.setSession(False)
                mainmenu.setSession(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                gmobs.checkInput(event.pos, surface)
                slobs.checkInput(event.pos)
            if event.type == pygame.MOUSEMOTION and slide.getSliding():
                slide.setCircle(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if slide.getSliding():
                    slide.allignCircle()
                slide.setSliding(False)
                
                
                
        pygame.display.update()
                
            
    
    pygame.display.update()


# quit pygame after closing window 
pygame.quit() 