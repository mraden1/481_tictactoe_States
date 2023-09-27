import networkx as nx
import matplotlib.pyplot as plt

class TTTGraph:
    def __init__(self):
        self.graph = nx.Graph()
        self.node_list = []
        self.horizontal = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        self.vertical = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
        self.criss = [(0, 4, 8), (6, 4, 2)]
        self.wins = [self.horizontal, self.vertical, self.criss]

    def addNode(self, board, player):
        self.node_list.append(BoardNode(board, player))

    def getNodeList(self):
        print(str(self.node_list))
        return self.node_list

    def checkForWin(self):
        for j in self.node_list:
            for each in self.wins:
                for item in each:
                    if (j.getState()[item[0]] != None) and (j.getState()[item[0]] == j.getState()[item[1]] == j.getState()[item[2]]):
                        j.setWin()
                        j.printBoard()
                        print("is winner!")
                        return True

class BoardNode:

    def __init__ (self, board, player):
        self.board = board
        self.next_states = []
        self.next_nodes = []
        self.player = player
        self.win = False

    def getState(self):
        return self.board

    def setState(self, board):
        self.board = board

    def generateNextStates(self):
        for i in range(len(self.board)):
            if self.board[i] == None:
                new_board = [None]*9
                new_board[i] = self.player
                self.next_states.append(new_board)

    def generateNextNodes(self):
        for i in range(len(self.next_states)):
            if self.player == 'X':
                self.next_nodes.append(BoardNode(self.next_states[i], 'O'))
            else:
                self.next_nodes.append(BoardNode(self.next_states[i], 'X'))

    def getNextNodes(self):
        return self.next_nodes

    def setWin(self):
        self.win = True

    def getWin(self):
        return self.win

    def printNextStates(self):
        for each in self.next_states:
            print(str(each))

    def printBoard(self):
        i = 0
        while i < 7:
            print('|'+ str(self.board[i]) + '|' + str(self.board[i+1]) + '|' + str(self.board[i+2]) + '|')
            i += 3

def PlayTicTacToe(board, player):
    print(board)
    print(player)
    while checkForWin(board) != True:
        index = 0
        while index < len(board):
            if (board[index] == None) and (player == 'O'):
                new_board = board
                board[index] = player
                player = 'X'
                index += 1
                PlayTicTacToe(board, player)
                board = new_board
                
            elif (board[index] == None) and (player == 'X'):
                new_board = board
                board[index] = player
                player = 'O'
                index += 1
                PlayTicTacToe(board, player)
                board = new_board
                



horizontal = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
vertical = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
criss = [(0, 4, 8), (6, 4, 2)]
wins = [horizontal, vertical, criss]

def checkForWin(board):
    for each in wins:
        for item in each:
            if (board[item[0]] != None) and (board[item[0]] == board[item[1]] == board[item[2]]):
                print(board)
                print("is winner!")

board = [None]*9

PlayTicTacToe(board, 'O')
