from board import Board
from evaluate import Evaluate
from search import Search
import datetime
myboard=Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
myboard.printBoard()
eval=Evaluate()
# search=Search()
start=datetime.datetime.now()
for i in range(1000000):
    eval.evaluate_node(myboard.board)
end=datetime.datetime.now()
print("Done",end-start)

