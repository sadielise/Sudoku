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

def solveSubsets(puzzle, num):
    changeMade = False
    
    for row in range(9):
        
        strings = []
        for cell1 in RowIter(row):
            tempString = ""
            if puzzle.booleans[cell1[0], cell1[1], 0] == 0:
                tempString += str(cell1[0])
                tempString += str(cell1[1])
                index = 1
                for i in range(9):
                    if puzzle.booleans[cell1[0], cell1[1], index] == 1:
                        tempString += str(index)
                    index += 1
                if len(tempString) == num + 2:
                    strings.append(tempString)
            
        finalStrings = []
        tempStrings = []
        stringsLen = len(strings)
        if(stringsLen >= num):
            for j in range(stringsLen - 1):
                k = j + 1
                while k < stringsLen:
                    if strings[j][2:] == strings[k][2:]:
                        if strings[j] not in tempStrings:
                            tempStrings.append(strings[j])
                        if strings[k] not in tempStrings:
                            tempStrings.append(strings[k])
                    k += 1
                if len(tempStrings) == 4:
                    for temp in tempStrings:
                        if temp not in finalStrings:
                            finalStrings.append(temp)

        finalStringsLen = len(finalStrings)
        if(finalStringsLen >= num):    
            for cell2 in RowIter(row):
                matchFound = False
                for s1 in finalStrings:
                    if str(cell2[0]) == str(s1[0]) and str(cell2[1]) == str(s1[1]):
                        matchFound = True
                if matchFound == False:
                    for s2 in finalStrings:
                        index = 2
                        for n in range(num):
                            if puzzle.booleans[cell2[0], cell2[1], int(s2[index])] != 0:
                                puzzle.booleans[cell2[0], cell2[1], int(s2[index])] = 0
                                changeMade = True
                                print("row change made")
                            index += 1
                        
    
    for col in range(9):
        
        strings = []
        for cell1 in ColumnIter(col):
            tempString = ""
            if puzzle.booleans[cell1[0], cell1[1], 0] == 0:
                tempString += str(cell1[0])
                tempString += str(cell1[1])
                index = 1
                for i in range(9):
                    if puzzle.booleans[cell1[0], cell1[1], index] == 1:
                        tempString += str(index)
                    index += 1
                if len(tempString) == num + 2:
                    strings.append(tempString)
                    print("adding string " + tempString)
            
        finalStrings = []
        tempStrings = []
        stringsLen = len(strings)
        if(stringsLen >= num):
            for j in range(stringsLen - 1):
                k = j + 1
                while k < stringsLen:
                    if strings[j][2:] == strings[k][2:]:
                        if strings[j] not in tempStrings:
                            tempStrings.append(strings[j])
                        if strings[k] not in tempStrings:
                            tempStrings.append(strings[k])
                    k += 1
                if len(tempStrings) == 4:
                    for temp in tempStrings:
                        if temp not in finalStrings:
                            finalStrings.append(temp)

        finalStringsLen = len(finalStrings)
        if(finalStringsLen >= num):
            for cell2 in ColumnIter(col):
                matchFound = False
                for s1 in finalStrings:
                    if str(cell2[0]) == str(s1[0]) and str(cell2[1]) == str(s1[1]):
                        matchFound = True
                if matchFound == False:
                    for s2 in finalStrings:
                        index = 2
                        for n in range(num):
                            if puzzle.booleans[cell2[0], cell2[1], int(s2[index])] != 0:
                                puzzle.booleans[cell2[0], cell2[1], int(s2[index])] = 0
                                changeMade = True
                                print("col change made")
                            index += 1
 
        
    boxRow = 0
    boxCol = 0
    while boxRow < 9:
        while boxCol < 9:
            strings = []
            for cell1 in BoxIter(boxRow, boxCol):
                tempString = ""
                if puzzle.booleans[cell1[0], cell1[1], 0] == 0:
                    tempString += str(cell1[0])
                    tempString += str(cell1[1])
                    index = 1
                    for i in range(9):
                        if puzzle.booleans[cell1[0], cell1[1], index] == 1:
                            tempString += str(index)
                        index += 1
                    if len(tempString) == num + 2:
                        strings.append(tempString)
            
            finalStrings = []
            tempStrings = []
            stringsLen = len(strings)
            if(stringsLen >= num):
                for j in range(stringsLen - 1):
                    k = j + 1
                    while k < stringsLen:
                        if strings[j][2:] == strings[k][2:]:
                            if strings[j] not in tempStrings:
                                tempStrings.append(strings[j])
                            if strings[k] not in tempStrings:
                                tempStrings.append(strings[k])
                        k += 1
                    if len(tempStrings) == 4:
                        for temp in tempStrings:
                            if temp not in finalStrings:
                                finalStrings.append(temp)
        
            finalStringsLen = len(finalStrings)
            if(finalStringsLen >= num):
                for cell2 in BoxIter(boxRow, boxCol):
                    matchFound = False
                    for s1 in finalStrings:
                        if str(cell2[0]) == str(s1[0]) and str(cell2[1]) == str(s1[1]):
                            matchFound = True
                    if matchFound == False:
                        for s2 in finalStrings:
                            index = 2
                            for n in range(num):
                                if puzzle.booleans[cell2[0], cell2[1], int(s2[index])] != 0:
                                    puzzle.booleans[cell2[0], cell2[1], int(s2[index])] = 0
                                    changeMade = True
                                    print("box change made")
                                index += 1
        
            boxCol += 3
        boxRow += 3
        
    return changeMade

"""initialize puzzle"""
puzzle = SudokuPuzzle('puzzle38.txt')
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
    
    
    print("moving to subsets of size 2")
    subsetsWorked = True
    while subsetsWorked == True and isSolved == False:
        subsetsWorked = solveSubsets(puzzle, 2) 
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
    puzzle.printOptions()
    
    
    print("moving to subsets of size 3")
    subsetsWorked = True
    while subsetsWorked == True and isSolved == False:
        subsetsWorked = solveSubsets(puzzle, 3) 
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
    puzzle.printOptions()
            
            
    print("moving to subsets of size 4")
    subsetsWorked = True
    while subsetsWorked == True and isSolved == False:
        subsetsWorked = solveSubsets(puzzle, 4) 
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)            
    puzzle.printOptions()  
        
