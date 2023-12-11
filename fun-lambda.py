# funkcja lambda - skrocony zapis funkcji
odejmij = lambda a, b: a - b  # domyslnie ma return
print(odejmij(9, 8))

oblicz_vat = lambda cena, vat=8: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))

lista = [1, 2, 3, 4, 5, 55, 66, 100]
for i in lista:
    print(i * 2)

print([i * 2 for i in lista])


def zmien(x):
    return x * 2


# map
print(f"Zastosowanie map() {list(map(zmien, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map() {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie map() {list(filter(lambda x: x > 8, lista))}")
print(f"Zastosowanie map() {list(filter(lambda x: 3 < x < 8, lista))}")


