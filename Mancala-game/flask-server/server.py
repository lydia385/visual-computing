from flask import Flask,request
from flask_cors import CORS
from Game import Game
from MancalaBoard import MancalaBoard
from Play import MinMax
import json
import time
app = Flask(__name__)

CORS(app)

@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
      state = request.json
      if state != None:
        s = MancalaBoard()
        D = {'A': state['players'][0]['field'][0],
        'B': state['players'][0]['field'][1],
        'C': state['players'][0]['field'][2],
        'D': state['players'][0]['field'][3],
        'E': state['players'][0]['field'][4],
        'F': state['players'][0]['field'][5],
         1: state['players'][0]['field'][6],
        'G': state['players'][1]['field'][0],
        'H': state['players'][1]['field'][1],
        'I': state['players'][1]['field'][2],
        'J': state['players'][1]['field'][3],
        'K': state['players'][1]['field'][4],
        'L': state['players'][1]['field'][5],
        2: state['players'][1]['field'][6],

        }
        s.board = D
        game = Game(s,1)
        if state['players'][state['turn']]['type'] == 'bot':
            player=1
            s= game.state.board.copy()
            #move= NegaMaxAlphaBetaPruning(g, player, 5, (math.inf), -(math.inf))
            #index,value= MinMax(g, player, 5)
            index= MinMax(game,player,5)
            game.state.board=s
            index = game.state.ind_player1.index(game.bestMove)
            print("index",index)
            next_player=game.state.doMove(player,game.bestMove)
            move_D = {
                'move':index,
                'player' :next_player
            }
            # x= list(p.state.board.values())
            # state['players'][1]['field'] = x[0:7]
            # state['players'][0]['field'] = x[7:14]
            # state['turn'] = next_player
            with open("state.txt",'w',encoding = 'utf-8') as f:
                f.write(json.dumps(move_D))
            f.close()
            with open("history.txt",'a',encoding = 'utf-8') as f:
                f.write(json.dumps(move_D))
            f.close()
        
    return "No  information is given"

@app.route('/content', methods=['GET'])

def content(): 
    f= open('state.txt', 'r') 
    time.sleep(3)
    line= f.readline()
    f.close()
    return line        



        
if __name__ == "__main__":
    app.run(host="localhost",port=8000, debug=True)