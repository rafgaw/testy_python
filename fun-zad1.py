# funkcje - wydzielony fragment kodu ktory mozna uzycz wielokrotnie

a = 8
b = 9


# deklaracja funkcji
def dodaj():
    c = 7  # zmienna lokalna
    print(a + b)


dodaj()

print("---------------------------------")


def dodaj2(a, b):
    print(a + b)


dodaj2(5, 9)

print("---------------------------------")


# mozna zasymulowac
def odejmij(a, b, c=0):  # c - parametr domyslny
    print(a - b - c)


odejmij(1, 2)
odejmij(2, 4, 1)
odejmij(b=8, a=4, c=-2)

print("---------------------------------")
