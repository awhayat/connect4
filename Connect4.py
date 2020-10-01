from turtle import *

#INTRO
print("Welcome to Connect 4!")
print("To win the game, you must have 4 of your pieces in a row on the board.\nThey can be placed vertically, horizontally, or diagonally.\nType 1, 2, 3, or 4 to choose the column in which to drop your piece.")

#DEFINITIONS
A = "~"
B = "~"
C = "~"
D = "~"
E = "~"
F = "~"
G = "~"
H = "~"
I = "~"
J = "~"
K = "~"
L = "~"
M = "~"
N = "~"
O = "~"
P = "~"
row1 = "|" + A + "|" + B + "|" + C + "|" + D + "|"
row2 = "|" + E + "|" + F + "|" + G + "|" + H + "|"
row3 = "|" + I + "|" + J + "|" + K + "|" + L + "|"
row4 = "|" + M + "|" + N + "|" + O + "|" + P + "|"

def DrawX(x, y):
    speed(6)
    penup()
    setpos(x, y)

    pencolor('blue')
    pendown()
    width(20)
    setpos((x + 165), (y - 100))

    penup()
    setpos((x + 165), y)

    pendown()
    setpos(x, (y - 100))

def DrawO(x, y):
    speed(10)
    penup()
    setpos((x + 82.5), y)

    pencolor('lightgreen')
    pendown()
    circle(50)
    
def CheckBoard():
    global A
    global B
    global C
    global D
    global E
    global F
    global G
    global H
    global I
    global J
    global K
    global L
    global M
    global N
    global O
    global P

    if (M == "X") and (N == "X") and (O == "X") and (P == "X"):
        return("X wins!")
    elif (I == "X") and (J == "X") and (K == "X") and (L == "X"):
        return("X wins!")
    elif (E == "X") and (F == "X") and (G == "X") and (H == "X"):
        return("X wins!")
    elif (A == "X") and (B == "X") and (C == "X") and (D == "X"):
        return("X wins!")
    elif (A == "X") and (E == "X") and (I == "X") and (M == "X"):
        return("X wins!")
    elif (B == "X") and (F == "X") and (J == "X") and (N == "X"):
        return("X wins!")
    elif (C == "X") and (G == "X") and (K == "X") and (O == "X"):
        return("X wins!")
    elif (D == "X") and (H == "X") and (L == "X") and (P == "X"):
        return("X wins!")
    elif (A == "X") and (F == "X") and (K == "X") and (P == "X"):
        return("X wins!")
    elif (D == "X") and (G == "X") and (J == "X") and (M == "X"):
        return("X wins!")
    elif (M == "O") and (N == "O") and (O == "O") and (P == "O"):
        return("O wins!")
    elif (I == "O") and (J == "O") and (K == "O") and (L == "O"):
        return("O wins!")
    elif (E == "O") and (F == "O") and (G == "O") and (H == "O"):
        return("O wins!")
    elif (A == "O") and (B == "O") and (C == "O") and (D == "O"):
        return("O wins!")
    elif (A == "O") and (E == "O") and (I == "O") and (M == "O"):
        return("O wins!")
    elif (B == "O") and (F == "O") and (J == "O") and (N == "O"):
        return("O wins!")
    elif (C == "O") and (G == "O") and (K == "O") and (O == "O"):
        return("O wins!")
    elif (D == "O") and (H == "O") and (L == "O") and (P == "O"):
        return("O wins!")
    elif (A == "O") and (F == "O") and (K == "O") and (P == "O"):
        return("O wins!")
    elif (D == "O") and (G == "O") and (J == "O") and (M == "O"):
        return("O wins!")
    else:
        return("")

