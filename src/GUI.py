import pygame, sys
from pygame.locals import *
from Puzzle import SudokuPuzzle
from Game import SudokuGame

class SudokuGUI(object):
    
    def __init__(self):
        
        """Variable definitions"""
        self.RUNNING = True
        self.WINDOW_WIDTH = 730
        self.WINDOW_HEIGHT = 560
        self.BOX_WIDTH = 150
        self.BOX_HEIGHT = 150
        self.CELL_WIDTH = 50
        self.CELL_HEIGHT = 50
        self.INNER_CELL_WIDTH = 48
        self.INNER_CELL_HEIGHT = 48
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
        self.LIGHT_YELLOW = (255,255,102)
        self.LIGHT_ORANGE = (255,153,102)
        self.LIGHT_PINK = (255,153,255)
        self.LIGHT_BLUE = (153,204,255)
        self.LIGHT_GREEN = (153,255,102)
        self.LIGHT_PURPLE = (204,153,255)
        self.PURPLE = (153,51,153)
        self.TITLE_FONT_SIZE = 55
        self.NUM_FONT_SIZE = 40
        self.SOLVED_FONT_SIZE = 40
        self.OPTIONS_FONT_SIZE = 12
        self.STARTED = False
        self.OPTIONS_ON = True
        self.HINTS_ON = True
        
        
    def drawGrid(self, display):
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(display, self.BLACK, [self.BOX_WIDTH * col + self.START_X, self.BOX_HEIGHT * row + self.START_Y, self.BOX_WIDTH, self.BOX_HEIGHT], 3)
        for row in range(9):
            for col in range(9):
                pygame.draw.rect(display, self.BLACK, [self.CELL_WIDTH * col + self.START_X, self.CELL_HEIGHT * row + self.START_Y, self.CELL_WIDTH, self.CELL_HEIGHT], 1)
     
    def drawHints(self, display, game, booleans):
        
        if self.HINTS_ON == True:
            for row in range(9):
                for col in range(9):
                    if booleans[row, col, 0] == 0:
                        totalOptions = 0
                        index = 1
                        for i in range(9):
                            if booleans[row, col, index] == 1:
                                totalOptions += 1
                            index += 1
                        if totalOptions == 1:
                            pygame.draw.rect(display, self.LIGHT_BLUE, [self.CELL_WIDTH * col + self.START_X + 1, self.CELL_HEIGHT * row + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
            
            for subsets in range(9):
                subsetsRow2 = game.findRowSubsetsNotMatching(2, subsets)
                if len(subsetsRow2) != 0:
                    for cell in subsetsRow2:
                        pygame.draw.rect(display, self.LIGHT_ORANGE, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                subsetsCol2 = game.findColSubsetsNotMatching(2, subsets)
                if len(subsetsCol2) != 0:
                    for cell in subsetsCol2:
                        pygame.draw.rect(display, self.LIGHT_ORANGE, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                
                subsetsRow3 = game.findRowSubsetsNotMatching(3, subsets)
                if len(subsetsRow3) != 0:
                    for cell in subsetsRow3:
                        pygame.draw.rect(display, self.LIGHT_PINK, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                subsetsCol3 = game.findColSubsetsNotMatching(3, subsets)
                if len(subsetsCol3) != 0:
                    for cell in subsetsCol3:
                        pygame.draw.rect(display, self.LIGHT_PINK, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                
                subsetsRow4 = game.findRowSubsetsNotMatching(4, subsets)
                if len(subsetsRow4) != 0:
                    for cell in subsetsRow4:
                        pygame.draw.rect(display, self.LIGHT_PURPLE, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                subsetsCol4 = game.findColSubsetsNotMatching(4, subsets)
                if len(subsetsCol4) != 0:
                    for cell in subsetsCol4:
                        pygame.draw.rect(display, self.LIGHT_PURPLE, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                
                subsetsRow5 = game.findRowSubsetsNotMatching(5, subsets)
                if len(subsetsRow5) != 0:
                    for cell in subsetsRow5:
                        pygame.draw.rect(display, self.LIGHT_YELLOW, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                subsetsCol5 = game.findColSubsetsNotMatching(5, subsets)
                if len(subsetsCol5) != 0:
                    for cell in subsetsCol5:
                        pygame.draw.rect(display, self.LIGHT_YELLOW, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                
            boxRow = 0
            boxCol = 0
            for i in range(3):
                for j in range(3):
                    subsetsBox2 = game.findBoxSubsetsNotMatching(2, boxRow, boxCol)
                    if len(subsetsBox2) != 0:
                        for cell in subsetsBox2:
                            pygame.draw.rect(display, self.LIGHT_ORANGE, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                   
                    subsetsBox3 = game.findBoxSubsetsNotMatching(3, boxRow, boxCol)
                    if len(subsetsBox3) != 0:
                        for cell in subsetsBox3:
                            pygame.draw.rect(display, self.LIGHT_PINK, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                    
                    subsetsBox4 = game.findBoxSubsetsNotMatching(4, boxRow, boxCol)
                    if len(subsetsBox4) != 0:
                        for cell in subsetsBox4:
                            pygame.draw.rect(display, self.LIGHT_PURPLE, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                    
                    subsetsBox5 = game.findBoxSubsetsNotMatching(5, boxRow, boxCol)
                    if len(subsetsBox5) != 0:
                        for cell in subsetsBox5:
                            pygame.draw.rect(display, self.LIGHT_YELLOW, [self.CELL_WIDTH * int(cell[1]) + self.START_X + 1, self.CELL_HEIGHT * int(cell[0]) + self.START_Y + 1, self.INNER_CELL_WIDTH, self.INNER_CELL_HEIGHT])
                    
                    boxRow += 3
                boxCol += 3
                        
                        
    def drawNumbers(self, display, booleans, numbers):
        
        for row in range(9):
            for col in range(9):
                numFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
                optionFont = pygame.font.SysFont('Calibri Light', self.OPTIONS_FONT_SIZE)
                x_loc_num = self.CELL_WIDTH * col + self.START_X + self.NUM_X
                y_loc_num = self.CELL_HEIGHT * row + self.START_Y + self.NUM_Y
                x_loc_option = self.CELL_WIDTH * col + self.START_X + self.NUM_X - 10
                y_loc_option = self.CELL_HEIGHT * row + self.START_Y + self.NUM_Y - 8
                if booleans[row, col, 0] == 0 and self.OPTIONS_ON == True:
                    index = 1
                    for x in range(3):
                        temp_x_loc = x_loc_option
                        for y in range(3):
                            if booleans[row, col, index] == 1:
                                option = optionFont.render(str(index), False, self.BLACK)
                                display.blit(option, (temp_x_loc, y_loc_option))
                            temp_x_loc = temp_x_loc + 15
                            index += 1
                        y_loc_option = y_loc_option + 15
                else:
                    if numbers[row, col] != 0:
                        num = numFont.render(str(numbers[row, col]), False, self.BLACK)
                        display.blit(num, (x_loc_num, y_loc_num))
                        
    def drawStartButton(self, display):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 20
        text_y = self.START_Y + 8
        retVal = False
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 100 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = True                
        pygame.draw.rect(display, self.BLACK, (rect_x,rect_y,100,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("START", False, self.WHITE)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def drawQuitButton(self, display):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 125
        rect_y = self.START_Y
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 140
        text_y = self.START_Y + 8
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 100 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = False                
        pygame.draw.rect(display, self.BLACK, (rect_x,rect_y,100,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("QUIT", False, self.WHITE)
        display.blit(next, (text_x,text_y)) 
        return retVal
                    
    def drawOptionsButton(self, display):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y + 50
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 23
        text_y = self.START_Y + 57
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 210 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                self.OPTIONS_ON = not self.OPTIONS_ON
        pygame.draw.rect(display, self.BLACK, (rect_x,rect_y,210,40))
        optionsFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        if self.OPTIONS_ON == True:
            options = optionsFont.render("OPTIONS OFF", False, self.WHITE)
            display.blit(options, (text_x,text_y))
        else:
            options = optionsFont.render("OPTIONS ON", False, self.WHITE)
            display.blit(options, (text_x,text_y))
            
    def drawHintsButton(self, display):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y + 100
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 45
        text_y = self.START_Y + 107
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 210 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                self.HINTS_ON = not self.HINTS_ON
        pygame.draw.rect(display, self.BLACK, (rect_x,rect_y,210,40))
        optionsFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        if self.HINTS_ON == True:
            options = optionsFont.render("HINTS OFF", False, self.WHITE)
            display.blit(options, (text_x,text_y))
        else:
            options = optionsFont.render("HINTS ON", False, self.WHITE)
            display.blit(options, (text_x,text_y))
    
    def drawOneChoiceButton(self, display, game):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y + (3 * self.BOX_WIDTH) - 290
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 28
        text_y = self.START_Y + (3 * self.BOX_WIDTH) - 283
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 210 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = game.solveOneChoice() 
        pygame.draw.rect(display, self.LIGHT_BLUE, (rect_x,rect_y,210,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("ONE CHOICE", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def drawEliminationButton(self, display, game):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y + (3 * self.BOX_WIDTH) - 240
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 28
        text_y = self.START_Y + (3 * self.BOX_WIDTH) - 233
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 210 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = game.solveElimination() 
        pygame.draw.rect(display, self.LIGHT_GREEN, (rect_x,rect_y,210,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("ELIMINATION", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def drawSubsets2Button(self, display, game):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y + (3 * self.BOX_WIDTH) - 190
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 28
        text_y = self.START_Y + (3 * self.BOX_WIDTH) - 183
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 210 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = game.solveSubsets(2) 
        pygame.draw.rect(display, self.LIGHT_ORANGE, (rect_x,rect_y,210,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("SUBSETS 2", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def drawSubsets3Button(self, display, game):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y + (3 * self.BOX_WIDTH) - 140
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 28
        text_y = self.START_Y + (3 * self.BOX_WIDTH) - 133
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 210 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = game.solveSubsets(3) 
        pygame.draw.rect(display, self.LIGHT_PINK, (rect_x,rect_y,210,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("SUBSETS 3", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def drawSubsets4Button(self, display, game):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y + (3 * self.BOX_WIDTH) - 90
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 28
        text_y = self.START_Y + (3 * self.BOX_WIDTH) - 83
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 210 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = game.solveSubsets(4) 
        pygame.draw.rect(display, self.LIGHT_PURPLE, (rect_x,rect_y,210,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("SUBSETS 4", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def drawSubsets5Button(self, display, game):
        rect_x = self.START_X + (3 * self.BOX_WIDTH) + 15
        rect_y = self.START_Y + (3 * self.BOX_WIDTH) - 40
        text_x = self.START_X + (3 * self.BOX_WIDTH) + 28
        text_y = self.START_Y + (3 * self.BOX_WIDTH) - 33
        retVal = True
        mouse_pos = pygame.mouse.get_pos()
        click_pos = pygame.mouse.get_pressed()
        if rect_x < mouse_pos[0] < rect_x + 210 and rect_y < mouse_pos[1] < rect_y + 40:
            if click_pos[0] == 1:
                retVal = game.solveSubsets(5) 
        pygame.draw.rect(display, self.LIGHT_YELLOW, (rect_x,rect_y,210,40))
        nextFont = pygame.font.SysFont('Calibri Light', self.NUM_FONT_SIZE)
        next = nextFont.render("SUBSETS 5", False, self.BLACK)
        display.blit(next, (text_x,text_y)) 
        return retVal
    
    def runGUI(self):
        
        puzzle = SudokuPuzzle('puzzle38.txt')
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
            self.drawHints(display, game, puzzle.getBooleans())
            self.drawNumbers(display, puzzle.getBooleans(), puzzle.getNumbers())
            self.drawGrid(display)
            self.drawOptionsButton(display)
            self.drawHintsButton(display)
            if self.STARTED == False:
                self.STARTED = self.drawStartButton(display)
            if self.STARTED == True and solved == False and solveWorked == True:
                onechoice = self.drawOneChoiceButton(display, game)
                elimination = self.drawEliminationButton(display, game)
                subsets2 = self.drawSubsets2Button(display, game)
                subsets3 = self.drawSubsets3Button(display, game)
                subsets4 = self.drawSubsets4Button(display, game)
                subsets5 = self.drawSubsets5Button(display, game)
                solveWorked = onechoice or elimination or subsets2 or subsets3 or subsets4 or subsets5
            running = self.drawQuitButton(display)
            if puzzle.isSolved() == True:
                display.blit(solvedText, (self.START_X + (3 * self.BOX_WIDTH) + 60,self.TITLE_Y))
            if puzzle.isSolved() == False and solveWorked == False:
                display.blit(unsolvableText, (self.START_X + (3 * self.BOX_WIDTH) + 15, self.TITLE_Y))
            pygame.display.update()

gui = SudokuGUI()
gui.runGUI()