import pygame, sys
from pygame.locals import *
from Puzzle import SudokuPuzzle
from Game import SudokuGame

class SudokuGUI(object):
    
    def __init__(self, game):
        
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
        self.GAME = SudokuGame("puzzle2.txt")
        
        
    def drawGrid(self, display):
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(display, self.WHITE, [self.BOX_WIDTH * col + self.START_X, self.BOX_HEIGHT * row + self.START_Y, self.BOX_WIDTH, self.BOX_HEIGHT], 3)
     
    def drawNumbers(self, display, numbers, booleans):
        for row in range(9):
            for col in range(9):
                pygame.draw.rect(display, self.WHITE, [self.CELL_WIDTH * col + self.START_X, self.CELL_HEIGHT * row + self.START_Y, self.CELL_WIDTH, self.CELL_HEIGHT], 1)
                numFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
                if booleans[row, col, 0] == 0:                        
                    num = numFont.render("", False, self.WHITE)
                else:
                    num = numFont.render(str(numbers[row, col]), False, self.WHITE)
                self.SCREEN.blit(num, (self.CELL_WIDTH * col + self.START_X + self.NUM_X, self.CELL_HEIGHT * row + self.START_Y + self.NUM_Y))
           

def main():
    
    gui = SudokuGUI()
    pygame.init()
    display = pygame.display.set_mode([gui.WINDOW_WIDTH, gui.WINDOW_HEIGHT])
    pygame.display.set_caption("Python Sudoku")
    pygame.font.init()
    myfont = pygame.font.SysFont('Calibri Light', gui.TITLE_FONT_SIZE)
    gui.TITLE = myfont.render('Sudoku', False, gui.WHITE)
    gui.SCREEN.fill(gui.GREY)
    
    gui.drawGrid(display)
    gui.drawNumbers(display, gui.GAME.getPuzzle().getBooleans(), gui.GAME.getPuzzle().getNumbers())
    gui.updateWindow()
    display.blit(gui.TITLE,(gui.TITLE_X, gui.TITLE_Y))
    pygame.display.update()

if __name__=='__main__':
    main()
            
"""puzzle = SudokuPuzzle('puzzle2.txt')
gui = SudokuGUI(puzzle.getNumbers(), puzzle.getBooleans())
gui.runWindow()"""