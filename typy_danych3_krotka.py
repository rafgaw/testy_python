# krotka - sekwencja niezmienna

tupla = ("asd")

tupl2 = "asd",

tulp3 = "asd", 36, 6

print(tupla)
print(tupl2)
print(tulp3)

tuple_names = "radek", "tomek", "zenek", "mirek"
tuple_names2 = ("radek", "tomek", "zenek", "mirek")

tupla_liczby = 34, 234, 121, 999
print(tupla_liczby)

# tuple mozna uzunąć del tupla ale nie da sie sie usunac pojedynczego elementu del tupla[0]

print(tupla_liczby[0])
print(tupla_liczby[2:])
print(tupla_liczby[-1::-1])  # od -1 do nic krok co -1 czyli do tylu (999, 121, 234, 34)

print("radek" in tuple_names)  # czy istnieje

print(sorted(tuple_names))  # dostajemy liste ['mirek', 'radek', 'tomek', 'zenek']

print(sorted(tuple_names, reverse=True))

# rozpakowanie tupli
a, *b, c = 1, 2, 3, 4, 5
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

lista = list(tuple_names)
print(lista)
print(type(lista))
print(len(lista))


