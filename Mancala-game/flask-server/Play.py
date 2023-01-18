from MancalaBoard import MancalaBoard
from Game import Game
import math
from copy import *


def humanTurn(game):
    gotIt  = False

    while gotIt == False:
        x = input("votre tours! choisisez votre fosse: ")
        L= game.state.possibleMoves(-1)
        if x in  L: 
            #move =L.index(x)
            next_player=game.state.doMove(-1,x)
            gotIt = True
            print(game.state.board)
            return game,next_player
        else : print('refaire \n')

def NegaMaxAlphaBetaPruning(game, player, depth,bestPit, alpha, beta):
       
        if game.gameOver() or depth == 1:
          
            bestValue = game.evaluate2()
            bestPit =None
            if player == -1:
                bestValue = -bestValue

            return bestValue, bestPit
        
        bestValue = -math.inf
        #bestPit = None
        for pit in game.state.possibleMoves(player):
            child_game =  deepcopy(game)
            child_game.state.doMove(player,pit)
            value, _ = NegaMaxAlphaBetaPruning(child_game, -player, depth-1,bestPit, -beta, -alpha)
            value = (-1)*value
            if value > bestValue:
            
                bestValue = value
                bestPit =pit
                print(game.state.possibleMoves(player), bestPit)
                
            if bestValue > alpha:
    
                alpha = bestValue
    
            if beta <= alpha:
                break

    
        return bestValue, bestPit


def MinMax(game,player,depth=5):
    if depth == 1 or game.gameOver():
        return game.evaluate2(),game.bestMove
    bestValue = player* (-math.inf)
    child_game =  deepcopy(game)
    for move in game.state.possibleMoves(player):
        child_game.state.doMove(player,move)
        value,_ = MinMax(child_game,player,depth)
        
        if player == 1 :
            if value> bestValue :
                bestValue = value

        else:
            if value< bestValue :
                bestValue = value
    game.bestMove = move

    return bestValue,game.bestMove






def computerTurn(game,player,depth, alpha, beta):
      s= deepcopy(game.state.board)
      #move= NegaMaxAlphaBetaPruning(game, player, depth,'C', alpha, beta)
      index= MinMax(game,player,depth)
      game.state.board=s
      next_player=game.state.doMove(player,game.bestMove)
      print(game.state.board)
      return game,next_player


# s= MancalaBoard()
# #player=[1,-1]
# g=Game(s,1)

# print("Computer\n")

# p,next_player = computerTurn(g,1,5,(math.inf),-(math.inf))
# print("Computer\n") if next_player==2 else print("User\n")

# while True:
#     if next_player== 1 :
#         p,next_player = computerTurn(p,1,5,(math.inf),-(math.inf))
#     else : 
#         p,next_player=humanTurn(p)
#     print("Computer\n") if next_player==1 else print("\n\nUser\n")
