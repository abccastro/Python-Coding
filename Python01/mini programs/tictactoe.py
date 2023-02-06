"""
Create a two-player Tic Tac Toe game
Created by: Auradee Castro
"""

tictactoe_board = [[" "] * 3 for i in range(3)]  # initialize tic-tac-toe grid


def startGame():
    print("Welcome to Tic Tac Toe")

    turn_counter = 0
    player = "X"
    has_winner = False

    while True:
        displayBoard()

        if turn_counter >= 5:
            has_winner = checkWinner(player)

        if has_winner or turn_counter == 9:
            if has_winner:
                print(player, "wins!")
            else:
                print("It's a tie...")
            print("Game over!")
            break

        else:
            player = getCurrentPlayer(turn_counter)

            is_cell_empty = False
            while not is_cell_empty:
                row = pickRowNumber()
                column = pickColumnNumber()
                is_cell_empty = isCellEmpty(row, column)
            else:
                turn_counter += 1

            setPlayersPick(player, row, column)
            print()


def displayBoard():
    for row in tictactoe_board:
        print("+---+---+---+")
        print("|", row[0], "|", row[1], "|", row[2], "|")
    else:
        print("+---+---+---+")


def getCurrentPlayer(turn_counter):
    if turn_counter % 2 == 0:
        player = "X"
    else:
        player = "O"

    print(player + "'s turn")
    return player


def pickRowNumber():
    while True:
        row = input("Pick a row (1, 2, 3): ")
        if row.isdigit() and int(row)-1 in range(3):
            break
        else:
            print("Invalid row number")
    return int(row)


def pickColumnNumber():
    while True:
        column = input("Pick a column (1, 2, 3): ")
        if column.isdigit() and int(column)-1 in range(3):
            break
        else:
            print("Invalid column number")
    return int(column)


def isCellEmpty(row, column):
    if tictactoe_board[row - 1][column - 1] == " ":
        return True
    else:
        print("Cell is already taken. Pick another one.")
        return False


def setPlayersPick(player, row, column):
    record = tictactoe_board[row - 1]
    record[column - 1] = player


def checkWinner(player):
    # check rows
    for row in range(3):
        if tictactoe_board[row][0] == player and tictactoe_board[row][1] == player and tictactoe_board[row][2] == player:
            return True

    # check columns
    for col in range(3):
        if tictactoe_board[0][col] == player and tictactoe_board[1][col] == player and tictactoe_board[2][col] == player:
            return True

    # check diagonal
    for x in range(3):
        if tictactoe_board[x][x] != player:
            break
    else:
        return True

    # check opposite diagonal
    for x in range(3):
        if tictactoe_board[x][(x+1)*(-1)] != player:
            break
    else:
        return True


if __name__ == "__main__":
    startGame()
