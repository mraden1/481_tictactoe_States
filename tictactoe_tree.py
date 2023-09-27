def PlayTicTacToe(board, player):
    if CheckForWin(board):
        print('game finished')
    else:
        for i in range(len(board)):
            if board[i] == '-':
                board[i] = player
                PrintBoard(board)
                if player == 'O':
                    PlayTicTacToe(board, 'X')
                elif player == 'X':
                    PlayTicTacToe(board, 'O')
                board[i] = '-'

def HorizontalWin(board):
    if ((board[0] != '-' and board[0] == board[1] == board[2]) or
        (board[3] != '-' and board[3] == board[4] == board[5]) or
        (board[6] != '-' and board[6] == board[7] == board[8])):
        print('Horizontal Win')
        return True
    else:
        return False

def VerticalWin(board):
    if ((board[0] != '-' and board[0] == board[3] == board[6]) or
        (board[1] != '-' and board[1] == board[4] == board[7]) or
        (board[2] != '-' and board[2] == board[5] == board[8])):
        print('Vertical win')
        return True
    else:
        return False

def CrossWin(board):
    if ((board[0] != '-' and board[0] == board[4] == board[8]) or
        (board[6] != '-' and board[6] == board[4] == board[2])):
        print('Cross win')
        return True
    else:
        return False

def CheckForWin(board):
    if HorizontalWin(board) or VerticalWin(board) or CrossWin(board):
        return True
    else:
        return False

def PrintBoard(board):
    index = 0
    while index < 7:
        print('|' + str(board[index]) +
              '|' + str(board[index+1]) +
              '|' + str(board[index+2] +
              '|'))
        index += 3

board = ['-']*9
PlayTicTacToe(board, 'O')
