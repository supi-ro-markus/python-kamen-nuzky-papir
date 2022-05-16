import random

znaky = ("kamen", "nuzky", "papir")
oddelovac=45*"-"
uvodna_sprava="Ahoj a vitaj v hre kamen, nuzky, papir, ktoru som vytvoril. Nech vyhra ten najlepsi!"


print (uvodna_sprava)
print(oddelovac)

pocet_kol= int(input("Zadaj pocet kol, ktore chces hrat:"))

cop1=0 #toto je pocet vyhier mna
cop2=0 #toto je pocet vyhier pocitaca
cop3=0 #toto je pocet remiz
cop=0 #celkovy pocet kol

print (oddelovac)

while cop<pocet_kol:
    user1 = input("Napis kamen, nuzky alebo papir a snaz sa vyhrat:") #ked si zadas random.choise tak nechas proti sebe ist PC
    print("Zadal si:"+user1)
    user2 = random.choice(znaky) #mozes zadat podobne ako user1 a hrat proti sebe :P
    print ("Pocitac zadal:"+ user2)
    if user1 not in znaky:
        print("Nezadal si spravny znak. Podvadzas!")
        break
    elif user1 == "kamen" and user2 == "papir":
        print("Vyhral hrac cislo 2. Gratulujeme!")
        cop2 = cop2 + 1
    elif user1 == "kamen" and user2 == "nuzky":
        print("Vyhral hrac cislo 1. Gratulujeme!")
        cop1 = cop1 + 1
    elif user1 == "nuzky" and user2 == "papir":
        print("Vyhral hrac cislo 1. Gratulujeme!")
        cop1 = cop1 + 1
    elif user1 == "nuzky" and user2 == "kamen":
        print("Vyhral hrac cislo 2. Gratulujeme!")
        cop2 = cop2 + 1
    elif user1 == "papir" and user2 == "kamen":
        print("Vyhral hrac cislo 1. Gratulujeme!")
        cop1 = cop1 + 1
    elif user1 == "papir" and user2 == "nuzky":
        print("Vyhral hrac cislo 2. Gratulujeme!")
        cop2 = cop2 + 1
    else:
        print("Je to remiza!")
        cop3=cop3+1
    cop = cop1 + cop2 + cop3
    print (oddelovac)
print("Dakujeme za hru!")

hrac=str(cop1) #prehodene na str / toto je pocet vyhier mna
PC= str(cop2) #prehodene na str / toto je pocet vyhier pocitaca
remiza=str(cop3) #prehodene na str / toto je pocet remiz

if cop1>cop2:
    print ("Gratulujeme! Vyhral si! Pocet tvojich vyhier je:"+hrac+", pocet remiz je:"+remiza+" a pocet prehier je:"+PC+".")
elif cop1==cop2:
    print ("Je to remiza. To nie je take zle! Pocet tvojich vyhier je:"+hrac+", pocet remiz je:"+remiza+" a pocet prehier je:"+PC+".")
else:
    print("Mrzi nas to, ale prehral si! Skus to nabuduce! Pocet tvojich vyhier je:"+hrac+", pocet remiz je:"+remiza+" a pocet prehier je:"+PC+".")

