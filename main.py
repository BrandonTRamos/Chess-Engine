from board import Board
from evaluate import Evaluate
from search import Search
import datetime

myboard=Board('1Q5K/8/3n4/4k3/8/8/8/8 b KQkq - 0 1')
eval=Evaluate()
search=Search()
myboard.printBoard()
print(search.is_pinned(myboard,44))
# bestline=search.mini_max(myboard,eval,myboard.sideToMove,7,[],-1000,1000)
# print('--------------------------------------------------')
# print('Evaluation:',bestline[0],'Bestline:',search.moves_toString(bestline[1]))
# # print('\n Final Board:')
# # myboard.printBoard()
# print('Nodes evaluated:',search.nodes)


