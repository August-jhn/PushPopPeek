from stack import *

NEUTRAL = 'RED'
WHITE = 'WHITE'
BLACK = 'BLACK'

GOESFIRST = WHITE

MOVES = {'REMOVE2' : 0, 'PLACENEUTRAL' : 1, 'PLACE' : 2}



PLAYERS = [WHITE, BLACK]


class Game:


    turn = 'WHITE'
    
    def __init__(self, board):
        self.board = []

        for i in range(4):
            row = []
            for j in range(4):
                row.append(Stack())
            self.board.append(row)

        self.turn = GOESFIRST

        while not self.checkWin():
            makeTurn()




    def checkWin(self):



        # def checkFour(seq):
        #     '''checks if diagonal, row, or col is a four-in-a-row'''
        #     start = seq[0]

        #     win = True

        #     for piece in seq:
        #         if piece != start:
        #             return False
            
        #     return True


        # self.rows = board #these just make it easier to check each turn if anyone has won
        # self.cols = [[board[i][j] for i in range(4)] for j in range(4)] #may be wrong
        # self.diags = [[board[i][i] for i in range(4)],[board[i][4- i]] for i in range(4)] #also may be wrong, need to test

        # ways = [rows, cols, diags]

        # for way in ways:
        #     for seq in way:
        #         if (checkFour(seq)):
        #             return True
        
        # return False

    
    def makeTurn(move):

        #move should be a string



        

        # if self.turn == 'WHITE':
        #     self.turn = 'BLACK'
        # else:
        #     self.turn = 'WHITE' #switch turns


