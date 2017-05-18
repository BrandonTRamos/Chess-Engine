from board import Board
from evaluate import Evaluate
myboard=Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
myboard.printBoard()
eval=Evaluate()
print('\nEvaluation:',eval.evaluate_node(myboard.board))
