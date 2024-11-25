from abc import ABC, abstractmethod
import pygame
import numpy as np

class Game(ABC):
    @abstractmethod
    def initMatrix():
        pass

    @abstractmethod    
    def nextGen():
        pass
    
    @abstractmethod
    def display():
        pass

class NewGame(Game):
        
    def __init__(self, x = 32, shape = pygame.Rect(0,0,0,0)):
        self.session = False
        self.width = x
        self.height = x
        self.row = 0
        self.column = 0
        self.matrix = []
        self.mapfps = [0.6, 0.4, 0.2, 0.1, 0.08]
        self.mappx = [32, 16, 8]
        self.fps = self.mapfps[0]
        self.cell = shape
        
    def initMatrix(self):
        self.row = int(800 / self.width)
        self.column = int(480 / self.height)
        self.matrix = np.random.choice([0, 1], size = (self.row, self.column), p = [0.8, 0.2])
        return (self.width, self.height, self.row, self.column)
        
    def getMapFps(self, key):
        return self.mapfps[key]
    
    def getMapPx(self, key):
        return self.mappx[key]
    
    def setCelDim(self, x):
        self.width = x
        self.height = x
        
        
    def setSession(self, flag):
        self.session = flag
            
    def getSession(self):
        return self.session
    
    def setFps(self, fps):
        self.fps = fps
    
    def getFps(self):
        return self.fps
    
    def nextGen(self):
        newmatrix = np.copy(self.matrix)
        for y in range(self.column):
            for x in range(self.row):
                n_neighbors = self.matrix[(x - 1) % self.row, (y - 1) % self.column] + \
                          self.matrix[(x)     % self.row, (y - 1) % self.column] + \
                          self.matrix[(x + 1) % self.row, (y - 1) % self.column] + \
                          self.matrix[(x - 1) % self.row, (y)     % self.column] + \
                          self.matrix[(x + 1) % self.row, (y)     % self.column] + \
                          self.matrix[(x - 1) % self.row, (y + 1) % self.column] + \
                          self.matrix[(x)     % self.row, (y + 1) % self.column] + \
                          self.matrix[(x + 1) % self.row, (y + 1) % self.column]

                if self.matrix[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    newmatrix[x, y] = 0
                elif self.matrix[x, y] == 0 and n_neighbors == 3:
                    newmatrix[x, y] = 1

        self.matrix = newmatrix
        
    def drawGrid(self, screen):
        for y in range(0, 480, self.height):
            for x in range(0, 800, self.width):
                cell = pygame.Rect(x, y, self.width, self.height)
                pygame.draw.rect(screen, (168,168,168), cell, True)
                
    def drawCells(self, screen):
        for y in range(self.column):
            for x in range(self.row):
                cell = pygame.Rect(x * self.width, y * self.height, self.width, self.height)
                if self.matrix[x, y] == 1:
                    pygame.draw.rect(screen, (0,0,0), cell)
                    
    def display(self, screen):
        self.drawCells(screen)
        self.drawGrid(screen)
        