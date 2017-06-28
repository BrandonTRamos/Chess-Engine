from board import Board
from evaluate import Evaluate
from search import Search
import datetime

def moves_toString(movelist):
    movenumber = 1
    line = ''
    piecemap = {1: '', 2: 'N', 3: 'B', 4: 'N', 5: 'Q', 6: 'K',
                7: '', 8: 'N', 9: 'B', 10: 'R', 11: 'Q', 12: 'K'}
    intToAlgebraic = {21: 'a8', 22: 'b8', 23: 'c8', 24: 'd8', 25: 'e8', 26: 'f8', 27: 'g8', 28: 'h8',
                       31: 'a7', 32: 'b7', 33: 'c7', 34: 'd7', 35: 'e7', 36: 'f7', 37: 'g7', 38: 'h7',
                       41: 'a6', 42: 'b6', 43: 'c6', 44: 'd6', 45: 'e6', 46: 'f6', 47: 'g6', 48: 'h6',
                       51: 'a5', 52: 'b5', 53: 'c5', 54: 'd5', 55: 'e5', 56: 'f5', 57: 'g5', 58: 'h5',
                       61: 'a4', 62: 'b4', 63: 'c4', 64: 'd4', 65: 'e4', 66: 'f4', 67: 'g4', 68: 'h4',
                       71: 'a3', 72: 'b3', 73: 'c3', 74: 'd3', 75: 'e3', 76: 'f3', 77: 'g3', 78: 'h3',
                       81: 'a2', 82: 'b2', 83: 'c2', 84: 'd2', 85: 'e2', 86: 'f2', 87: 'g2', 88: 'h2',
                       91: 'a1', 92: 'b1', 93: 'c1', 94: 'd1', 95: 'e1', 96: 'f1', 97: 'g1', 98: 'h1'}
    for move in movelist:
        capturedPiece = move & 15
        toSquare = (move >> 4) & 127
        fromSquare = (move >> 11) & 127
        piece = (move >> 18) & 15
        line += ' '
        if movenumber == int(movenumber):
            line += (str(int(movenumber)) + '.')
        line += piecemap[piece]
        if capturedPiece != 0:
            line += 'x'
        line += intToAlgebraic[toSquare]
        movenumber += .5

    return line

myboard=Board('1k6/4n3/2p3p1/5P2/1N6/2P5/5K2/8 w KQkq - 0 1')
eval=Evaluate()
search=Search()
myboard.printBoard()


# print(search.is_pinned(myboard,73))
start=datetime.datetime.now()
bestline=search.mini_max(myboard,eval,myboard.sideToMove,10,[],-1000,1000)
end = datetime.datetime.now()
print('--------------------------------------------------')
print('Evaluation:',bestline[0],'Bestline:',moves_toString(bestline[1]))
# print('\n Final Board:')
# myboard.printBoard()
print('Nodes evaluated:',search.nodes)
print("Time",end-start)


