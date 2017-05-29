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
                    if board.board[toSquare]!=99 and board.board[toSquare]!=6  and toSquare not in board.whitepiecesq:
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
                    if board.board[toSquare]!=99 and board.board[toSquare]!=12 and toSquare not in board.blackpiecesq:
                        if board.board[toSquare] in board.whitePieces:
                            capturedPiece=board.board[toSquare]
                        move=(move<<7)|fromsquare
                        move=(move<<7)|toSquare
                        move=(move<<4)|capturedPiece
                        moves.append(move)

        # print('BOARD WITHIN GENMOVES:')
        # board.printBoard()
        # print('MOVES WITHIN GENMOVES:',moves)
        return moves






    def searchPosition(self,board,evaluate,side,depth):
        board.sideToMove=side
        print('side to move',board.sideToMove)
        if depth==0:
            print('Max depth reached, evaluation:',evaluate.evaluate_node(board))

        elif side==board.White:
            whitemoves=self.generateKnightmoves(board,board.White)
            for move in whitemoves:
                print('whitemoves @ depth',depth,':',whitemoves)
                print('white making @ depth:',depth,'Move:',move)
                board.makeMove(move)
                board.printBoard()
                self.searchPosition(board,evaluate,board.Black,depth-1)
                print('whiteunmaking @ depth:',depth,'Move:',move)
                board.unmakeMove(move)

        else:
            blackmoves=self.generateKnightmoves(board,board.Black)
            for move in blackmoves:
                print('blackmoves:',blackmoves)
                print('black making @ depth:', depth,'Move:',move)
                board.makeMove(move)
                board.printBoard()
                self.searchPosition(board,evaluate,board.White,depth-1)
                print('black unmaking @ depth:', depth,'Move:',move)
                board.unmakeMove(move)
