# lista

lista = []  # pusta lista
print(lista)
print(type(lista))

lista.append("Radek")
lista.append("Rafał")
lista.append("Renata")
lista.append("Maciek")
lista.append(1)

print(lista)
print(lista[0])
print(lista[-1])
print(len(lista))
print(lista[-5:-2])
print(lista[-2:-5])

# zmiana elementu
lista[2] = 4

print(lista)

# dodanie w konkretne miejsce elementu
lista.insert(1, 'Mara')

print(lista)

# usuniecie elementu

lista.remove("Maciek")

print(lista)

# sprawdzanie indeksu
indeks = lista.index("Rafał")
print(indeks)

# usuniecie elementu po nr indeksu

print(lista.pop(indeks))
print(lista)
print(lista.pop())  # ostatni element

lista2 = lista
lista3 = lista.copy()
lista.clear()
print(lista2)
print(lista)
print(lista3)
print(id(lista))
print(id(lista2))
print(id(lista3))

lista.sort()
print(lista)

krotka = tuple(lista3)
print(krotka)
print(type(krotka))

