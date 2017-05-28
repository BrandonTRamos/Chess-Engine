class Search():

    def generateKnightmoves(self,board,side):
        knightoffsets=[8,12,19,21,-8,-12,-19,-21]
        moves=[]
        if side==board.White:
            for square in board.whiteKnightsq:
                fromsquare=square
                for offset in knightoffsets:
                    capturedPiece = 0
                    move = 8
                    toSquare = fromsquare + offset
                    if board.board[toSquare]!=99 and toSquare not in board.whitepiecesq:
                        if board.board[toSquare] in board.blackPieces:
                            capturedPiece=board.board[toSquare]
                        move=(move<<7)|fromsquare
                        move=(move<<7)|toSquare
                        move=(move<<4)|capturedPiece
                        moves.append(move)
        else:
            for square in board.blackKnightsq:
                fromsquare=square
                for offset in knightoffsets:
                    capturedPiece = 0
                    move = 2
                    toSquare=fromsquare+offset
                    if board.board[toSquare]!=99 and toSquare not in board.blackpiecesq:
                        if board.board[toSquare] in board.whitePieces:
                            capturedPiece=board.board[toSquare]
                        move=(move<<7)|fromsquare
                        move=(move<<7)|toSquare
                        move=(move<<4)|capturedPiece
                        moves.append(move)
        return moves






    def generateMoves(self,board):
        movelist = []
        if board.sideToMove==0:
            for sq in board.legalsquares:
                pass
        return movelist

