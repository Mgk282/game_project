print("new game? Y/N: ")
start_game = input()
if start_game == "Y" or "y":
    print("tvoi geroi nachinaet pyteshestvie v mir boli & stradanii")
    gg.name = input("vvedi imya personaza: ")
    print(f"priyatno poznakomitsya {gg.name}. ya tvoi lichnii provodnik v dannom mire")
    answer_char = input(f"davai ya kranko tebya oznakomly s tvoimi haracteristikami? Y/N: ")
    if answer_char == "Y" or "y":
        print(f"tvoi lvl {gg.level}, pydet rasti po dostizheniy exp, chtobi nabit exb nado srazatsya")
        print(f"tvoe zdorove {gg.health}, ono bydet menyatsya po povisheniu lvl, a tak ze pri polychenii yrona")
        print(f"")
        print(f"")
        print(f"")
        print(f"")
        print(f"")



else:
    print("Sorry, your game not start, return ")




input()