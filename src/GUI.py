import pygame, sys
from pygame.locals import *
from Puzzle import SudokuPuzzle
from Game import SudokuGame
import time
import sys

class SudokuGUI(object):
    
    def __init__(self):
        
        """Variable definitions"""
        self.RUNNING = True
        self.WINDOW_WIDTH = 510
        self.WINDOW_HEIGHT = 625
        self.BOX_WIDTH = 150
        self.BOX_HEIGHT = 150
        self.CELL_WIDTH = 50
        self.CELL_HEIGHT = 50
        self.NUM_X = 18
        self.NUM_Y = 13
        self.TITLE_X = 185
        self.TITLE_Y = 30
        self.START_X = 30
        self.START_Y = 80
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GREY = (240,240,240)
        self.BLUE = (0,102,255)
        self.TITLE_FONT_SIZE = 55
        self.NUM_FONT_SIZE = 45
        
        
    def drawGrid(self, display):
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(display, self.WHITE, [self.BOX_WIDTH * col + self.START_X, self.BOX_HEIGHT * row + self.START_Y, self.BOX_WIDTH, self.BOX_HEIGHT], 3)
     
    def drawNumbers(self, display, booleans, numbers):
        for row in range(9):
            for col in range(9):
                pygame.draw.rect(display, self.BLACK, [self.CELL_WIDTH * col + self.START_X, self.CELL_HEIGHT * row + self.START_Y, self.CELL_WIDTH, self.CELL_HEIGHT], 1)
                numFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
                if booleans[row, col, 0] == 0:                        
                    num = numFont.render("", False, self.BLACK)
                else:
                    num = numFont.render(str(numbers[row, col]), False, self.BLACK)
                display.blit(num, (self.CELL_WIDTH * col + self.START_X + self.NUM_X, self.CELL_HEIGHT * row + self.START_Y + self.NUM_Y))
    
    def drawNextButton(self, display):
        pygame.draw.rect(display, self.BLUE, (self.START_X+(self.BOX_WIDTH * 3)-100,550,100,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("NEXT", False, self.BLACK)
        display.blit(next, (self.START_X+(self.BOX_WIDTH * 3)-92, 558)) 

    def runGUI(self):
        
        puzzle = SudokuPuzzle('puzzle2.txt')
        game = SudokuGame(puzzle)
        
        pygame.init()
        pygame.font.init()
        ft = pygame.font.SysFont('Calibri Light', self.TITLE_FONT_SIZE)
        title = ft.render('Sudoku', False, self.BLACK)
        display = pygame.display.set_mode([self.WINDOW_WIDTH, self.WINDOW_HEIGHT])
        pygame.display.set_caption("Python Sudoku")
        display.fill(self.GREY)
        display.blit(title,(self.TITLE_X, self.TITLE_Y))
        self.drawNextButton(display)
        self.drawGrid(display)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(1)

            self.drawNumbers(display, puzzle.getBooleans(), puzzle.getNumbers())
            pygame.display.flip()
            running = game.solveOneChoice()
            time.sleep(2)

gui = SudokuGUI()
gui.runGUI()
 