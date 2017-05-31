class Search():
    nodes=0
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
                    if board.board[toSquare]!=board.OffBoard and board.board[toSquare]!=board.BlackKing and toSquare not in board.whitepiecesq:
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
                    if board.board[toSquare]!=board.OffBoard and board.board[toSquare]!=board.WhiteKing and toSquare not in board.blackpiecesq:
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



    def get_max(self,line,bestline):
        if line[0]>bestline[0]:
            return line
        else:
            return bestline

    def get_min(self,line,bestline):
        if line[0]<bestline[0]:
            return line
        else:
            return bestline


    def mini_max(self,board,evaluate,side,depth,movelist,alpha,beta):
        board.sideToMove=side
        print('____________________________________________________')
        print('\nside to move',board.sideToMove)
        if depth==0:
            moves=movelist[:]
            print('Max depth reached, evaluation:',evaluate.evaluate_node(board))
            print('Result:',(evaluate.evaluate_node(board),moves))
            print('________________________________________________')
            self.nodes+=1
            return (evaluate.evaluate_node(board),moves)

        elif side==board.White:
            maxbestLine=(-1000,[])
            whitemoves=self.generateKnightmoves(board,board.White)
            for move in whitemoves:
                movelist.append(move)
                # print('whitemoves @ depth',depth,':',whitemoves)
                # print('white making @ depth:',depth,'Move:',move)
                board.makeMove(move)
                board.printBoard()
                line=self.mini_max(board,evaluate,board.Black,depth-1,movelist,alpha,beta)
                # print('whiteunmaking @ depth:',depth,'Move:',move)
                maxbestLine = self.get_max(line,maxbestLine)
                board.unmakeMove(move)
                movelist.pop()
                alpha = max(alpha, maxbestLine[0])
                if alpha >=beta:
                    break
            return maxbestLine


        else:
            minbestLine=(1000,[])
            blackmoves=self.generateKnightmoves(board,board.Black)
            for move in blackmoves:
                movelist.append(move)
                # print('blackmoves:',blackmoves)
                # print('black making @ depth:', depth,'Move:',move)
                board.makeMove(move)
                board.printBoard()
                line=self.mini_max(board,evaluate,board.White,depth-1,movelist,alpha,beta)
                # print('black unmaking @ depth:', depth,'Move:',move)
                minbestLine = self.get_min(line,minbestLine)
                board.unmakeMove(move)
                movelist.pop()
                beta=min(beta,minbestLine[0])
                if beta<=alpha:
                    break
            return minbestLine

