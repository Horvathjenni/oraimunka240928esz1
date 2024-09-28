# import random -generált
import random


def tizenegyedikFeladat():
    szam1 = random.randint(50,  150)
    szam2 = random.randint(50,  150)

    print("szam1="+str(szam1) + ", szam2=" + str(szam2))

    atmeneti =szam1
    szam1 = szam2
    szam2 = atmeneti

    """
    atmeneti = szam2
    szam2 = szam1
    szam1= atmeneti
    """
    print("szam1=" + str(szam1) +", szam2=" +str(szam2))



