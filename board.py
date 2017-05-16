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
    a1,b1,c1,d1,e1,f2,g1,h1=91,92,93,94,95,96,97,98
    a2,b2,c2,d2,e2,f2,g2,h2=81,82,83,84,85,86,87,88
    a3,b3,c3,d3,e3,f3,g3,h3=71,72,73,74,75,76,77,78
    a4,b4,c4,d4,e4,f4,g4,h4=61,62,63,64,65,66,67,68
    a5,b5,c5,d5,e5,f5,g5,h5=51,52,53,54,55,56,57,58
    a6,b6,c6,d6,e6,f6,g6,h6=41,42,43,44,45,46,47,48
    a7,b7,c7,d7,e7,f7,g7,h7=31,32,33,34,35,36,37,38
    a8,b8,c8,d8,e8,f8,g8,h8=21,22,23,24,25,26,27,28


    castleOptions=0
    enpassantSquare=''
    FiftyMove_Counter=0


    def __init__(self,FEN):
        self.FEN=FEN
        self.board=self.parseFEN()


    def printBoard(self):

        for i in range(21,101,10):
            line=[]
            for j in range(8):
               line.append(str(self.board[i+j]).rjust(2))
            print(' '.join(line))
        print('\nSide to move:',self.sideToMove)
        print('Castle Options: ',bin(self.castleOptions))
        print('enpassant square:', self.enpassantSquare)
        print('Fifty-Move Counter:', self.FiftyMove_Counter)

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
        print('FEN:',FEN)
        if FEN[0]=='w':
            self.sideToMove=0
        else:
            self.sideToMove=1
        FEN=FEN[2:]
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
        FEN=FEN[castlecount+1:]
        if FEN[0]!='-':
            self.enpassantSquare=FEN[:2]
            FEN=FEN[3:]
        else:
           FEN=FEN[2:]
        print("FEN:",FEN)
        movecount=''
        while FEN[0]!=' ':
            movecount+=FEN[0]
            FEN=FEN[1:]
        FEN=FEN[1:]
        self.FiftyMove_Counter=int(movecount)
        return board






