# funkcja zwracajace wynik

def dodaj(a, b):
    return a + b  # zwraca wynik


print(dodaj(2, 4))

print("---------------------------------")


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(odejmij())
print(odejmij(1))
print(odejmij(3, 1))
print(odejmij(10, 4, 1))
print(odejmij(a=10, c=4, b=1))

print("---------------------------------")


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))
print(oblicz_vat(vat=8, cena=1000))
