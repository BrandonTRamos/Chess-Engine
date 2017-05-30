from board import Board
from evaluate import Evaluate
from search import Search
import datetime

myboard=Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
eval=Evaluate()
search=Search()
# myboard.printBoard()
bestline=search.mini_max(myboard,eval,myboard.White,3,[])
print('--------------------------------------------------')
print('Evaluation:',bestline[0],'Bestline:',bestline[1])
# print('\n Final Board:')
# myboard.printBoard()
print('Nodes evaluated:',search.nodes)

