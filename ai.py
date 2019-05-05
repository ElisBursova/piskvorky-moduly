from random import randrange

def tah_pocitace(gameboard):
    while True:
        symbol_pocitace = "o"
        pozice = randrange(0,20)
        if gameboard[pozice] == "-":
            return gameboard[:pozice] + symbol_pocitace + gameboard[pozice + 1:]
            print("To je ono!")
        else:
            print("Ale ne, tato pozice už je obsazená!")
