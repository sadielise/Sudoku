from sys import stdout
import numpy as np
from astropy.wcs.docstrings import row

class SudokuPuzzle(object):
    
    """setup number and boolean arrays"""
    def __init__(self, fileName):
        self.numbers = self.initNumbers(fileName)
        self.booleans = self.initBooleans()
        self.setBooleans()
    
    """load values from file into numbers array"""    
    def initNumbers(self, fileName): 
        nums = np.loadtxt(fileName, 'int16')
        return nums
    
    """set all values in boolean array to 1"""
    def initBooleans(self): 
        bools = np.ones((9,9,10), np.int16)
        return bools
    
    """set first index to zero for unknown values, otherwise place val"""
    def setBooleans(self): 
        for cell in PuzzleIter():
            if self.numbers[cell[0], cell[1]] == 0:
                self.booleans[cell[0], cell[1], 0] = 0
        
        for cell in PuzzleIter():
            if self.numbers[cell[0], cell[1]] != 0:
                self.placeValue(cell[0], cell[1], self.numbers[cell[0], cell[1]])
    
    """change all indices > 0 to 0 except for value"""
    def setOptions(self, row, col, val): 
        self.booleans[row, col, 0] = 1
        for x in range(9):
            if (x + 1) != val:
                self.booleans[row, col, (x + 1)] = 0
    
    """set index of val to 0 for all cells in row"""
    def wipeOutRow(self, row, val): 
        for cell in RowIter(row):
            if(self.booleans[cell[0], cell[1], 0] == 0):
                self.booleans[cell[0], cell[1], val] = 0
    
    """set index of val to 0 for all cells in column"""
    def wipeOutColumn(self, col, val): 
        for cell in ColumnIter(col):
            if(self.booleans[cell[0], cell[1], 0] == 0):
                self.booleans[cell[0], cell[1], val] = 0
    
    """set index of val to 0 for all cells in box"""
    def wipeOutBox(self, row, col, val): 
        for cell in BoxIter(row, col):
                if(self.booleans[cell[0], cell[1], 0] == 0):
                    self.booleans[cell[0], cell[1], val] = 0
    
    """count how many times an option shows up in a row"""
    def countOptionsInRow(self, row, val): 
        count = 0
        col = 0
        for cell in RowIter(row):
            if(self.booleans[cell[0], cell[1], 0] == 0):
                if(self.booleans[cell[0], cell[1], val] == 1):
                    count = count + 1
                    col = cell[1]
        return count, row, col
    
    """count how many times an option shows up in a column"""
    def countOptionsInColumn(self, col, val): 
        count = 0
        row = 0
        for cell in ColumnIter(col):
            if(self.booleans[cell[0], cell[1], 0] == 0):
                if(self.booleans[cell[0],cell[1], val] == 1):
                    count = count + 1
                    row = cell[0]
        return count, row, col
        
    """count how many times an options shows up in a box"""
    def countOptionsInBox(self, row, col, val): 
        count = 0
        retRow = 0
        retCol = 0
        for cell in BoxIter(row, col):
            if(self.booleans[cell[0], cell[1], 0] == 0):
                if(self.booleans[cell[0],cell[1], val] == 1):
                    count = count + 1
                    retRow = cell[0]
                    retCol = cell[1]
        return count, retRow, retCol
    
    """place val in number array and wipe out row, column, and box in boolean array"""
    def placeValue(self, row, col, val):
        self.numbers[row, col] = val
        self.setOptions(row, col, self.numbers[row, col])
        self.wipeOutRow(row, self.numbers[row, col])
        self.wipeOutColumn(col, self.numbers[row, col])
        self.wipeOutBox(row, col, self.numbers[row, col])
        
    def isSolved(self):
        for cell in PuzzleIter():
            if self.booleans[cell[0], cell[1], 0] == 0:
                return False
        return True 
        
    """print numbers array"""        
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
        
    """print first index of boolean array"""
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
       
    """print entire boolean array"""
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


class BoxIter:
    def __init__(self, row, col):
        self.row, self.col = getBoxCoordinates(row, col)
        self.startRow = self.row
        self.startCol = self.col
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not(self.row == (self.startRow + 2) and self.col == (self.startCol + 3)):
            if self.col == (self.startCol + 3):
                self.col = self.startCol
                self.row = self.row + 1
            self.col = self.col + 1
            return (self.row), (self.col - 1)
        else:
            raise StopIteration
        
class RowIter:
    def __init__(self, row):
        self.row = row
        self.col = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.col < 9:
            self.col = self.col + 1
            return self.row, (self.col - 1)
        else:
            raise StopIteration
        
class ColumnIter:
    def __init__(self, col):
        self.row = 0
        self.col = col
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.row < 9:
            self.row = self.row + 1
            return (self.row - 1), self.col
        else:
            raise StopIteration
        
class PuzzleIter:
    def __init__(self):
        self.row = 0
        self.col = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not(self.row == 8 and self.col == 9):
            self.col = self.col + 1
            if self.col == 10:
                self.col = 1
                self.row = self.row + 1
            return self.row, (self.col - 1)
        else:
            raise StopIteration
        
"""return box number for given coordinates"""            
def getBoxCoordinates(row, col):
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
