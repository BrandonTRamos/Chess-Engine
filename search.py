class Search():

    def generateKnightmoves(self,board,side):
        knightoffsets=[8,12,19,21,-8,-12,-19,-21]
        moves=[]
        if side==board.White:
            for square in board.whiteKnightsq:
                fromsquare=square
                for offset in knightoffsets:
                    move=fromsquare
                    if board.board[fromsquare-offset]!=99 and fromsquare-offset not in board.whitepiecesq:
                        move=(move<<7|(fromsquare-offset))
                        moves.append(move)
        else:
            for square in board.blackKnightsq:
                fromsquare=square
                for offset in knightoffsets:
                    move=fromsquare
                    if board.board[fromsquare-offset]!=99 and fromsquare-offset not in board.blackpiecesq:
                        move=(move<<7|(fromsquare-offset))
                        moves.append(move)
        return moves






    def generateMoves(self,board):
        movelist = []
        if board.sideToMove==0:
            for sq in board.legalsquares:
                pass
        return movelist

