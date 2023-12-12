from abc import ABC


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lecę z szybkością", self.szybkosc)

    # @abstractmethod
    def wydaje_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, ", ja nie latam")

    def wydaje_odglos(self):
        print("kokokoko")

    def dziobanie(self):
        print(f"Tu {self.gatunek} ,ja sobie podziobie")

class Orzel(Ptak):
    def wydaje_odglos(self):
        print('kier kirr')

# or1 = Ptak("Orzeł", 45)
# or1.latam()
# ku1 = Ptak("Kura", 0)
# ku1.latam()

ku2 = Kura("Kura")
ku2.latam()
ku2.wydaje_odglos()
ku2.dziobanie()

or2 = Orzel("Orzeł", 45)
or2.wydaje_
odglos()
or2.latam()
