#GUL0021, Gulcik Tomas
# 9.Třída Soucet (bude sčítat cifry v zadaném čísle.
# např. zadá se číslo 5895 a proběhne následující výpočet 5+8+9+5 = 27 > 2+7 = 9 – tzn., až se dojde k jednocifernému číslu
# Metoda secti s parametrem číslo

def rozdelenie_cisla():
    print("Zadajte cislo:")
    cislo = input()
    zoznam_cislo = list(cislo)  # rozdelenie zadaneho cisla na zoznam

    sucet = 0  # vytvaram premmenu do ktorej sa uklada sucet, zaciname s 0
    for i in range(len(zoznam_cislo)):  # zistime pocet cisel ktore sa nachadzaju v zozname
        sucet += int(zoznam_cislo[i])  # scitavame jednotlive cisla v zozname napr. 0+5 potom 5+8, 8+9, 9+5
        #print(f'sucet 1: {sucet}')
    if len(str(sucet)) > 1:  # pokial je vysledok suctu viac ako jednociferne cislo tak musime opakovat predosly krok
        zoznam_sucet = list(str(sucet))  # rozdelenie vysledku na zoznam
        #print(f'zoznam_sucet: {zoznam_sucet}')
        sucet = 0
        for i in range(len(zoznam_sucet)):  # cyklus zisti dlzku zoznamu
            sucet += int(zoznam_sucet[i])  # scita jednotlive cleny zoznamu
            #print(f'sucet 2: {sucet}')
        if len(str(sucet)) > 1:  # znova, pokial je vysledok viac ako jednociferne cislo
            zoznam_sucet = list(str(sucet))  # rozdeli cislo na zoznam
            sucet = 0
            for i in range(len(zoznam_sucet)):  # cyklus zisti dlzku zoznamu
                sucet += int(zoznam_sucet[i])   # postupne scita jednotlive cleny zoznamu
    print(sucet)
rozdelenie_cisla() #volame funkciu rozdelenie cisla





