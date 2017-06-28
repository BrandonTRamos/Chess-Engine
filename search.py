class Search():
    nodes=0

    def is_pinned(self,board,square):
        offset =0
        if board.sideToMove==board.White:
            kingsquare=board.whiteKingsq[0]
        else:
            kingsquare = board.blackKingsq[0]
        if abs(square-kingsquare)%9==0:
            offset =9
        elif abs(square-kingsquare) % 11 == 0:
            offset = 11
        elif abs(square-kingsquare) % 10== 0:
            offset = 10
        elif int(kingsquare/10)==int(square/10):
            offset=1
        if offset==0:
            return False
        checksquare=square
        while checksquare!=kingsquare:
            if square - kingsquare < 0:
                checksquare+=offset
            else:
                checksquare-=offset
            if checksquare in board.blackKingsq or checksquare in board.whiteKingsq:
                continue
            elif checksquare in board.whitepiecesq or checksquare in board.blackpiecesq:
                return False
        checksquare=square
        while board.board[checksquare]!=board.OffBoard:
            if square - kingsquare < 0:
                checksquare-=offset
            else:
                checksquare+=offset
            if board.sideToMove==board.White:
                if offset == 11 or offset == 9:
                    if checksquare in board.blackQueensq or checksquare in board.blackBishopsq:
                        return True
                elif offset!=0:
                    if checksquare in board.blackQueensq or checksquare in board.blackRooksq:
                        return True
                if checksquare in board.blackpiecesq or checksquare in board.whitepiecesq:
                    return False
                if board.board[checksquare] != board.OffBoard:
                    return False
            elif board.sideToMove==board.Black:
                if offset == 11 or offset == 9:
                    if checksquare in board.whiteQueensq or checksquare in board.whiteBishopsq:
                        return True
                elif offset!=0:
                    if checksquare in board.whiteQueensq or checksquare in board.whiteRooksq:
                        return True
                if checksquare in board.blackpiecesq or checksquare in board.whitepiecesq:
                    return False
                if board.board[checksquare] != board.OffBoard:
                    return False

    def generatePawnmoves(self,board):
        moves=[]
        if board.sideToMove==board.White:
            for square in board.whitePawnsq:
                if self.is_pinned(board,square):

                    pass
                else:
                    singleSqauremove=square-10
                    doubleSquaremove=square-20
                    capturedPiece=0
                    pawnAttacksquares=[square-11,square-9]
                    for attacksquare in pawnAttacksquares:
                        move = 7
                        if board.board[attacksquare]!=board.OffBoard and board.board[attacksquare]!=board.BlackKing and (attacksquare) not in board.whitepiecesq:
                            if (attacksquare) in board.blackpiecesq: #or attacksquare==board.enpassantSquare:
                                capturedPiece = board.board[attacksquare]
                                move = (move << 7) | square
                                move = (move << 7) | attacksquare
                                move = (move << 4) | capturedPiece
                                self.moves.append(move)
                    if board.board[singleSqauremove]==0:
                        capturedPiece = 0
                        move = 7
                        move = (move << 7) | square
                        move = (move << 7) | singleSqauremove
                        move = (move << 4) | capturedPiece
                        self.moves.append(move)
                        if square in board.SecondRank:
                            if board.board[doubleSquaremove] == 0:
                                move = 7
                                move = (move << 7) | square
                                move = (move << 7) | doubleSquaremove
                                move = (move << 4) | capturedPiece
                                self.moves.append(move)


        else:
            for square in board.blackPawnsq:
                if self.is_pinned(board,square):
                    pass
                else:
                    singleSqauremove = square + 10
                    doubleSquaremove = square + 20
                    capturedPiece = 0
                    pawnAttacksquares = [square + 11, square + 9]
                    for attacksquare in pawnAttacksquares:
                        move = 1
                        if board.board[attacksquare] != board.OffBoard and board.board[attacksquare] != board.WhiteKing and (attacksquare) not in board.blackpiecesq:
                            if (attacksquare) in board.whitepiecesq: #or attacksquare == board.enpassantSquare:
                                capturedPiece = board.board[attacksquare]
                                move = (move << 7) | square
                                move = (move << 7) | attacksquare
                                move = (move << 4) | capturedPiece
                                self.moves.append(move)
                    if board.board[singleSqauremove] == 0:
                        move = 1
                        capturedPiece = 0
                        move = (move << 7) | square
                        move = (move << 7) | singleSqauremove
                        move = (move << 4) | capturedPiece
                        self.moves.append(move)
                        if square in board.SeventhRank:
                            if board.board[doubleSquaremove] == 0:
                                move = 1
                                move = (move << 7) | square
                                move = (move << 7) | doubleSquaremove
                                move = (move << 4) | capturedPiece
                                self.moves.append(move)



    def generateKnightmoves(self,board):
        knightoffsets=[-8,-12,-19,-21,8,12,19,21]
        moves=[]
        if board.sideToMove==board.White:
            for square in board.whiteKnightsq:
                if self.is_pinned(board,square):
                    pass
                else:
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
                            self.moves.append(move)

        else:
            knightoffsets = [8, 12, 19, 21, -8, -12, -19, -21]
            for square in board.blackKnightsq:
                if self.is_pinned(board,square):
                    pass
                else:
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
                            self.moves.append(move)

    def generateMoves(self,board):
        self.moves=[]
        self.generatePawnmoves(board)
        self.generateKnightmoves(board)

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
        # print('____________________________________________________')
        # print('\nside to move',board.sideToMove)
        if depth==0:
            moves=movelist[:]
            # print('Max depth reached, evaluation:',evaluate.evaluate_node(board))
            # print('Result:',(evaluate.evaluate_node(board),moves))
            # print('________________________________________________')
            self.nodes+=1
            return (evaluate.evaluate_node(board),moves)

        elif side==board.White:
            maxbestLine=(-1000,[])
            self.generateMoves(board)
            for move in self.moves:
                movelist.append(move)
                # print('whitemoves @ depth',depth,':',whitemoves)
                # print('white making @ depth:',depth,'Move:',move)
                board.makeMove(move)
                # board.printBoard()
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
            self.generateMoves(board)
            for move in self.moves:
                movelist.append(move)
                # print('blackmoves:',blackmoves)
                # print('black making @ depth:', depth,'Move:',move)
                board.makeMove(move)
                # board.printBoard()
                line=self.mini_max(board,evaluate,board.White,depth-1,movelist,alpha,beta)
                # print('black unmaking @ depth:', depth,'Move:',move)
                minbestLine = self.get_min(line,minbestLine)
                board.unmakeMove(move)
                movelist.pop()
                beta=min(beta,minbestLine[0])
                if beta<=alpha:
                    break
            return minbestLine




