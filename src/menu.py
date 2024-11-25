from abc import ABC, abstractmethod
from unittest import case, defaultTestLoader
import pygame

class Menu(ABC):
    @abstractmethod
    def display():
        pass
    
    @abstractmethod
    def action():
        pass
    
    
class MainMenu(Menu):
    def __init__(self, text, font, color, screen):
        self.session = True
        self.game = []
        self.obs = []
        self.text = []
        self.textrect = []
        self.wrect = 200
        x = screen[0] / 3
        y = screen[1] / 3
        k = 0

        for i in text:
            self.text += [font.render(i, True, color)]
            self.textrect += [self.text[k].get_rect(topleft = (x, y))]
            k += 1
            y += 40
        
    def getSession(self):
        return self.session
    
    def setSession(self, val):
        self.session = val
    
    def display(self, screen, color, voice = -1):
        if voice > -1:
            pygame.draw.rect(screen, color, (self.textrect[voice].left - 5, self.textrect[voice].top - 5, self.wrect, self.textrect[voice].height + 10))
            screen.blit(self.text[voice], self.textrect[voice])
        else:
            for i,j in zip(self.text, self.textrect):
                pygame.draw.rect(screen, color, (j.left - 5, j.top - 5, self.wrect, j.height + 10))
                screen.blit(i, j)
        
    def action(self, choice, screen):
        self.display(screen, (128,128,128), choice)
      

class GameMenu(Menu):
    def __init__(self, text, button, color, font):
        self.game = []
        self.obs = []
        self.wrect = 200
        self.startbut = button[0]
        self.stopbut = button[1]
        self.start = True

        self.text = font.render(text, True, color)
        self.textrect = self.text.get_rect(topleft = (855, 40))
        self.butrect = self.startbut.get_rect(topleft = (865, 200))
        
    def getStart(self):
        return self.start

    
    def display(self, screen):
        screen.blit(self.text, self.textrect)
        if self.start == False:
            screen.blit(self.startbut, self.butrect)
        else:
            screen.blit(self.stopbut, self.butrect)
        
    def action(self, choice, screen):
        if choice == 0:
            self.start = False
        elif choice == 1:
            self.start = True
                
