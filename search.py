class Search():
    nodes=0

    def reveals_Kingattack(self,board,move):
        offset =0
        fromSquare = (move >> 11) & 127
        #white
        if board.sideToMove==board.White:
            kingsquare=board.whiteKingsq
        else:
            kingsquare = board.blackKingsq

        if abs(fromSquare-kingsquare)%9==0:
            offset =9
        elif abs(fromSquare - kingsquare) % 11 == 0:
            offset = 11
        elif abs(fromSquare - kingsquare) % 10== 0:
            offset = 10
        elif abs(fromSquare - kingsquare) % 1 == 0:
            offset=1
        if offset==0:
            return False
        if offset==11 or offset == 9:
            if fromSquare-kingsquare<0:
                checksqaure=kingsquare
                while board.board[checksqaure]!= board.OffBoard:
                    checksqaure-=offset
                    if checksqaure==fromSquare:
                        pass
                    elif board.sideToMove==board.White:
                        if board.board[checksqaure]==board.BlackBishop or board.board[checksqaure]==board.BlackQueen:
                            return True
                        elif board.board[checksqaure] in board.whitePieces or board.board[checksqaure] in board.blackPieces:
                            return False
                    elif board.sideToMove==board.Black:
                        if board.board[checksqaure]==board.WhiteBishop or board.board[checksqaure]==board.WhiteQueen:
                            return True
                        elif board.board[checksqaure] in board.whitePieces or board.board[checksqaure] in board.blackPieces:
                            return False
            else:
                checksqaure=kingsquare
                while board.board[checksqaure]!= board.OffBoard:
                    checksqaure+=offset
                    if checksqaure==fromSquare:
                        pass
                    elif board.sideToMove==board.White:
                        if board.board[checksqaure]==board.BlackBishop or board.board[checksqaure]==board.BlackQueen:
                            return True
                        elif board.board[checksqaure] in board.whitePieces or board.board[checksqaure] in board.blackPieces:
                            return False
                    elif board.sideToMove==board.Black:
                        if board.board[checksqaure]==board.WhiteBishop or board.board[checksqaure]==board.WhiteQueen:
                            return True
                        elif board.board[checksqaure] in board.whitePieces or board.board[checksqaure] in board.blackPieces:
                            return False


        if offset == 10 or offset==1:
            #fill in code
            pass
    #fill black



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

    def moves_toString(self, movelist):
        movenumber=1
        line=''
        piecemap={1:'',2:'N',3:'B',4:'N',5:'Q',6:'K',
                  7:'',8:'N',9:'B',10:'R',11:'Q',12:'K'}
        legalsquaresmap =  {21:'a8', 22:'b8', 23:'c8', 24:'d8', 25:'e8', 26:'f8', 27:'g8', 28:'h8',
                            31:'a7', 32:'b7', 33:'c7', 34:'d7', 35:'e7', 36:'f7', 37:'g7', 38:'h7',
                            41:'a6', 42:'b6', 43:'c6', 44:'d6', 45:'e6', 46:'f6', 47:'g6', 48:'h6',
                            51:'a5', 52:'b5', 53:'c5', 54:'d5', 55:'e5', 56:'f5', 57:'g5', 58:'h5',
                            61:'a4', 62:'b4', 63:'c4', 64:'d4', 65:'e4', 66:'f4', 67:'g4', 68:'h4',
                            71:'a3', 72:'b3', 73:'c3', 74:'d3', 75:'e3', 76:'f3', 77:'g3', 78:'h3',
                            81:'a2', 82:'b2', 83:'c2', 84:'d2', 85:'e2', 86:'f2', 87:'g2', 88:'h2',
                            91:'a1', 92:'b1', 93:'c1', 94:'d1', 95:'e1', 96:'f1', 97:'g1', 98:'h1'}
        for move in movelist:
            capturedPiece=move&15
            toSquare=(move>>4)&127
            fromSquare=(move>>11)&127
            piece=(move>>18)&15
            line+=' '
            if movenumber==int(movenumber):
                line+=(str(int(movenumber))+'.')
            line+=piecemap[piece]
            if capturedPiece!=0:
                line+='x'
            line+=legalsquaresmap[toSquare]
            movenumber+=.5

        return line



