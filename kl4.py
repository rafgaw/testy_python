class Dom:
    """
    Klasa opisująca dom w pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Mamy kolor", self.__kolor)

    def podaj_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.__kolor = wybor
        self.mam_kolor()


dom1 = Dom(100, "czerwony", 8)
dom1.mam_kolor()
dom1.podaj_kolor()
