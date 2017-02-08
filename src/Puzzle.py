from sys import stdout
import numpy as np

class SudokuPuzzle(object):
    
    def __init__(self, fileName):
        self.numbers = self.initNumbers(fileName)
        self.booleans = self.initBooleans()
        
    def initNumbers(self, fileName):
        nums = np.loadtxt(fileName, 'int16')
        return nums
    
    def initBooleans(self):
        bools = np.ones((9,9,10), np.int16)
        for row in range(9):
            for col in range(9):
                if self.numbers[row, col] == 0:
                    bools[row, col, 0] = 0
        return bools

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
        
puzzle = SudokuPuzzle('puzzle1.txt')
puzzle.printNumbers()
puzzle.printBooleans()


