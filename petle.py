# for
import random
from itertools import zip_longest

for i in range(10):  # 0...9
    print(i)

print("-----------------------")

for i in range(1, 10):  # 1...9
    print(i)

print("-----------------------")

my_string = "Radek"
for i in my_string:
    print(i)

print("-----------------------")

lista_lotto = list(range(1, 50))
for i in range(6):
    wyn = random.choice(lista_lotto)
    lista_lotto.remove(wyn)
    print(wyn)

print("-----------------------")

for _ in range(4):
    print("Rafał")
    print(_)

print("-----------------------")

for i in range(10):
    if i % 2 == 0:
        print(i, "jest parzyste")

print("-----------------------")

lista3 = [j for j in range(1, 10) if j % 2 == 0]
for c in lista3:
    if c == 3:
        c += 1  # c = c + 1
print(c)

print("-----------------------")

# direc = {}
imiona = ["Radek", "Rafał", "Seba", "Zbyszek"]
for p in imiona:
    #    direc[p] = imiona.index(p)
    print(imiona.index(p), p)

print("-----------------------")

# enumerate() - numeruje kolekcje
for p in enumerate(imiona):
    print(p)

for p, o in enumerate(imiona, start=1):
    print(p, o)

print("-----------------------")

ludzie = ["Radek", "Rafał", "Seba", "Zbyszek"]
wiek = [45, 21, 44, 53]

for x in range(len(ludzie)):
    print(ludzie[x], wiek[x])

print("-----------------------")

ludzie = ["Radek", "Rafał", "Seba", "Zbyszek", "Adam"]
wiek = [45, 21, 44, 53]

for i in zip(ludzie, wiek):
    print(i)

for p, w in zip(ludzie, wiek):
    print(p, w)

print("-----------------------")

zipped = zip_longest(ludzie, wiek, fillvalue=None)
zipped_list = list(zipped)

for name, age in zipped_list:
    print(name, age)

print("-----------------------")

for i in enumerate(zipped_list):
    print(i)

print("-----------------------")

for i, (p, w) in enumerate(zipped_list):
    print(i, p, w)

print("-----------------------")

for i in range(0, 10, 2):  # start, stop, krok
    print(i)
for i in range(10, 0, -2):  # start, stop, krok
    print(i)

parzyste = [i for i in range(0, 10, 2)]
print(parzyste)
print("-----------------------")

c = {'name': 'Radek', 'age': '5'}
print({v: k for k, v in c.items()})

print("-----------------------")
