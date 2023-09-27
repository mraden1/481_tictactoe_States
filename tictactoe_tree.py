def PlayTicTacToe(board, player):
    for i in range(len(board)):
        if board[i] == None:
            board[i] = player
            print(board)
            board[i] = None

board = [None]*9
board[1] = 'O'
board[4] = 'X'
PlayTicTacToe(board, 'O')
