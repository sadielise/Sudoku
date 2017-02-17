from Puzzle import SudokuPuzzle
from Puzzle import RowIter
from Puzzle import ColumnIter
from Puzzle import BoxIter
from Puzzle import PuzzleIter
import sys

            
"""find cell in booleans that only has one option left"""
def solveOneChoice(puzzle):
    changeMade = False
    for cell in PuzzleIter():
        if puzzle.booleans[cell[0], cell[1], 0] == 0:
            oneCount = 0
            oneIndex = 0
            for x in range(9):
                val = x + 1
                if puzzle.booleans[cell[0], cell[1], val] == 1:
                    oneIndex = val
                    oneCount = oneCount + 1
            if oneCount == 1:
                puzzle.placeValue(cell[0], cell[1], oneIndex)
                changeMade = True
    
    return changeMade

def solveElimination(puzzle):
    changeMade = False
    for row in range(9):
        for val in range(9):
            count, retRow, retCol = puzzle.countOptionsInRow(row, (val+1))
            if count == 1:
                puzzle.placeValue(retRow, retCol, (val+1))
                changeMade = True
            
    for col in range(9):
        for val in range(9):
            count, retRow, retCol = puzzle.countOptionsInColumn(col, (val+1))
            if count == 1:
                puzzle.placeValue(retRow, retCol, (val+1))
                changeMade = True
    
    for box in range(9):
        for val in range(9):
            count, retRow, retCol = puzzle.countOptionsInColumn(box, (val+1))
            if count == 1:
                puzzle.placeValue(retRow, retCol, (val+1))
                changeMade = True
    
    return changeMade

"""initialize puzzle"""
puzzle = SudokuPuzzle('puzzle27.txt')
puzzle.printNumbers()
puzzle.printOptions()

"""solve puzzle"""
while True:
    
    isSolved = False
    
    print("moving to one choice")
    oneChoiceWorked = True
    while oneChoiceWorked == True and isSolved == False:
        oneChoiceWorked = solveOneChoice(puzzle)
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
            
    puzzle.printOptions()
        
    
    print("moving to elimination")
    eliminationWorked = True
    while eliminationWorked == True and isSolved == False:
        eliminationWorked = solveElimination(puzzle)
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
        
    puzzle.printOptions()    
        
