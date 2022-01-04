# Genius Square Solver
The Genius Square is a puzzle game made by The Happy Puzzle Company - https://www.happypuzzle.co.uk/family-puzzles-and-games/family-puzzles-games/genius-square  
  
I came across it on holiday once and decided to work out an algorithm to find a solution to any given board.  
I did this using Python, with a recursive algorithm, which:  
- Tries to place a piece by trying all available locations moving left to right and top to bottom, and rotating and flipping where necessary
- If it could be placed, recursively place the next piece, unless it's the last piece to be placed in which case return true
- If the recursive call returns true, that means that all remaining pieces were able to be placed, so return true
- If the recursive call returns false meaning that not all remaining pieces could be placed, try to place the piece somewhere else and try again
- If there are no possible placements of the piece that allow all remaining pieces to be placed, return false  

It attempts to place the larger pieces first, followed by the smaller ones as they are more likely to fit into gaps.

The input to the program is 7 dice values in the range of A1 to F6 which determine the coordinates to block, or alternatively the program can generate these coordinates randomly, using the dice from the actual puzzle.  
The solution found, if one exists, is outputted as a grid, where X denotes blocked coordinates, and all other coordinates contain a number denoting the piece that is placed there (e.g. 1 is the square piece, so there will be a square of 1s in the grid).
