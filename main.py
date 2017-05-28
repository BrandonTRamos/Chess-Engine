from board import Board
from evaluate import Evaluate
from search import Search
import datetime

myboard=Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
myboard.printBoard()
eval=Evaluate()
search=Search()

whiteknightmoves=search.generateKnightmoves(myboard,myboard.White)
blackknightmoves=search.generateKnightmoves(myboard,myboard.Black)

print("white knight moves:",whiteknightmoves)
for move in whiteknightmoves:
    print("from:",(move>>7)&127)
    print("to:", move & 127)
print("\nblack knight moves:",blackknightmoves)
for move in blackknightmoves:
    print("from:",(move>>7)&127)
    print("to:", move & 127)



# print("\nbegin eval...")
# start=datetime.datetime.now()
# for i in range(1):
#     eval.evaluate_node(myboard)
# end=datetime.datetime.now()
# print('finish eval...Time:',end-start)

