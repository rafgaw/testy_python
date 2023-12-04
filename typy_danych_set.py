# set - zbior - przechowuje unikatowe wartosci
# nie zachowuje kolejnosci podczas dodawania elementow

lista = [11, 22, 33, 55, 99, 11, 22, 999]
zbior = set(lista)
print(lista)
print(zbior)

zb2 = set()  # pusty set
print(zb2)

# dodawanie elementow do zbioru

zb2.add(2)
zb2.add(22)
zb2.add(344)
zb2.add(53423)
zb2.add(222)
zb2.add(23)
zb2.add(2)
zb2.add(244)

print(zb2)

print(zb2.pop())  # usuwanie pierwszego zbioru z listy wyswietlanych

print(sorted(zb2))

zbior2 = {22, 45, 23, 345, 2666, 34234, 6566}
print(zbior2)

# suma zbiorow

print(zb2 | zbior2)
print(zb2.union(zbior2))

zbior3 = {44, 22, 33}

print(zb2.union(zbior2, zbior3))

# czesc wspolna zbiorow

print(zb2 & zbior2)

# rózenica zbiorow

print(zbior2 - zb2)

print(zb2.difference(zbior2))

zbior4 = zbior3.copy()
zbior3.clear()
print(zbior4)

zbior3.update(zb2)
print(zbior3)

zb3 = {1, 2, 3, 4, 5, 7}
print(sum(zb3))
print(min(zb3))
print(max(zb3))
print(len(zb3))
print(sorted(zb3))
