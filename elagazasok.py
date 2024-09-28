def elso():
    print("A program eldőnti egy egész számról, hogy pozitív-e")
    szam = int(input("kérem adjon meg egy egész számot"))

    if szam > 0:
        print("A szám pozitív.")


def masodik():
    szam = int(input("kérem adjon meg egy egész számot"))

    if (szam >=-9) and (szam <=9):
        megelozo = szam -1
        rakovetkezo = szam +1
        print(" A rákövetkező érték:"+str(rakovetkezo)+", a megelöző érték:"+str(megelozo))