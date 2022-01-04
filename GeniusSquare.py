# Get coordinates from dice value
def diceToCoor(coor, printCoor): 
    if printCoor:
        print(coor)
    return (int(coor[1])-1,letters.index(coor[0]))  
            
# Check if the given piece can fit at the given coordinates
def checkFit(piece, x, y, pieceChar): 
    global board
    for s in piece:
        if x+s[0] < 0 or x+s[0] > 5:
            return False
        elif y+s[1] < 0 or y+s[1] > 5:
            return False
        elif board[y+s[1]][x+s[0]] != "0":
            return False
    board[y][x] = pieceChar
    for s in piece:
        board[y+s[1]][x+s[0]] = pieceChar
    return True

# Check if the given piece turned 180 degrees can fit at the given coordinates
def checkFit180(piece, x, y, pieceChar): 
    global board
    for s in piece:
        if x-s[0] < 0 or x-s[0] > 5:
            return False
        elif y-s[1] < 0 or y-s[1] > 5:
            return False
        elif board[y-s[1]][x-s[0]] != "0":
            return False
    board[y][x] = pieceChar
    for s in piece:
        board[y-s[1]][x-s[0]] = pieceChar
    return True

# Remove all instances of a character from the board
def removeFromBoard(char): 
    global board
    for r in range(6):
        if char in board[r]:
            board[r] = ["0" if i == char else i for i in board[r]]

# Recursive function for placing pieces on the board to solve the puzzle
def placePiece(pieceNo): 
    global board
    global pieces0
    global pieces90
    global noRotSymmetry
    global piecesFlipped0
    global piecesFlipped90
    
    for y in range(6):
        for x in range(6):
            if board[y][x] == "0":

                # Try to place the piece at (x,y)
                if checkFit(pieces0[pieceNo],x,y,str(pieceNo+1)):
                    if pieceNo == 7:
                        return True
                    elif placePiece(pieceNo+1):
                        return True
                    else:
                        removeFromBoard(str(pieceNo+1))

                # Try to place the piece at (x,y) after rotating it 90 degrees
                if checkFit(pieces90[pieceNo],x,y,str(pieceNo+1)):
                    if pieceNo == 7:
                        return True
                    elif placePiece(pieceNo+1):
                        return True
                    else:
                        removeFromBoard(str(pieceNo+1))

                # Try to place the piece at (x,y) after rotating it 180 or 270 degrees, if it has no rotational symmetry
                if pieceNo in noRotSymmetry:
                    if checkFit180(pieces0[pieceNo],x,y,str(pieceNo+1)):
                        if placePiece(pieceNo+1):
                            return True
                        else:
                            removeFromBoard(str(pieceNo+1))
                                              
                    if checkFit180(pieces90[pieceNo],x,y,str(pieceNo+1)):
                        if placePiece(pieceNo+1):
                            return True
                        else:
                            removeFromBoard(str(pieceNo+1))

                # Try to place the piece at (x,y) in rotations after flipping it, if it has no symmetry
                if pieceNo == 2 or pieceNo == 3:
                    if checkFit(piecesFlipped0[pieceNo],x,y,str(pieceNo+1)):
                        if placePiece(pieceNo+1):
                            return True
                        else:
                            removeFromBoard(str(pieceNo+1))
                                              
                    if checkFit(piecesFlipped90[pieceNo],x,y,str(pieceNo+1)):
                        if placePiece(pieceNo+1):
                            return True
                        else:
                            removeFromBoard(str(pieceNo+1))
                                              
                    if pieceNo == 3:
                        if checkFit180(piecesFlipped0[3],x,y,"4"):
                            if placePiece(4):
                                return True
                            else:
                                removeFromBoard("4")
                                                        
                        if checkFit180(piecesFlipped90[3],x,y,"4"):
                            if placePiece(4):
                                return True
                            else:
                                removeFromBoard("4")
    
    # If the piece cannot fit anywhere in a way that allows all remaining pieces to be placed, return false
    return False

import random

letters = ["A","B","C","D","E","F"]
dice = [["A1", "C1", "D1", "D2", "E2", "F3"], ["A2", "A3", "B1", "B2", "B3", "C2"], ["A4", "B5", "C5", "C6", "D6", "F6"], ["A5", "A5", "B6", "E1", "F2", "F2"], ["A6", "F1"], ["B4", "C3", "C4", "D3", "D4", "E3"], ["D5", "E4", "E5", "E6", "F4", "F5"]] 
board = [["0","0","0","0","0","0"], ["0","0","0","0","0","0"], ["0","0","0","0","0","0"], ["0","0","0","0","0","0"], ["0","0","0","0","0","0"], ["0","0","0","0","0","0"]]

# The pieces to be placed on the board, specified by coordinates of components of the piece relative to a reference piece component at (0,0)
# First in one orientation (pieces0), then rotated 90 degrees clockwise (pieces90)
pieces0 = [[(1,0),(1,1),(0,1)], [(1,0),(2,0),(3,0)], [(1,0),(1,1),(2,1)], [(1,0),(2,0),(0,1)], [(1,0),(2,0),(1,1)], [(1,0),(0,1)], [(1,0),(2,0)], [(1,0)]]
pieces90 = [[(0,1),(-1,0),(-1,1)], [(0,1),(0,2),(0,3)], [(0,1),(-1,1),(-1,2)], [(0,1),(0,2),(-1,0)], [(0,1),(0,2),(-1,1)], [(0,1),(-1,0)], [(0,1),(0,2)], [(0,1)]]

# Indexes of pieces with no rotational symmetry
noRotSymmetry = [3,4,5]

# Pieces flipped and rotated 0 and 90 degrees clockwise, only for pieces with no symmetry
piecesFlipped0 = [[], [], [(-1,0),(-1,1),(-2,1)], [(-1,0),(-2,0),(0,1)], [], [], [], []]
piecesFlipped90 = [[], [], [(0,-1),(-1,-1),(-1,-2)], [(-1,0),(0,-1),(0,-2)], [], [], [], []]

print("Input 7 dice coordinates or press enter for random dice")

die = input("Input dice: ").upper()
if die == "":
    print("\nGenerated dice:")
    for d in dice:
        (x,y) = diceToCoor(random.choice(d),True)
        board[y][x] = "X"
else:
    for i in range(7):
        valid = False
        while not valid:
            if die == "":
                die = input("Input dice: ").upper()
            if len(die) != 2 or die[0] not in letters or die[1] not in ["1","2","3","4","5","6"]:
                print("Invalid dice - must be in the range A1-F6")
                die = ""
            else:
                valid = True
        (x,y) = diceToCoor(die,False)
        board[y][x] = "X"
        die = ""

print()
if placePiece(0):
    print("Solution found!\n")

    for r in board:
        for c in r:
            print(c,end=" ")
        print()
else:
    print("This puzzle cannot be solved.")
