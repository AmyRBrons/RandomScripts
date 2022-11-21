# CISC 121 Assignment 1 - Connect 4

# This program will allow two players to engage in a game of connect four
# Once 4 of the same pieces are in a row, the player will be declared a winner

# Amy Brons - 20252295 - Jul 15, 2022


"""
The boardCreate() function sets the board as a dictionary of lists, where all columns are determined
by a letter and all empty spaces are determined by *.
"""
def boardCreate():
   
    boardLayout = {
            "A" : ["*","*","*","*","*","*"],
            "B" : ["*","*","*","*","*","*"],
            "C" : ["*","*","*","*","*","*"],
            "D" : ["*","*","*","*","*","*"],
            "E" : ["*","*","*","*","*","*"],
            "F" : ["*","*","*","*","*","*"],
            }
    return boardLayout


"""
Paramters of board, row, col, and piece are taken into this function.
The fuction determines where to place the player's piece by replacing the current item
at board[col][row] with the player piece.
"""
def placePiece(board, row, col, piece):
    board[col][row] = piece #replace the current spot with the token
    

"""
The win function take the current board layout, the selected column, and the player piece, and determines if
there is any 4 connecting pieces in a horizontal, vertical or diagonal row. If a win is determined, True will be
returned, else false.
"""
def win(boardLayout, letter, piece):
    win = False # start win at false
    
    if horizontalWin == True:
        win = True
    if verticalWin == True:
        win = True
    if diagonalUpWin == True:
        win = True
    if diagonalDownWin == True:
        win = Ture
    else:
        win = False # return false if no wins occur

"""
This function determines if there are four pieces that are the player token in a row on a column.
Because the column must start with the piece at the bottom (highest row count), and build up to 0,
this can be found by comparing the most recently dropped piece with the space under it (+1 row count),
then under thant (+2) etc.. This function must take in the boardLayout, letter and piece to determine
this function and correctly use the findRow() function.
"""
def verticalWin(boardLayout, letter, piece):
    row = findRow(boardLayout,letter)
    if boardLayout[letter][row] == boardLayout[letter][row+1] == boardLayout[letter][row+2] == boardLayout[letter][row+3] == piece:
        return True
    else:
        return False


"""
This horizontalWin function takes in the boardLayout, letter, and piece paramaters and checks the diffent ways in which the
horizontal connections can be made. Given that the board is 6 places across,there are four ways that a piece can be dropped to
garner a win. This also returns a number to determine which way the win occured, for a future function that finds and prints the
spaces involved in the win.
"""
def horizontalWin(boardLayout, letter, piece):
    winNumber = 0
        
    row = findRow(boardLayout,letter)
    if boardLayout[letter][row] == boardLayout[letter+1][row] == boardLayout[letter+2][row] == boardLayout[letter+3][row] == piece:
        return True
        winNumber = 1
    
    if boardLayout[letter][row] == boardLayout[letter-1][row] == boardLayout[letter+1][row] == boardLayout[letter+2][row] == piece:
        return True
        winNumber = 2

    if boardLayout[letter][row] == boardLayout[letter-1][row] == boardLayout[letter+1][row] == boardLayout[letter-2][row] == piece:
        return True
        winNumber = 3

    if boardLayout[letter][row] == boardLayout[letter-1][row] == boardLayout[letter-2][row] == boardLayout[letter-3][row] == piece:
        return True
        winNumber = 4
    
    else:
        return False
        

"""
This checks up-sloping diagonals for a win. There are four places that a dropped piece can complete a 4-connection diagonal.
This function compares the dropped piece to the pieces surrounding it, but changing the row and column that is being compared on the board.
The diagonalUpWin must take in the boardLayout, letter and piece to correctly execute. This also returns a number to determine which
way the win occured, for a future function that finds and prints the spaces involved in the win.
"""
def diagonalUpWin(boardLayout, letter, piece):
    row = findRow(boardLayout,letter)
    winNumber = 0

    if boardLayout[letter][row] == boardLayout[letter+1][row+1] == boardLayout[letter+2][row+2] == boardLayout[letter+3][row+3] == piece:
        return True
        winNumber = 1
    
    if boardLayout[letter][row] == boardLayout[letter-1][row-1] == boardLayout[letter+1][row+1] == boardLayout[letter+2][row+2] == piece:
        return True
        winNumber = 2

    if boardLayout[letter][row] == boardLayout[letter-1][row-1] == boardLayout[letter+1][row+1] == boardLayout[letter-2][row-2] == piece:
        return True
        winNumber = 3

    if boardLayout[letter][row] == boardLayout[letter-1][row-1] == boardLayout[letter-2][row-2] == boardLayout[letter-3][row-3] == piece:
        return True
        winNumber = 4
        
    else:
        return False