def X_move():
    global A
    global B
    global C
    global D
    global E
    global F
    global G
    global H
    global I
    global J
    global K
    global L
    global M
    global N
    global O
    global P

    if (((A == "X") or (A == "O")) and ((E == "X") or (E == "O")) and ((I == "X") or (I == "O")) and ((M == "X") or (M == "O"))):
        invalid1 = "1"
    else:
        invalid1 = "0"
    if (((B == "X") or (B == "O")) and ((F == "X") or (F == "O")) and ((J == "X") or (J == "O")) and ((N == "X") or (N == "O"))):
        invalid2 = "2"
    else:
        invalid2 = "0"
    if (((C == "X") or (C == "O")) and ((G == "X") or (G == "O")) and ((K == "X") or (K == "O")) and ((O == "X") or (O == "O"))):
        invalid3 = "3"
    else:
        invalid3 = "0"
    if (((D == "X") or (D == "O")) and ((H == "X") or (H == "O")) and ((L == "X") or (L == "O")) and ((P == "X") or (P == "O"))):
        invalid4 = "4"
    else:
        invalid4 = "0"
    
    move = input("Player X, make your move :")
    while (move != "1") and (move != "2") and (move != "3") and (move != "4"):
        move = input("Invalid move :")
    while (move == invalid1) or (move == invalid2) or (move == invalid3) or (move == invalid4):
        move = input("Invalid move :")
        
    if (move == "1"):
        if (M != "X") and (M != "O"):
            DrawX(-330, -30)
            M = "X"
        elif (I != "X") and (I != "O"):
            DrawX(-330, 70)
            I = "X"
        elif (E != "X") and (E != "O"):
            DrawX(-330, 170)
            E = "X"
        elif (A != "X") and (A != "O"):
            DrawX(-330, 270)
            A = "X"

    if (move == "2"):
        if (N != "X") and (N != "O"):
            DrawX(-165, -30)
            N = "X"
        elif (J != "X") and (J != "O"):
            DrawX(-165, 70)
            J = "X"
        elif (F != "X") and (F != "O"):
            DrawX(-165, 170)
            F = "X"
        elif (B != "X") and (B != "O"):
            DrawX(-165, 270)
            B = "X"

    if (move == "3"):
        if (O != "X") and (O != "O"):
            DrawX(0, -30)
            O = "X"
        elif (K != "X") and (K != "O"):
            DrawX(0, 70)
            K = "X"
        elif (G != "X") and (G != "O"):
            DrawX(0, 170)
            G = "X"
        elif (C != "X") and (C != "O"):
            DrawX(0, 270)
            C = "X"

    if (move == "4"):
        if (P != "X") and (P != "O"):
            DrawX(165, -30)
            P = "X"
        elif (L != "X") and (L != "O"):
            DrawX(165, 70)
            L = "X"
        elif (H != "X") and (H != "O"):
            DrawX(165, 170)
            H = "X"
        elif (D != "X") and (D != "O"):
            DrawX(165, 270)
            D = "X"

    row1 = "|" + A + "|" + B + "|" + C + "|" + D + "|"
    row2 = "|" + E + "|" + F + "|" + G + "|" + H + "|"
    row3 = "|" + I + "|" + J + "|" + K + "|" + L + "|"
    row4 = "|" + M + "|" + N + "|" + O + "|" + P + "|"
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(CheckBoard())

def O_move():
    global A
    global B
    global C
    global D
    global E
    global F
    global G
    global H
    global I
    global J
    global K
    global L
    global M
    global N
    global O
    global P

    if (((A == "X") or (A == "O")) and ((E == "X") or (E == "O")) and ((I == "X") or (I == "O")) and ((M == "X") or (M == "O"))):
        invalid1 = "1"
    else:
        invalid1 = "0"
    if (((B == "X") or (B == "O")) and ((F == "X") or (F == "O")) and ((J == "X") or (J == "O")) and ((N == "X") or (N == "O"))):
        invalid2 = "2"
    else:
        invalid2 = "0"
    if (((C == "X") or (C == "O")) and ((G == "X") or (G == "O")) and ((K == "X") or (K == "O")) and ((O == "X") or (O == "O"))):
        invalid3 = "3"
    else:
        invalid3 = "0"
    if (((D == "X") or (D == "O")) and ((H == "X") or (H == "O")) and ((L == "X") or (L == "O")) and ((P == "X") or (P == "O"))):
        invalid4 = "4"
    else:
        invalid4 = "0"

    move = input("Player O, make your move :")
    while (move != "1") and (move != "2") and (move != "3") and (move != "4"):
        move = input("Invalid move :")
    while (move == invalid1) or (move == invalid2) or (move == invalid3) or (move == invalid4):
        move = input("Invalid move :")
    if (move == "1"):
        if (M != "X") and (M != "O"):
            DrawO(-330, -130)
            M = "O"
        elif (I != "X") and (I != "O"):
            DrawO(-330, -30)
            I = "O"
        elif (E != "X") and (E != "O"):
            DrawO(-330, 70)
            E = "O"
        elif (A != "X") and (A != "O"):
            DrawO(-330, 170)
            A = "O"

    if (move == "2"):
        if (N != "X") and (N != "O"):
            DrawO(-165, -130)
            N = "O"
        elif (J != "X") and (J != "O"):
            DrawO(-165, -30)
            J = "O"
        elif (F != "X") and (F != "O"):
            DrawO(-165, 70)
            F = "O"
        elif (B != "X") and (B != "O"):
            DrawO(-165, 170)
            B = "O"

    if (move == "3"):
        if (O != "X") and (O != "O"):
            DrawO(0, -130)
            O = "O"
        elif (K != "X") and (K != "O"):
            DrawO(0, -30)
            K = "O"
        elif (G != "X") and (G != "O"):
            DrawO(0, 70)
            G = "O"
        elif (C != "X") and (C != "O"):
            DrawO(0, 170)
            C = "O"

    if (move == "4"):
        if (P != "X") and (P != "O"):
            DrawO(165, -130)
            P = "O"
        elif (L != "X") and (L != "O"):
            DrawO(165, -30)
            L = "O"
        elif (H != "X") and (H != "O"):
            DrawO(165, 70)
            H = "O"
        elif (D != "X") and (D != "O"):
            DrawO(165, 170)
            D = "O"

    row1 = "|" + A + "|" + B + "|" + C + "|" + D + "|"
    row2 = "|" + E + "|" + F + "|" + G + "|" + H + "|"
    row3 = "|" + I + "|" + J + "|" + K + "|" + L + "|"
    row4 = "|" + M + "|" + N + "|" + O + "|" + P + "|"
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(CheckBoard())

