
class MancalaBoard:
    def __init__(self):
        #changer plyer magasin a 1 et -1
        self.board = {'A':4,'B':4,'C':4,'D':4,'E':4,'F':4,1:0,'G':4,'H':4,'I':4,'J':4,'K':4,'L':4,2:0}
        self.ind_player1 = ('A','B','C','D','E','F')
        self.ind_player2 = ('G','H','I','J','K','L')
    
    def possibleMoves(self,player):
        if player == 1 :
            return [x for x in self.ind_player1 if self.board[x]!=0 ]
        elif player == -1:
            return [x for x in self.ind_player2 if self.board[x]!=0 ]



    def doMove(self,player,move_player):
         possible_move =self.possibleMoves(player)
         if( len(possible_move)!= 0):
           graines_move = self.board[move_player]
           K = list(self.board.keys())
           if player == 1 :
                 move_player_FS=self.ind_player1.index(move_player)+1
           elif player == -1 :
                move_player_FS= 6+self.ind_player2.index(move_player)+2
           for i in range(graines_move):
              if move_player_FS== len(K)-1 :      
                  key = K[len(K)-1]
                  self.board[key]+=1   
                  move_player_FS= 0
              else :
                    key = K[move_player_FS]
                    self.board[key]+=1
                    move_player_FS+=1
              #print("move_player_FS",move_player_FS,"player",player)
           self.board[move_player] = 0
           if (self.board[K[move_player_FS]]==1)  :
            if  (K[move_player_FS] in self.ind_player1 and player == -1 ):
                self.board[1] +=   self.board[K[move_player_FS]]
            elif (K[move_player_FS] in self.ind_player2 and player == 1 ):
                self.board[2] +=   self.board[K[move_player_FS]]
           if ((player ==1 and move_player_FS-1 ==6 )or (player==-1 and move_player_FS == 0) ):
              
              return player
           else : 
               return (-1)*player

        