"""
This checks down-sloping diagonals for a win. There are four places that a dropped piece can complete a 4-connection diagonal.
This function compares the dropped piece to the pieces surrounding it, but changing the row and column that is being compared on the board.
The diagonalUpWin must take in the boardLayout, letter and piece to correctly execute. This also returns a number to determine which way
the win occured, for a future function that finds and prints the spaces involved in the win.
"""
def diagonalDownWin(boardLayout, letter, piece):
    row = findRow(boardLayout,letter)
    winNumber = 0
    
    if boardLayout[col][row] == boardLayout[col+1][row-1] == boardLayout[col+2][row-2] == boardLayout[col+3][row-3]:
        return True
        winNumber = 1
    
    if boardLayout[col][row] == boardLayout[col-1][row+1] == boardLayout[col+1][row-1] == boardLayout[col+2][row-2]:
        return True
        winNumber = 2

    if boardLayout[col][row] == boardLayout[col+1][row-1] == boardLayout[col-1][row+1] == boardLayout[col-2][row+2]:
        return True
        winNumber = 3
        
    if boardLayout[col][row] == boardLayout[col-1][row+1]== boardLayout[col-2][row+2] == boardLayout[col-3][row+3]:
        return True
        winNumber = 4
    
    else:
        return False

    
"""
This function takes in the boardLayout and selected column and returns the list for that key in the dictionary of
lists that makes up the board.
"""
def findList(boardLayout,letter):
    for i in range(6):
        return boardLayout[letter][i] #returns the list of items for a key in the dictionary



"""
FindRow takes the find list fuction and finds the available row that the player piece can be dropped into.
This is done by comparing the max row number (5, given that the list has 6 values), and compared to the empty symbol.
"""
def findRow(boardLayout,letter):
    rowList = findList(boardLayout,letter) # calls the list of items representing the rows of the board

    # given that pieces are dropped, starting at the highest value list item, and the list must be
    # 6 characters long, we check boardLayout[letter][5] first to see if it has been replaced with
    # a player piece. If not we return the row number, if replaced we move down to a higher row
    if boardLayout[letter][5]== "*":
        return 5

    elif boardLayout[letter][4]== "*":
        return 4
    
    elif boardLayout[letter][3]== "*":
        return 3
    
    elif boardLayout[letter][2]== "*":
        return 2

    elif boardLayout[letter][1]== "*":
        return 1
    
    elif boardLayout[letter][0]== "*":
        return 0

    else:
        return 9 # this arbitrary value will be used for error catching in the main connectFour() function    
    
    
"""
The findTokens function takes in the boolean win, player piece, and all surrounding pieces and outputs the
pieces that are connected in the connect four win.
"""
def findTokens(boardLayout, piece, letter):
    row = findRow(boardLayout, letter)


    # if a vertical win is found, the four token placements can be determined as follows
    if verticalWin(boardLayout,letter,piece) == True:
        T1 = f'{letter}{row}' # printing in an f string will allow for the format to be correct
        T2 = f'{letter}{row+1}'
        T3 = f'{letter}{row+2}'
        T4 = f'{letter}{row+3}'
        Tokens = f'{T1}\,{T2}\,{T3}\,{T4}'
        return Tokens # returns the token placements

    # if a horizontal win is found,the four token placements can be determined as follows
    if horizontalWin(boardLayout,letter,piece) == True:
        if winNumber == 1:
            T1 = f'{letter}{row}'
            T2 = f'{letter+1}{row}'
            T3 = f'{letter+2}{row}'
            T4 = f'{letter+3}{row}'
                   
        if winNumber == 2:
            T1 = f'{letter-1}{row}'
            T2 = f'{letter}{row}'
            T3 = f'{letter+1}{row}'
            T4 = f'{letter+2}{row}'

        if winNumber == 3:
            T1 = f'{letter-2}{row}'
            T2 = f'{letter-1}{row}'
            T3 = f'{letter}{row}'
            T4 = f'{letter+1}{row}'

        if winNumber == 4:
            T1 = f'{letter-3}{row}'
            T2 = f'{letter-2}{row}'
            T3 = f'{letter-1}{row}'
            T4 = f'{letter}{row}'
        
        Tokens = f'{T1}\,{T2}\,{T3}\,{T4}'
        return Tokens
    
    # if a diagonal up win is found,the four token placements can be determined as follows
    if diagonalUpWin(boardLayout, letter, piece) == True:
        if winNumber == 1:
            T1 = f'{letter}{row}'
            T2 = f'{letter+1}{row+1}'
            T3 = f'{letter+2}{row+2}'
            T4 = f'{letter+3}{row+3}'
            
        if winNumber == 2:
            T1 = f'{letter-1}{row-1}'
            T2 = f'{letter}{row}'
            T3 = f'{letter+1}{row+1}'
            T4 = f'{letter+2}{row+2}'

        if winNumber == 3:
            T1 = f'{letter-2}{row-2}'
            T2 = f'{letter-1}{row-1}'
            T3 = f'{letter}{row}'
            T4 = f'{letter+1}{row+1}'
            
        if winNumber == 4:
            T1 = f'{letter-3}{row-3}'
            T2 = f'{letter-2}{row-2}'
            T3 = f'{letter-1}{row-1}'
            T4 = f'{letter}{row}'

        Tokens = f'{T1}\,{T2}\,{T3}\,{T4}'
        return Tokens

    # if a diagonal up win is found,the four token placements can be determined as follows
    if diagonalDownWin(boardLayout, letter, piece) == True:
        if winNumber == 1:
            T1 = f'{letter}{row}'
            T2 = f'{letter+1}{row-1}'
            T3 = f'{letter+2}{row-2}'
            T4 = f'{letter+3}{row-3}'
            
        if winNumber == 2:
            T1 = f'{letter-1}{row+1}'
            T2 = f'{letter}{row}'
            T3 = f'{letter+1}{row-1}'
            T4 = f'{letter+2}{row-2}'

        if winNumber == 3:
            T1 = f'{letter-2}{row+2}'
            T2 = f'{letter-1}{row+1}'
            T3 = f'{letter}{row}'
            T4 = f'{letter+1}{row-1}'

        if winNumber == 4:
            T1 = f'{letter-3}{row+3}'
            T2 = f'{letter-2}{row+2}'
            T3 = f'{letter-1}{row+1}'
            T4 = f'{letter}{row}'

        Tokens = f'{T1}\,{T2}\,{T3}\,{T4}'
        return Tokens