#GAME
PLAY = "Y"

while (PLAY == "Y") or (PLAY == "y"):
    A = "~"
    B = "~"
    C = "~"
    D = "~"
    E = "~"
    F = "~"
    G = "~"
    H = "~"
    I = "~"
    J = "~"
    K = "~"
    L = "~"
    M = "~"
    N = "~"
    O = "~"
    P = "~"

    #drawboard
    clearscreen()
    speed(10)
    penup()
    setpos(-330, 270)

    pencolor('yellow')
    width(25)
    pendown()
    forward(660)

    right(90)
    forward(100)

    right(90)
    forward(660)

    right(90)
    forward(100)

    right(90)
    forward(165)

    right(90)
    forward(100)

    left(90)
    forward(165)

    left(90)
    forward(100)

    right(90)
    forward(165)

    right(90)
    forward(100)

    left(90)
    forward(165)

    right(90)
    forward(100)

    right(90)
    forward(660)

    right(90)
    forward(100)

    right(90)
    forward(165)

    right(90)
    forward(100)

    left(90)
    forward(165)

    left(90)
    forward(100)

    right(90)
    forward(165)

    right(90)
    forward(100)

    left(90)
    forward(165)

    right(90)
    forward(100)

    right(90)
    forward(660)

    right(90)
    forward(100)

    right(90)
    forward(165)

    right(90)
    forward(100)

    left(90)
    forward(165)

    left(90)
    forward(100)

    right(90)
    forward(165)

    right(90)
    forward(100)

    left(90)
    forward(165)

    right(90)
    forward(100)

    right(90)
    forward(660)

    right(90)
    forward(100)

    right(90)
    forward(165)

    right(90)
    forward(100)

    left(90)
    forward(165)

    left(90)
    forward(100)

    right(90)
    forward(165)

    right(90)
    forward(100)

    left(90)
    forward(165)
   
    while (CheckBoard() != "X wins!") and (CheckBoard() != "O wins!"):
        X_move()
        if (CheckBoard() == "X wins!"):
            break
        O_move()

    if(CheckBoard() == "X wins!"):
        #drawvictoryX
        clearscreen()
        speed(5)
        penup()
        setpos(-300, 270)
        pencolor('orange')
        pendown()
        width(50)
        right(45)
        forward(750)
        penup()
        setpos(300, 270)
        pencolor('orange')
        width(50)
        pendown()
        right(90)
        forward(750)
    elif(CheckBoard() == "O wins!"):
        #drawvictoryO
        clearscreen()
        speed(10)
        penup()
        sety(-270)
        pencolor('orange')
        pendown()
        width(50)
        circle(270)

    PLAY = input("Would you like to play another game? [Y] [N] :")

print("Thanks for playing, have a wonderful day!")