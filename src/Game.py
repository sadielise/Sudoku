from Puzzle import SudokuPuzzle

puzzle = SudokuPuzzle('puzzle3.txt')
puzzle.printNumbers()
puzzle.printOptions()

changeMade = True
while changeMade == True:
    changeMade = puzzle.findCellWithOneOption()
    puzzle.printNumbers()
