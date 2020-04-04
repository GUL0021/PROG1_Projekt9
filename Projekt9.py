#GUL0021, Gulcik Tomas
# 9.Třída Soucet (bude sčítat cifry v zadaném čísle.
# např. zadá se číslo 5895 a proběhne následující výpočet 5+8+9+5 = 27 > 2+7 = 9 – tzn., až se dojde k jednocifernému číslu
# Metoda secti s parametrem číslo
# Po zobrazeni vysledku, vypise numerologicky vyznam cisla.

# Zdroj významov čísel: https://www.numerologia.sk/clanky/vyznam-cisel-19.html
vyznamy_cisel = {                        # vytvoril som slovnik v ktorom su na lavej strane kluce, na pravej hodnoty
  "1": "začiatok, počatie, vývoj",      # v slovniku su zadefinovane vyznamy jednotlivych jednocifernych cisel
  "2": "rozmnoženie, pohyb nahor",
  "3": "viera, nádej a láska",
  "4": "nehoda, rozklad, smrť",
  "5": "symbol tvorivosti",
  "6": "splnené túžby, vyrovnanosť, spokojnosť, harmónia",
  "7": "svetlo, pokoj, šťastie, prináša oddych po práci, začiatok pre nové tvorivé činy, radosť v živote i hrách",
  "8": "dvojitý zápor, ktorý sa ruší a vytvára klad",
  "9": "tvorenie, splnenie plánov, dosiahnutie veľkých úspechov",
}


def rozdelenie_cisla():
    print("Zadajte číslo:")
    cislo = input().strip()
    zoznam_cislo = list(cislo)  # rozdelenie zadaneho cisla na zoznam

    sucet = 0  # vytvaram premmenu do ktorej sa uklada sucet, zaciname s 0
    scitavane_cislice = []
    for i in range(len(zoznam_cislo)):  # zistime pocet cisel ktore sa nachadzaju v zozname
        sucet += int(zoznam_cislo[i])  # scitavame jednotlive cisla v zozname napr. 0+5 potom 5+8, 8+9, 9+5
    if len(str(sucet)) > 1:  # pokial je vysledok suctu viac ako jednociferne cislo tak musime opakovat predosly krok
        zoznam_sucet = list(str(sucet))  # rozdelenie vysledku na zoznam
        # print(f'zoznam_sucet: {zoznam_sucet}')
        sucet = 0
        for i in range(len(zoznam_sucet)):  # cyklus zisti dlzku zoznamu
            sucet += int(zoznam_sucet[i])  # scita jednotlive cleny zoznamu
        if len(str(sucet)) > 1:  # znova, pokial je vysledok viac ako jednociferne cislo
            zoznam_sucet = list(str(sucet))  # rozdeli cislo na zoznam
            sucet = 0
            for i in range(len(zoznam_sucet)):  # cyklus zisti dlzku zoznamu
                sucet += int(zoznam_sucet[i])   # postupne scita jednotlive cleny zoznamu

    print(f'Výsledok súčtu číslic v čísle: {cislo} je: {sucet}')
    return sucet  # príkaz return nám vráti výsledok s ktorým budeme pracovat dalej


def vyznam_cisla(cislo):
    vyznam = vyznamy_cisel.get(str(cislo))  # zo zadefinovaného slovníku získame číslo, ktoré vyšlo predtým ako výsledok rozdelenia
    print(f'Význam čísla: {cislo} v numerológií je: {vyznam}')


opakovanie_programu = True
while opakovanie_programu:            # cyklus, ktorý nám umozni opakovat program po vložení čísla 1
    vyznam_cisla(rozdelenie_cisla())
    print("Pokiaľ chcete opakovať program vložte číslo 1")
    print("Pokiaľ zadáte iné číslo ako 1 program sa ukončí.")
    rozhodnutie = input().strip()
    if rozhodnutie == str(1):
        vyznam_cisla(rozdelenie_cisla())
    else:
        opakovanie_programu = False



