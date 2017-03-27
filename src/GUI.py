import pygame
from pygame.locals import *
from Puzzle import SudokuPuzzle

class SudokuGUI(object):
    
    def __init__(self, numbers, booleans):
        
        """Variable definitions"""
        self.RUNNING = True
        self.WINDOW_WIDTH = 510
        self.WINDOW_HEIGHT = 565
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
        self.WHITE = (0,0,0)
        self.GREY = (240,240,240)
        self.TITLE_FONT_SIZE = 55
        self.NUM_FONT_SIZE = 45
        self.NUMBERS = numbers
        self.BOOLEANS = booleans
        
    def buildWindow(self):
        
        """Game setup"""
        pygame.init()
        pygame.font.init()
        myfont = pygame.font.SysFont('Calibri Light', self.TITLE_FONT_SIZE)
        fontsurface = myfont.render('Sudoku', False, self.WHITE)
        screen = pygame.display.set_mode([self.WINDOW_WIDTH, self.WINDOW_HEIGHT])
        screen.fill(self.GREY)
        pygame.display.set_caption("Python Sudoku")

        while self.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
            for row in range(3):
                for col in range(3):
                    pygame.draw.rect(screen, self.WHITE, [self.BOX_WIDTH * col + self.START_X, self.BOX_HEIGHT * row + self.START_Y, self.BOX_WIDTH, self.BOX_HEIGHT], 3)
            for row in range(9):
                for col in range(9):
                    pygame.draw.rect(screen, self.WHITE, [self.CELL_WIDTH * col + self.START_X, self.CELL_HEIGHT * row + self.START_Y, self.CELL_WIDTH, self.CELL_HEIGHT], 1)
                    numFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
                    if self.BOOLEANS[row, col, 0] == 0:
                        num = numFont.render("", False, self.WHITE)
                    else:
                        num = numFont.render(str(self.NUMBERS[row, col]), False, self.WHITE)
                    screen.blit(num, (self.CELL_WIDTH * col + self.START_X + self.NUM_X, self.CELL_HEIGHT * row + self.START_Y + self.NUM_Y))
            screen.blit(fontsurface,(self.TITLE_X, self.TITLE_Y))
            pygame.display.flip()
            
puzzle = SudokuPuzzle('puzzle2.txt')
gui = SudokuGUI(puzzle.getNumbers(), puzzle.getBooleans())
gui.buildWindow()