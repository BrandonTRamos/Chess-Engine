
class Evaluate():

    legalsquares=[21, 22, 23, 24, 25, 26, 27, 28,
                  31, 32, 33, 34, 35, 36, 37, 38,
                  41, 42, 43, 44, 45, 46, 47, 48,
                  51, 52, 53, 54, 55, 56, 57, 58,
                  61, 62, 63, 64, 65, 66, 67, 68,
                  71, 72, 73, 74, 75, 76, 77, 78,
                  81, 82, 83, 84, 85, 86, 87, 88,
                  91, 92, 93, 94, 95, 96, 97, 98]


    whitepawns=[ 0,  0,  0,  0,  0,  0,  0,  0,
                 50, 50, 50, 50, 50, 50, 50, 50,
                 10, 10, 20, 30, 30, 20, 10, 10,
                 5,  5, 10, 25, 25, 10,  5,  5,
                 0,  0,  0, 20, 20,  0,  0,  0,
                 5, -5,-10,  0,  0,-10, -5,  5,
                 5, 10, 10,-20,-20, 10, 10,  5,
                 0,  0,  0,  0,  0,  0,  0,  0]

    blackpawns=[0, 0, 0, 0, 0, 0, 0, 0,
                 5, 10, 10, -20, -20, 10, 10, 5,
                 5, -5, -10, 0, 0, -10, -5, 5,
                 0, 0, 0, 20, 20, 0, 0, 0,
                 5, 5, 10, 25, 25, 10, 5, 5,
                 10, 10, 20, 30, 30, 20, 10, 10,
                 50, 50, 50, 50, 50, 50, 50, 50,
                 0, 0, 0, 0, 0, 0, 0,0]

    whiteknights=[-50,-40,-30,-30,-30,-30,-40,-50,
                -40,-20,  0,  0,  0,  0,-20,-40,
                -30,  0, 10, 15, 15, 10,  0,-30,
                -30,  5, 15, 20, 20, 15,  5,-30,
                -30,  0, 15, 20, 20, 15,  0,-30,
                -30,  5, 10, 15, 15, 10,  5,-30,
                -40,-20,  0,  5,  5,  0,-20,-40,
                -50,-40,-30,-30,-30,-30,-40,-50,]

    blackknights=[-50,-40,-30,-30,-30,-30,-40,-50,
                -40,-20,  0,  0,  0,  0,-20,-40,
                -30,  0, 10, 15, 15, 10,  0,-30,
                -30,  5, 15, 20, 20, 15,  5,-30,
                -30,  0, 15, 20, 20, 15,  0,-30,
                -30,  5, 10, 15, 15, 10,  5,-30,
                -40,-20,  0,  5,  5,  0,-20,-40,
                -50,-40,-30,-30,-30,-30,-40,-50,]

    whitebishops=[-20,-10,-10,-10,-10,-10,-10,-20,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -10,  0,  5, 10, 10,  5,  0,-10,
                -10,  5,  5, 10, 10,  5,  5,-10,
                -10,  0, 10, 10, 10, 10,  0,-10,
                -10, 10, 10, 10, 10, 10, 10,-10,
                -10,  5,  0,  0,  0,  0,  5,-10,
                -20,-10,-10,-10,-10,-10,-10,-20,]

    blackbishops=[-20, -10, -10, -10, -10, -10, -10, -20,
                   -10, 5, 0, 0, 0, 0, 5, -10,
                   -10, 10, 10, 10, 10, 10, 10, -10,
                   -10, 0, 10, 10, 10, 10, 0, -10,
                   -10, 5, 5, 10, 10, 5, 5, -10,
                   -10, 0, 5, 10, 10, 5, 0, -10,
                   -10, 0, 0, 0, 0, 0, 0, -10,
                   -20, -10, -10, -10, -10, -10, -10,-20]

    whiterooks=[  0,  0,  0,  0,  0,  0,  0,  0,
                  5, 10, 10, 10, 10, 10, 10,  5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                  0,  0,  0,  5,  5,  0,  0,  0]

    blackrooks=[0, 0, 0, 5, 5, 0, 0, 0,
                -5, 0, 0, 0, 0, 0, 0, -5,
                -5, 0, 0, 0, 0, 0, 0, -5,
                -5, 0, 0, 0, 0, 0, 0, -5,
                -5, 0, 0, 0, 0, 0, 0, -5,
                -5, 0, 0, 0, 0, 0, 0, -5,
                 5, 10, 10, 10, 10, 10, 10,5,
                0, 0, 0, 0, 0, 0, 0,0]

    whitequeen=[-20,-10,-10, -5, -5,-10,-10,-20,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -10,  0,  5,  5,  5,  5,  0,-10,
                 -5,  0,  5,  5,  5,  5,  0, -5,
                  0,  0,  5,  5,  5,  5,  0, -5,
                -10,  5,  5,  5,  5,  5,  0,-10,
                -10,  0,  5,  0,  0,  0,  0,-10,
                -20,-10,-10, -5, -5,-10,-10,-20]

    blackqueen=[-20, -10, -10, -5, -5, -10, -10, -20,
                -10, 0, 0, 0, 0, 5, 0, -10,
                -10,0, 5, 5, 5, 5, 5, -10,
                -5, 0, 5, 5, 5, 5, 0, 0,
                -5, 0, 5, 5, 5, 5, 0, -5,
                -10, 0, 5, 5, 5, 5, 0, -10,
                -10, 0, 0, 0, 0, 0, 0, -10,
                -20, -10, -10, -5, -5, -10, -10,-20]

    whiteking_middlegame=[-30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -30,-40,-40,-50,-50,-40,-40,-30,
                        -20,-30,-30,-40,-40,-30,-30,-20,
                        -10,-20,-20,-20,-20,-20,-20,-10,
                         20, 20,  0,  0,  0,  0, 20, 20,
                         20, 30, 10,  0,  0, 10, 30, 20]

    blackking_middlegame=[20, 30, 10, 0, 0, 10, 30, 20,
                          20, 20, 0, 0, 0, 0, 20, 20,
                          -10, -20, -20, -20, -20, -20, -20, -10,
                          -20, -30, -30, -40, -40, -30, -30, -20,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30]

    whiteking_endgame=[-50,-40,-30,-20,-20,-30,-40,-50,
                        -30,-20,-10,  0,  0,-10,-20,-30,
                        -30,-10, 20, 30, 30, 20,-10,-30,
                        -30,-10, 30, 40, 40, 30,-10,-30,
                        -30,-10, 30, 40, 40, 30,-10,-30,
                        -30,-10, 20, 30, 30, 20,-10,-30,
                        -30,-30,  0,  0,  0,  0,-30,-30,
                        -50,-30,-30,-30,-30,-30,-30,-50]

    blackking_endgame=[-50, -30, -30, -30, -30, -30, -30, -50,
                       -30, -30, 0, 0, 0, 0, -30, -30,
                       -30, -10, 20, 30, 30, 20, -10, -30,
                       -30, -10, 30, 40, 40, 30, -10, -30,
                       -30, -10, 30, 40, 40, 30, -10, -30,
                       -30, -10, 20, 30, 30, 20, -10, -30,
                       -30, -20, -10, 0, 0, -10, -20, -30,
                       -50, -40, -30, -20, -20, -30, -40, -50]

    def __init__(self):
        self.onetwentyto64map=self.init_map()

    def init_map(self):
        onetwentyto64map={}
        i=0
        for square in self.legalsquares:
            onetwentyto64map[square]=i
            i+=1
        return onetwentyto64map

    def evaluate_node(self,board):
        whitePieces=[]
        blackPieces=[]

        blackPawns=[]
        blackKnights=[]
        blackBishops=[]
        blackRooks=[]
        blackQueen=[]
        blackKing=[]

        whitePawns=[]
        whiteKnights=[]
        whiteBishops=[]
        whiteRooks=[]
        whiteQueen=[]
        whiteKing=[]

        allpieces=[]

        whitescore=0
        blackscore=0
        for square in self.legalsquares:
            if board[square]==1:
                blackscore+=100
                blackscore+=self.blackpawns[self.onetwentyto64map[square]]
                blackPieces.append(square)
                blackPawns.append(square)
            elif board[square]==2:
                blackscore+=300
                blackscore += self.blackknights[self.onetwentyto64map[square]]
                blackKnights.append(square)
                blackPieces.append(square)
            elif board[square]==3:
                blackscore+=310
                blackscore += self.blackbishops[self.onetwentyto64map[square]]
                blackBishops.append(square)
                blackPieces.append(square)
            elif board[square]==4:
                blackscore+=500
                blackscore += self.blackrooks[self.onetwentyto64map[square]]
                blackRooks.append(square)
                blackPieces.append(square)
            elif board[square]==5:
                blackscore+=900
                blackscore += self.blackqueen[self.onetwentyto64map[square]]
                blackQueen.append(square)
                blackPieces.append(square)
            elif board[square]==6:
                blackKing.append(square)
                blackPieces.append(square)
            elif board[square]==7:
                whitescore+=100
                whitescore += self.whitepawns[self.onetwentyto64map[square]]
                whitePawns.append(square)
                whitePieces.append(square)
            elif board[square]==8:
                whitescore+=300
                whitescore += self.whiteknights[self.onetwentyto64map[square]]
                whiteKnights.append(square)
                whitePieces.append(square)
            elif board[square]==9:
                whitescore+=310
                whitescore += self.whitebishops[self.onetwentyto64map[square]]
                whiteBishops.append(square)
                whitePieces.append(square)
            elif board[square]==10:
                whitescore+=500
                whitescore += self.whiterooks[self.onetwentyto64map[square]]
                whiteRooks.append(square)
                whitePieces.append(square)
            elif board[square]==11:
                whitescore+=900
                whitescore += self.whitequeen[self.onetwentyto64map[square]]
                whiteQueen.append(square)
                whitePieces.append(square)

            elif board[square]==12:
                whiteKing.append(square)
                whitePieces.append(square)
            totalscore=whitescore-blackscore
        return totalscore/100