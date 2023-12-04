import random

print(random)

print(random.randint(1, 6))  # 1...6
print(random.randrange(1, 6))  # 1...5
print(random.randrange(6))  # 0...5
print(random.random())  # (0..1)
print(random.random() * 10)  # (0..1)

lista = [3, 7, 23, 66, 1234]

print(random.choice(lista))
print("----------------------")
lista_lotto = list(range(1, 50))
a = (random.choice(lista_lotto))
print(a)
lista_lotto.remove(a)
b = (random.choice(lista_lotto))
print(b)
lista_lotto.remove(b)
c = (random.choice(lista_lotto))
print(c)
lista_lotto.remove(c)
d = (random.choice(lista_lotto))
print(d)
lista_lotto.remove(d)
e = (random.choice(lista_lotto))
print(e)
lista_lotto.remove(e)
f = (random.choice(lista_lotto))
print(f)
lista_lotto.remove(f)

print(random.choices(lista_lotto, k=6))  # losowanie z powtorzeniami
print(random.sample(lista_lotto, 6))  # losowanie bez powtorzen


