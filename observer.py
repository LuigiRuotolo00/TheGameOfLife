from abc import ABC, abstractmethod
import pygame

class Observer(ABC):
    @abstractmethod
    def checkInput():
        pass
    
    @abstractmethod
    def attach():
        pass
    
class MenuObserver(Observer):
    def __init__(self):
        self.menu = []
        pass
    
    def checkInput(self, evpos, screen):
        
        for m in self.menu:
            k = 0
            for t in m.textrect:
                if t.collidepoint(evpos):
                    m.action(k, screen)
                    return k
                else:
                    k += 1
    
    def attach(self, menu):
        self.menu.append(menu)

class GameMenuObserver(Observer):
    def __init__(self):
        self.menu = []
        pass
    
    def checkInput(self, evpos, screen):
        
        for m in self.menu:
            k = 0
            if m.butrect.collidepoint(evpos):
                if m.start == True:
                    m.action(0, screen)
                    
                else:
                    m.action(1, screen)
                    
    
    def attach(self, menu):
        self.menu.append(menu)

 
class SliderObserver(Observer):
    def __init__(self):
        self.slide = []
        
    def checkInput(self, evpos):
        mousex, mousey = evpos
        for s in self.slide:
            dist = ((mousex - s.circle_x) ** 2 + (mousey - s.circle_y) ** 2) ** 0.5
            if dist <= s.r:
                s.setSliding(True)
                    
    
    def attach(self, slide):
        self.slide.append(slide)