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
        """get row/column/options for all cells in row with number of options = num"""
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
                    
        """find all strings w/ matching options and put into temp array"""
        finalStrings = []
        stringsLen = len(strings)
        if(stringsLen >= num):
            for j in range(stringsLen - 1):
                k = j + 1
                tempStrings = []
                while k < stringsLen:
                    if strings[j][2:] == strings[k][2:]:
                        if strings[j] not in tempStrings:
                            tempStrings.append(strings[j])
                        if strings[k] not in tempStrings:
                            tempStrings.append(strings[k])
                    k += 1
            
                if len(tempStrings) == num:
                    for tempStr in tempStrings:
                        if tempStr not in finalStrings:
                            finalStrings.append(tempStr)

        """for cells not chosen, remove chosen cell options from their options"""
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
                            index += 1
    
    for col in range(9):

        """get row/column/options for all cells in column with number of options = num"""
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

                    
        """find all strings w/ matching options and put into temp array"""
        finalStrings = []
        stringsLen = len(strings)
        if(stringsLen >= num):
            for j in range(stringsLen - 1):
                k = j + 1
                tempStrings = []
                while k < stringsLen:
                    if strings[j][2:] == strings[k][2:]:
                        if strings[j] not in tempStrings:
                            tempStrings.append(strings[j])
                        if strings[k] not in tempStrings:
                            tempStrings.append(strings[k])
                    k += 1
            
                if len(tempStrings) == num:
                    for tempStr in tempStrings:
                        if tempStr not in finalStrings:
                            finalStrings.append(tempStr)

        """for cells not chosen, remove chosen cell options from their options"""
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
                            index += 1
 
    """get row/column/options for all cells in box with number of options = num"""    
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
            
            """find all strings w/ matching options and put into temp array"""
            finalStrings = []
            stringsLen = len(strings)
            if(stringsLen >= num):
                for j in range(stringsLen - 1):
                    k = j + 1
                    tempStrings = []
                    while k < stringsLen:
                        if strings[j][2:] == strings[k][2:]:
                            if strings[j] not in tempStrings:
                                tempStrings.append(strings[j])
                            if strings[k] not in tempStrings:
                                tempStrings.append(strings[k])
                        k += 1
                
                    if len(tempStrings) == num:
                        for tempStr in tempStrings:
                            if tempStr not in finalStrings:
                                finalStrings.append(tempStr)
        
            """for cells not chosen, remove chosen cell options from their options"""
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
                                index += 1
        
            boxCol += 3
        boxRow += 3
        
    return changeMade

"""initialize puzzle"""
puzzle = SudokuPuzzle('puzzle49.txt')
puzzle.printNumbers()
puzzle.printOptions()

"""solve puzzle"""
while True:
    
    isSolved = False
    verbose = False
    numChanges = 0
    
    print("moving to one choice")
    oneChoiceWorked = True
    while oneChoiceWorked == True and isSolved == False:
        oneChoiceWorked = solveOneChoice(puzzle)
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
        if oneChoiceWorked == True:
            numChanges +=1
    if verbose == True:
        puzzle.printOptions()
        
    
    print("moving to elimination")
    eliminationWorked = True
    while eliminationWorked == True and isSolved == False:
        eliminationWorked = solveElimination(puzzle)
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
        if eliminationWorked == True:
            numChanges += 1
    if verbose == True:
        puzzle.printOptions()
    
    
    print("moving to subsets of size 2")
    subsets2Worked = True
    while subsets2Worked == True and isSolved == False:
        subsets2Worked = solveSubsets(puzzle, 2) 
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
        if subsets2Worked == True:
            numChanges += 1
    if verbose == True:
        puzzle.printOptions()
    
    
    print("moving to subsets of size 3")
    subsets3Worked = True
    while subsets3Worked == True and isSolved == False:
        subsets3Worked = solveSubsets(puzzle, 3) 
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
        if subsets3Worked == True:
            numChanges += 1
    if verbose == True:
        puzzle.printOptions()
            
            
    print("moving to subsets of size 4")
    subsets4Worked = True
    while subsets4Worked == True and isSolved == False:
        subsets4Worked = solveSubsets(puzzle, 4) 
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)
        if subsets4Worked == True:
            numChanges += 1            
    puzzle.printOptions()  
        
    
    print("moving to subsets of size 5")
    subsets5Worked = True
    while subsets5Worked == True and isSolved == False:
        subsets5Worked = solveSubsets(puzzle, 5) 
        puzzle.printNumbers()
        isSolved = puzzle.isSolved()
        if isSolved == True:
            sys.exit(1)   
        if subsets5Worked == True:
            numChanges += 1         
    if verbose == True:
        puzzle.printOptions()
    
    if numChanges == 0:
        print("Puzzle cannot be solved")
        sys.exit(1)
