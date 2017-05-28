from board import Board
from evaluate import Evaluate
from search import Search
import datetime

myboard=Board('rnbqkbnr/pppppppp/8/8/8/7r/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
myboard.printBoard()
eval=Evaluate()
search=Search()

whiteknightmoves=search.generateKnightmoves(myboard,myboard.White)
myboard.makeMove(whiteknightmoves)
blackknightmoves=search.generateKnightmoves(myboard,myboard.Black)



# print("\nbegin eval...")
# start=datetime.datetime.now()
# for i in range(1):
#     eval.evaluate_node(myboard)
# end=datetime.datetime.now()
# print('finish eval...Time:',end-start)

