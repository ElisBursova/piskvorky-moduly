import piskvorky

def test_vyhodnot():
    assert piskvorky.vyhodnot("xxx") == "x"
    assert piskvorky.vyhodnot("--------------") == "-"
    assert piskvorky.vyhodnot("ooo") == "o"
    assert piskvorky.vyhodnot("----x--o---x--oo----") == "-"
