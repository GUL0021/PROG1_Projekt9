from PyQt5 import QtWidgets, uic
from Projekt9 import Soucet


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
    with open('rozlozenie_cisla.ui') as f:
        uic.loadUi(f, window)

    mc = Okno()
    mc.set_window(window)
    x = QtWidgets.QLineEdit()

    window.spustit_PushButton.clicked.connect(mc.button_click)
    window.show()

    return app.exec()


main()
