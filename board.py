class Board():
    BlackPawn=1
    BlackKnight=2
    BlackBishop=3
    BlackRook=4
    BlackQueen=5
    BlackKing=6
    WhitePawn=7
    WhiteKnight=8
    WhiteBishop=9
    WhiteRook=10
    WhiteQueen=11
    WhiteKing=12
    FirstRank=[91,92,93,94,95,96,97,98]
    SecondRank=[81,82,83,84,85,86,87,88]
    ThirdRank=[71,72,73,74,75,76,77,78]
    FourthRank=[61,62,63,64,65,66,67,68]
    FifthRank=[51,52,53,54,55,56,57,58]
    SixthRank=[41,42,43,44,45,46,47,48]
    SeventhRank=[31,32,33,34,35,36,37,38]
    EigthRank=[21,22,23,24,25,26,27,28]
    Afile=[21,31,41,51,61,71,81,91]
    Bfile=[22,32,42,52,62,72,82,92]
    Cfile=[23,33,43,53,63,73,83,93]
    Dfile=[24,34,44,54,64,74,84,94]
    Efile=[25,35,45,55,65,75,85,95]
    Ffile=[26,36,46,56,66,76,86,96]
    Gfile=[27,37,47,57,67,77,87,97]
    Hfile=[28,38,48,58,68,78,88,98]

    castleOptions=0
    enpassantSquare=''
    FiftyMove_Counter=0


    def __init__(self,FEN):
        self.FEN=FEN
        self.board=self.parseFEN()

    def initalizeBoard(self):
        emptyranks=[self.ThirdRank,self.FourthRank,self.FifthRank,self.SixthRank]
        board=[99 for i in range(120)]
        for rank in emptyranks:
            for square in rank:
                board[square]=0
        for square in self.SeventhRank:
            board[square]=self.BlackPawn
        for square in self.SecondRank:
            board[square]=self.WhitePawn
        board[21]=self.BlackRook
        board[28]=self.BlackRook
        board[22]=self.BlackKnight
        board[27]=self.BlackKnight
        board[23]=self.BlackBishop
        board[26]=self.BlackBishop
        board[24]=self.BlackQueen
        board[25]=self.BlackKing
        board[91]=self.WhiteRook
        board[98]=self.WhiteRook
        board[92]=self.WhiteKnight
        board[97]=self.WhiteKnight
        board[93]=self.WhiteBishop
        board[96]=self.WhiteBishop
        board[94]=self.WhiteQueen
        board[95]=self.WhiteKing
        return board
    def printBoard(self):

        for i in range(21,101,10):
            line=[]
            for j in range(8):
               line.append(str(self.board[i+j]).rjust(2))
            print(' '.join(line))

    def parseFEN(self):
        castlecount=0
        self.castleOptions = 0b0000
        board=[99 for i in range(120)]
        ranks=[self.EigthRank,self.SeventhRank,self.SixthRank,self.FifthRank,self.FourthRank,
               self.ThirdRank,self.SecondRank,self.FirstRank]
        fenMap={'p':self.BlackPawn,'n':self.BlackKnight,'b':self.BlackBishop,'r':self.BlackRook,'q':self.BlackQueen,'k':self.BlackKing,
                'P':self.WhitePawn,'N':self.WhiteKnight,'B':self.WhiteBishop,'R':self.WhiteRook,'Q':self.WhiteQueen,'K':self.WhiteKing}

        FEN=self.FEN
        for rank in range(len(ranks)):
           square=0
           while square<9:
                if FEN [0]=='/' or FEN[0] ==' ':
                    FEN=FEN[1:]
                    break
                elif FEN[0] in fenMap:
                    board[ranks[rank][square]]=fenMap[FEN[0]]
                    FEN=FEN[1:]
                    square+=1
                else:
                    blankcount=int(FEN[0])
                    for blank in range(blankcount):
                        board[ranks[rank][square+blank]]=0
                    FEN=FEN[1:]
                    square+=blankcount
        if FEN[0]=='w':
            self.sideToMove=0
        else:
            self.sideToMove=1
        FEN=FEN[2:]
        print(FEN)
        if 'K'in FEN[:4]:
            self.castleOptions=0b0001
            castlecount+=1
        if 'Q' in FEN[:4]:
            self.castleOptions=self.castleOptions | 0b0010
            castlecount+=1
        if 'k' in FEN[:4]:
            self.castleOptions=self.castleOptions|0b0100
            castlecount+=1
        if 'q' in FEN[:4]:
            self.castleOptions=self.castleOptions|0b1000
            castlecount+=1
        print('Castle Options:',bin(self.castleOptions))
        print('Castle Count:',castlecount)
        FEN=FEN[castlecount+1:]
        if FEN[0]!='-':
            self.enpassantSquare=FEN[:2]
            FEN=FEN[3:]
        else:
           FEN=FEN[2:]
        print('EP:',self.enpassantSquare)
        print(FEN)

        return board






