def createField(field):
    for row in range(7): 
        if(row%2 == 0):
            createRow=int(row/2)
            for column in range(7):
                createColumn= int(column/2)
                if(column%2==0):
                    if(column != 6):
                        print(field[createColumn][createRow],end="")
                    else:
                        print(field[createColumn][createRow])
                else:
                    print("|",end="")
        else:
            print("-------")

def GameCheck(CountPlayer1,CountPlayer2):
    if(CountPlayer1>=4 or CountPlayer2>=4):
        print("Game check")
        for c in range(4):
            for r in range(6):
                if(currentField[r][c]=="O" and currentField[r][c+1] == "O" and currentField[r][c+2] == "O" and currentField[r][c+3] == "O"):
                    print("Player 2 win")
                    break
                elif(currentField[r][c]=="X" and currentField[r][c+1] == "X" and currentField[r][c+2] == "X" and currentField[r][c+3] == "X"):
                    print("Player 1 win")
                    break

        for c in range(7):
            for r in range(3):
                if(currentField[r][c]=="O" and currentField[r+1][c] == "O" and currentField[r+2][c] == "O" and currentField[r+3][c] == "O"):
                    print("Player 2 win")
                    break
                elif currentField[r][c] == "X" and currentField[r+1][c] == "X" and currentField[r+2][c] == "X" and currentField[r+3][c] == "X":
                    print("Player 1 win")
                    break

        # Check positively sloped diaganols
        for c in range(4):
            for r in range(3):
                if(currentField[r][c]=="O" and currentField[r+1][c+1] == "O" and currentField[r+2][c+2] == "O" and currentField[r+3][c+3] == "O"):
                    print("Player 2 win")
                    break
                elif currentField[r][c] == "X" and currentField[r+1][c+1] == "X" and currentField[r+2][c+2] == "X" and currentField[r+3][c+3] == "X":
                    print("Player 1 win")
                    break
                    
        # Check negatively sloped diaganols
        for c in range(4):
            for r in range(3,6):
                if(currentField[r][c]=="O" and currentField[r-1][c+1] == "O" and currentField[r-2][c+2] == "O" and currentField[r-3][c+3] == "O"):
                    print("Player 2 win")
                    break
                elif currentField[r][c] == "X" and currentField[r-1][c+1] == "X" and currentField[r-2][c+2] == "X" and currentField[r-3][c+3] == "X":
                    print("Player 1 win")
                    break


currentField = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
createField(currentField)       
Player = 1
CountPlayer1 =0
CountPlayer2 =0

while(True):
    print("Players turn: ",Player)
    MoveRow = int(input("Please enter the row\n"))       # Convert the row to integer
    MoveColumn = int(input("Please enter the column\n"))

    if(Player == 1):
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            CountPlayer1 +=1
            Player = 2
            print("CountPlayer1",CountPlayer1)
    else:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            CountPlayer2 +=1
            Player = 1

    createField(currentField)
    GameCheck(CountPlayer1,CountPlayer2)


