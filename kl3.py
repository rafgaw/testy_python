class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # zmienna prywatna

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 5

    def __zmien_bieg(self):
        print(("zmieniam bieg"))


car1 = Car("Opel Insgnia", 2017)
print(car1)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.gaz())
car1.licznik()
car1.__pedkosc = 0
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()
