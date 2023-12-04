# slownik - para: klucz wartosci
# {'name' : ' Radek'}
# klucze nie moga sie powtarzac

my_dict = {"a": 'one', 'B': 'two', 'C': 'three'}
print(type(my_dict))
print(my_dict)

# pusty slownik
empty_dict = {}
empty_dict2 = dict()

print(empty_dict)
print(empty_dict2)

dict_mixed = {1: 'one', 'A': 'two', 3: 'three'}
print(dict_mixed)

print(dict_mixed.keys())
print(dict_mixed.items())
print(dict_mixed.values())

dictionary = {'x': 2}
dictionary.update([('y', 2), ('z', 3)])
print(dictionary)

empty_dict['imie'] = 'Radek'
empty_dict['wiek'] = 33

print(empty_dict)

empty_dict['wiek'] = 43

print(empty_dict)

print(empty_dict['wiek'])
print(empty_dict.get('wiek'))
print(empty_dict.get('wiek2', 'default'))

slownik = {'kot': 'cat', 'pies': 'dog', 'dom': 'house'}
print((f"Potrafie przetłumaczyć : {slownik.keys()}"))
# key = input("podaj słowo")
# print(slownik[key.lower().replace(" ", "")])

# input zwraca sting

# a = float(input("Podaj pierwsza liczbe"))
# b = input("Podaj druga liczbe")
# print(a + int(b))

