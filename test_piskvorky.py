def vyhodnot(gameboard):
    if "xxx" in gameboard:
        return "x"
    elif "ooo" in gameboard:
        return "o"
    elif "-" not in gameboard:
        return "!"
    else:
        return "-"

def test_vyhodnot(gameboard, pozice):
    assert vyhodnot("xxx") == "x"
