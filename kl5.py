class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja

class Manager(Pracownik):  # dziedziczenie po Pracownik
    """
    Manager
    """
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia
    def oblicz_pensje(self):
        return self.premia + self.pensja


pracownik = Pracownik("Jan", "Kowalski", 4249)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wyn_prac} zł")

manager = Manager("Anna", "Nowak", 8000, 3000)
manager.przedstaw_sie()
wyn_men = manager.oblicz_pensje()
print(f"Wynagrodzenie managera {manager.imie} {manager.nazwisko}: {wyn_men} zł")
