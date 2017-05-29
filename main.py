from board import Board
from evaluate import Evaluate
from search import Search
import datetime

myboard=Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
# myboard.printBoard()
eval=Evaluate()
search=Search()
myboard.printBoard()
print('\nWhite')
search.searchPosition(myboard,eval,myboard.White,3)
print('\n Final Board:')
myboard.printBoard()


