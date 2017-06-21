from board import Board
from evaluate import Evaluate
from search import Search
import datetime
myboard=Board('rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 0 1')
eval=Evaluate()
search=Search()
myboard.printBoard()
# print(search.is_pinned(myboard,73))
start=datetime.datetime.now()
bestline=search.mini_max(myboard,eval,myboard.sideToMove,11,[],-1000,1000)
end = datetime.datetime.now()
print('--------------------------------------------------')
print('Evaluation:',bestline[0],'Bestline:',search.moves_toString(bestline[1]))
# print('\n Final Board:')
# myboard.printBoard()
print('Nodes evaluated:',search.nodes)
print("Time",end-start)


