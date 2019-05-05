import ai

def tah_hrace(gameboard):
    while True:
        symbol_hrace = "x"
        tah_hrace_na_pozici = int(input("Zadej číslo mezi 0-19: "))
        if tah_hrace_na_pozici >= 0 and tah_hrace_na_pozici <= 19:
            if gameboard[tah_hrace_na_pozici] == "-":
                print("To je ono!")
                return gameboard[:tah_hrace_na_pozici] + symbol_hrace + gameboard[tah_hrace_na_pozici + 1:]
            else:
                print("Ale ne, tato pozice už je obsazená!")
        elif tah_hrace_na_pozici > 19:
            print("Ach ne, tvé číslo je moc veliké.")
        elif tah_hrace_na_pozici < 0:
            print("Nemůžeš zadat záporné číslo...")

def piskvorky1d(gameboard):
    round = 0
    while True:
        gameboard = tah_hrace(gameboard)
        gameboard = ai.tah_pocitace(gameboard)
        print(gameboard)
        round += 1
        print(round)

        result = vyhodnot(gameboard)

        if result != "-":
            if result == "x":
                print("Vyhrála jsem!")
            elif result == "o":
                print("Ach ne, prohrála jsem!")
            elif result == "!":
                print("Plichta!")
            break

def vyhodnot(gameboard):
    if "xxx" in gameboard:
        return "x"
    elif "ooo" in gameboard:
        return "o"
    elif "-" not in gameboard:
        return "!"
    else:
        return "-"
