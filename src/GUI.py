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
        self.WINDOW_HEIGHT = 700
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
        self.GREEN = (32,170,34)
        self.RED = (170,32,32)
        self.TITLE_FONT_SIZE = 55
        self.NUM_FONT_SIZE = 40
        self.SOLVED_FONT_SIZE = 40
        self.OPTIONS_FONT_SIZE = 12
        self.STARTED = False
        
        
    def drawGrid(self, display):
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(display, self.BLACK, [self.BOX_WIDTH * col + self.START_X, self.BOX_HEIGHT * row + self.START_Y, self.BOX_WIDTH, self.BOX_HEIGHT], 3)
        for row in range(9):
            for col in range(9):
                pygame.draw.rect(display, self.BLACK, [self.CELL_WIDTH * col + self.START_X, self.CELL_HEIGHT * row + self.START_Y, self.CELL_WIDTH, self.CELL_HEIGHT], 1)
     
    def drawNumbers(self, display, booleans, numbers):
        for row in range(9):
            for col in range(9):
                numFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
                optionFont = pygame.font.SysFont('Calibri Light', self.OPTIONS_FONT_SIZE)
                x_loc_num = self.CELL_WIDTH * col + self.START_X + self.NUM_X
                y_loc_num = self.CELL_HEIGHT * row + self.START_Y + self.NUM_Y
                x_loc_option = self.CELL_WIDTH * col + self.START_X + self.NUM_X - 10
                y_loc_option = self.CELL_HEIGHT * row + self.START_Y + self.NUM_Y - 8
                if booleans[row, col, 0] == 0:
                    index = 1
                    for x in range(3):
                        temp_x_loc = x_loc_option
                        for y in range(3):
                            if booleans[row, col, index] == 1:
                                option = optionFont.render(str(index), False, self.BLACK)
                                display.blit(option, (temp_x_loc, y_loc_option))
                            temp_x_loc = temp_x_loc + 15
                            index = index + 1
                        y_loc_option = y_loc_option + 15
                else:
                    num = numFont.render(str(numbers[row, col]), False, self.BLACK)
                    display.blit(num, (x_loc_num, y_loc_num))
    
    def drawNextButton(self, display, game):
        rect_x = self.START_X+175
        rect_y = 550
        text_x = self.START_X+187
        text_y = 558
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 100 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = game.solveOneChoice() 
        pygame.draw.rect(display, self.BLUE, (rect_x,rect_y,100,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("NEXT", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def drawStartButton(self, display):
        rect_x = self.START_X
        rect_y = 550
        text_x = self.START_X+5
        text_y = 558
        retVal = False
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 100 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = True                
        pygame.draw.rect(display, self.BLUE, (rect_x,rect_y,100,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("START", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def drawQuitButton(self, display):
        rect_x = self.START_X+(self.BOX_WIDTH * 3)-100
        rect_y = 550
        text_x = self.START_X+(self.BOX_WIDTH * 3)-85
        text_y = 558
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 100 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = False                
        pygame.draw.rect(display, self.BLUE, (rect_x,rect_y,100,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("QUIT", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal

    def runGUI(self):
        
        puzzle = SudokuPuzzle('puzzle2.txt')
        game = SudokuGame(puzzle)
        
        pygame.init()
        pygame.font.init()
        ftTitle = pygame.font.SysFont('Calibri Light', self.TITLE_FONT_SIZE)
        titleText = ftTitle.render('Sudoku', False, self.BLACK)
        ftSolved = pygame.font.SysFont('Calibri Light', self.SOLVED_FONT_SIZE)
        solvedText = ftSolved.render('Solved!', False, self.GREEN)
        ftUnsolvable = pygame.font.SysFont('Calibri Light', self.SOLVED_FONT_SIZE)
        unsolvableText = ftUnsolvable.render('Cannot be solved!', False, self.RED)
        display = pygame.display.set_mode([self.WINDOW_WIDTH, self.WINDOW_HEIGHT])
        pygame.display.set_caption("Python Sudoku")
        
        running = True
        solveWorked = True
        solved = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(1)
            display.fill(self.GREY)
            display.blit(titleText,(self.TITLE_X, self.TITLE_Y))
            if self.STARTED == False:
                self.STARTED = self.drawStartButton(display)
            if self.STARTED == True and solved == False and solveWorked == True:
                solveWorked = self.drawNextButton(display, game)
            running = self.drawQuitButton(display)
            self.drawGrid(display)
            self.drawNumbers(display, puzzle.getBooleans(), puzzle.getNumbers())
            if puzzle.isSolved() == True:
                display.blit(solvedText, (self.TITLE_X + 18, 610))
            if puzzle.isSolved() == False and solveWorked == False:
                display.blit(unsolvableText, (self.TITLE_X - 45, 610))
            pygame.display.update()

gui = SudokuGUI()
gui.runGUI()