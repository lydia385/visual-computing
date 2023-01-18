from copy import deepcopy
import random
import numpy as np
from operator import itemgetter

class Game:
    def __init__(self,state,playerSide=[1,-1]):
        self.state = state
        self.playerSide=playerSide
        self.bestMove = None
    def gameOver(self):
        if len(self.state.possibleMoves(1))==0 or len(self.state.possibleMoves(-1))==0 :
            if len(self.state.possibleMoves(1))==0 :
                l= [x for x in self.state.ind_player2 if self.state.board[x]!=0 ]
                for i in l:
                    self.state.board[2]+=self.state.board[i]
            else :
                l= [x for x in self.state.ind_player1 if self.state.board[x]!=0 ]
                for i in l:
                    self.state.board[1]+=self.state.board[i]
            return True
        else:
            return False
    def findWinner(self):
        # winner.append(self.state.board[1])
        # winner.append(self.state.board[2])
        # winner = np.array[]
        winner = np.array([self.state.board[1],self.state.board[2]])
        

        winner = winner.argmax()
        return winner+1

        
    def evaluate(self):
          return self.state.board[1]-self.state.board[2]
          
    

    def evaluate2(self):
        store1 = self.state.board[1]
        store2= self.state.board[2]

        somme_max = 0
        somme_min = 0
        weight = 10

        for key, value in self.state.board.items():
            if key in self.state.possibleMoves(1):
                somme_max += value
            elif key in self.state.possibleMoves(-1):
                somme_min += value

        evaluation = (weight*store1 + somme_max) - \
            (weight*store2 + somme_min)
        return evaluation


    def evalute4_MonteCarlo(self, mcts_iteration=600):
        gain = 0
        for _ in range(mcts_iteration):
            game_copy= deepcopy(self)
            mancala_game= game_copy.state
            player=game_copy.playerSide

            while not game_copy.gameOver():
                #choose random
                        if len(mancala_game.possible_moves(current_player)) > 0:
                            moves = mancala_game.possible_moves(current_player)
                            move = moves[random.randint(0, len(moves)-1)]
                            current_player = mancala_game.do_move(move, current_player)
            winner = game_copy.findWinner()
            winner= -1 if winner==1 else 1 # change 1 to 2
            
            if winner == player :   
                gain+=1 
            
        return gain