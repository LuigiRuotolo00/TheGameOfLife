from abc import ABC, abstractmethod
import pygame

class Slider(ABC):
    @abstractmethod
    def display():
        pass

class NewSlider(Slider):
    def __init__(self, liney, linex1, linex2, space, label = []):
        self.line_y = liney # Vertical position of the line
        self.line_x1 = linex1 # Start of the line
        self.line_x2 = linex2 # End of the line
        self.space = space # Distance between points
        self.points = list(range(self.line_x1, self.line_x2 + 1, self.space))
        self.level = 1
        self.levmap = {}
        self.label = label
        i = 1
        for k in self.points:
            self.levmap[k] = i
            i += 1
        self.r = 9
        self.circle_x = self.points[0]
        self.circle_y = self.line_y
        self.sliding = False
        
    def getSliding(self):
        return self.sliding
    
    def setCircle(self, evpos):
        x, y = evpos
        self.circle_x = max(self.line_x1, min(self.line_x2, x))
        
    def getLevel(self):
        return self.level
        
    def allignCircle(self):
        self.circle_x = min(self.points, key = lambda x: abs(x - self.circle_x))
        self.level = self.levmap[self.circle_x]
        
        
    def display(self, screen, color, font = None):
        pygame.draw.line(screen, color, (self.line_x1, self.line_y), (self.line_x2, self.line_y), 3)
        for p in self.points:
            pygame.draw.circle(screen, color, (p, self.line_y), 3)
        pygame.draw.circle(screen, color, (self.circle_x, self.circle_y), self.r, 0)
        for i, point in zip(self.label, self.points):
            text = font.render(str(i), True, color)
            screen.blit(text, (point - 10, self.line_y + 15))
        
    def setSliding(self, sld):
        self.sliding = sld