"""
Function takes the dictionary of lists and prints it in a grid, using f string.
This allows the dictionary to print as a 2D square, and visualize the board whenever called.
"""
def printBoard(boardLayout):
    print("A \t B \t C \t D \t E \t F") # prints column headers
    for i in range(6):        
            print(f'{boardLayout["A"][i]}\t{boardLayout["B"][i]}\t{boardLayout["C"][i]}\t {boardLayout["D"][i]}\t {boardLayout["E"][i]}\t {boardLayout["F"][i]}')
    print()


"""
This is the main connect four function that calls other predetermined functions to play a game of connect
four between two people.
"""      
def connectFour():

    # determines the board, from our boardCreate function
    boardLayout = boardCreate()

    # lists the tow possible pieces that the players can be denoted by
    playerList = ["X","O"]

    # sets the turns and 0, to start
    turn = 0

    # sets the win to be false, noting that no one has won the game
    wins = False


    # prints opening message, the board and prompts player one to choose a token
    print("Welcome to Connect Four! Let's play!","\n","\n")
    printBoard(boardLayout)
    playerOne = input("There are to tokens available - 'X' and 'O'\
                      \nPlayer 1 -  which token would you like to use?")

    # if the player has chosen something in the token list, remove from the list, and
    # assign player two with the remaining token
    if playerOne in playerList:
        playerList.remove(playerOne)
    else:
        print("This is not a valid token")
    playerTwo = playerList[0]
    print("Player 2 - You will use token ", playerTwo)
    
    # while the game is not won, loop through the following block
    while wins == False:

        
        # if the turn is even, it is player 1's turn
        # player one gets prompted to select a column to drop their token 
        if turn %2 == 0:
            selection = input("Player 1, Make your Selection(A-F):")

            # if the selected column is a valid key in the boardLayout loop through this
            # code, else return an error
            # use findRow to find the row that the piece will be dropped onto
            # use placePiece to replace the empty symbol with the selected player token
            # print updated board with player token on it
            # determines if placed piece garners a win, and turns win to be true
            if selection in boardLayout:
                row = findRow(boardLayout,selection)
                
                if row != 9: #error catching to ensure that row is not out of bounds
                    
                    placePiece(boardLayout, row, selection, playerOne)
                    printBoard(boardLayout)
                    wins = win(boardLayout, selection, playerOne)
                else:
                    print("Column is full, not a valid selection.")
                turn +=1  # add 1 to turn count 
                
            else:
                print("Not a valid selection")


            
        # if the turn is odd, it is player 2's turn
        # player two gets prompted to select a column to drop their token   
        if turn %2 != 0:
            selection = input("Player 2, Make your Selection(A-F):")

            # if the selected column is a valid key in the boardLayout loop through this
            # code, else return an error
            # use findRow to find the row that the piece will be dropped onto
            # use placePiece to replace the empty symbol with the selected player token
            # print updated board with player token on it
            # determines if placed piece garners a win, and turns win to be true
            if selection in boardLayout:
                row = findRow(boardLayout,selection)

                if row != 9: #error catching to ensure that row is not out of bounds
                    
                    placePiece(boardLayout, row, selection, playerTwo)
                    printBoard(boardLayout)
                    wins = win(boardLayout, selection, playerOne)
                else:
                    print("Column is full, not a valid selection.")
                turn +=1 # add 1 to turn count 

                
            else:
                print("Not a valid selection")


    # if win returns a true, the winner can be determined by which turn the play ended on
    # this is opposite of above, where player one would win if ends on an odd, and player two ends on an even
    else:
        if turn %2 == 0:
            # calls function to find connecting tokens to add to print statment
            print("Win! Congrats to Player One for the victory!", findTokens(boardLayout,playerOne,selection) )

            
        if turn %2 !=0:
            # calls function to find connecting tokens to add to print statment
            print("Win! Congrats to Player Two for the victory!", findTokens(boardLayout,playerTwo,selection))



"""
Main function calls the connectFour() function, and starts the game
"""
def main():
    start = connectFour()

#main is called
main()
