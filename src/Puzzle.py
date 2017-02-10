from sys import stdout
import numpy as np

class SudokuPuzzle(object):
    
    def __init__(self, fileName):
        self.numbers = self.initNumbers(fileName)
        self.booleans = self.initBooleans()
        self.setBooleans()
        
    def initNumbers(self, fileName):
        nums = np.loadtxt(fileName, 'int16')
        return nums
    
    def initBooleans(self):
        bools = np.ones((9,9,10), np.int16)
        return bools
    
    def setBooleans(self):
        for row in range(9):
            for col in range(9):
                if self.numbers[row, col] == 0:
                    self.booleans[row, col, 0] = 0
        
        for row in range(9):
            for col in range(9):
                if self.numbers[row, col] != 0:
                    self.setOptions(row, col, self.numbers[row, col])
                    self.wipeOutRow(row, self.numbers[row, col])
                    self.wipeOutColumn(col, self.numbers[row, col])
                    self.wipeOutBox(row, col, self.numbers[row, col])
    
    def setOptions(self, row, col, val):
        for x in range(9):
            if (x + 1) != val:
                self.booleans[row, col, (x + 1)] = 0
    
    def wipeOutRow(self, row, val):
        for col in range(9):
            if(self.booleans[row, col, 0] == 0):
                self.booleans[row, col, val] = 0
    
    def wipeOutColumn(self, col, val):
        for row in range(9):
            if(self.booleans[row, col, 0] == 0):
                self.booleans[row, col, val] = 0
    
    def wipeOutBox(self, row, col, val):
        startRow, startCol = self.getBoxCoordinates(row, col)
        rowCount = startRow
        colCount = startCol
        for x in range(3):
            for y in range(3):
                if(self.booleans[rowCount, colCount, 0] == 0):
                    self.booleans[rowCount, colCount, val] = 0
                colCount = colCount + 1
            colCount = startCol
            rowCount = rowCount + 1
                
    def getBoxCoordinates(self, row, col):
        if row < 3 and col < 3:
            return 0, 0
        elif row < 3 and col > 2 and col < 6:
            return 0, 3
        elif row < 3 and col > 5:
            return 0, 6
        elif row > 2 and row < 6 and col < 3:
            return 3, 0
        elif row > 2 and row < 6 and col > 2 and col < 6:
            return 3, 3
        elif row > 2 and row < 6 and col < 9:
            return 3, 6
        elif row > 5 and col < 3:
            return 6, 0
        elif row > 5 and col > 2 and col < 6:
            return 6, 3
        elif row > 5 and col > 5:
            return 6, 6
            
    def printNumbers(self):
        colCount = 0
        boxCount = 0
        rowCount = 0
        print("---------------------")
        for val in np.nditer(self.numbers):
            stdout.write(str(val))
            if colCount == 2 or colCount == 5:
                stdout.write("\t")
                colCount = colCount + 1
            elif colCount == 8:
                rowCount = rowCount + 1
                stdout.write("\n")
                colCount = 0
                if boxCount == 2 and rowCount < 8:
                    stdout.write("\n")
                    boxCount = 0
                else:
                    boxCount = boxCount + 1
            else:
                stdout.write(" ")
                colCount = colCount + 1
        print("---------------------\n")
        
    def printBooleans(self):
        colCount = 0
        boxCount = 0
        rowCount = 0
        print("---------------------")
        for row in range(9):
            for col in range(9):
                stdout.write(str(self.booleans[row, col, 0]))
                if colCount == 2 or colCount == 5:
                    stdout.write("\t")
                    colCount = colCount + 1
                elif colCount == 8:
                    rowCount = rowCount + 1
                    stdout.write("\n")
                    colCount = 0
                    if boxCount == 2 and rowCount < 8:
                        stdout.write("\n")
                        boxCount = 0
                    else:
                        boxCount = boxCount + 1
                else:
                    stdout.write(" ")
                    colCount = colCount + 1
        print("---------------------\n")
        
    def printOptions(self):
        rowCount = 0
        colCount = 0
        boxCount = 1
        
        print("---------------------------------------------------------------------")
        for w in range(9):
            for x in range(9):
                for y in range(3):
                    if(self.booleans[rowCount, colCount, boxCount] == 0):
                        stdout.write("- ")
                    else:
                        stdout.write(str(boxCount) + " ")
                    boxCount = boxCount + 1
                stdout.write("\t")
                colCount = colCount + 1
                boxCount = 1
                if x == 2 or x == 5:
                    stdout.write(" ")
            stdout.write("\n")
            boxCount = 4
            colCount = 0
            
            for x in range(9):
                for y in range(3):
                    if(self.booleans[rowCount, colCount, boxCount] == 0):
                        stdout.write("- ")
                    else:
                        stdout.write(str(boxCount) + " ")
                    boxCount = boxCount + 1
                stdout.write("\t") 
                colCount = colCount + 1
                boxCount = 4
                if x == 2 or x == 5:
                    stdout.write(" ")
            stdout.write("\n")
            boxCount = 7
            colCount = 0
            
            for x in range(9):
                for y in range(3):
                    if(self.booleans[rowCount, colCount, boxCount] == 0):
                        stdout.write("- ")
                    else:
                        stdout.write(str(boxCount) + " ")
                    boxCount = boxCount + 1
                stdout.write("\t")
                colCount = colCount + 1
                boxCount = 7
                if x == 2 or x == 5:
                    stdout.write(" ")
            if rowCount < 8:
                stdout.write("\n\n")
                if rowCount == 2 or rowCount == 5:
                    stdout.write("\n")
            else:
                stdout.write("\n")
            boxCount = 1
            colCount = 0
            rowCount = rowCount + 1
        
        print("---------------------------------------------------------------------\n")
        
        
puzzle = SudokuPuzzle('puzzle1.txt')
puzzle.printNumbers()
puzzle.printOptions()


