#GUL0021, Gulcik Tomas
# 9.Třída Soucet (bude sčítat cifry v zadaném čísle.
# např. zadá se číslo 5895 a proběhne následující výpočet 5+8+9+5 = 27 > 2+7 = 9 – tzn., až se dojde k jednocifernému číslu
# Metoda secti s parametrem číslo
# Po zobrazeni vysledku, vypise numerologicky vyznam cisla.
from PyQt5 import QtWidgets, uic
from sucet import Soucet


class Okno:
    window = None
    sucet = Soucet()

    def set_window(self, window):
        self.window = window

    def button_click(self):
        vstupne_cislo = self.window.vstupne_cislo.text()
        vysledok_rozlozenia = self.sucet.rozdelenie_cisla(vstupne_cislo)
        self.window.vysledok_rozlozenia.setText(str(vysledok_rozlozenia))
        self.window.vyznam_cisla_v_numerologii.setText(self.sucet.vyznam_cisla(vysledok_rozlozenia))


def main():
    app = QtWidgets.QApplication([])
    window = QtWidgets.QDialog()
    with open('gui_projekt9.ui') as f:
        uic.loadUi(f, window)

    mc = Okno()
    mc.set_window(window)
    x = QtWidgets.QLineEdit()

    window.spustit_PushButton.clicked.connect(mc.button_click)
    window.show()

    return app.exec()


main()
