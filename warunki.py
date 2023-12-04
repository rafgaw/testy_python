# instrukcja warunkowa
# instrukcje sterowanie przeplywem programu

# if warunek:
#   komenda gdy spelniony warunek
# po : musi byc conajmniej jedna komenda pythona

odp = True

if odp:
    print("Brawo")
else:
    print("False")
print("dalsza czesc programu")

if odp:
    pass  # nic nie rob

print("Dalej")

# podatek = 0.9  # 90%
# podatek2 = 0.1  # 10%
# zarobki = float(input("Podaj dochód: "))
#
# if zarobki > 10000:
#     print(f"Podatek:  {zarobki * podatek}")
# elif zarobki > 1000 and zarobki <= 10000:
#     print(f"Podatek:  {zarobki * podatek2}")
# else:
#     print("Ty biedaku")

print("--------------------------")

error_mes = "Stało się coś strasznego"
prog = 'email'
blad = "criticala"
if prog == 'console':
    print(error_mes)
elif prog == 'email':
    if blad == 'critical':
        print("masz blad krytyczny")
    elif blad == 'medium':
        print('ostrzezenie')
    else:
        print('nic szczegolnego')
else:
    print('nie znam takiego systemu')

print("--------------------------")

print("ile to 2 * 2")
a = float(input("podaj wynik: "))
if a == 4:
    print("dobrze grasz dalej")
    wynik = 1
    print("ile to 4 * 4")
    b = float(input("podaj wynik: "))
    if b == 16:
        print("dobrze grasz dalej")
        wynik = wynik+2
        print("ile to 16 * 16")
        c = float(input("podaj wynik: "))
        if c == 256:
            print("dobrze koniec gry")
            wynik = wynik + 44
            print(f"Twój wynik to {wynik}")
        else:
            print(f"""Koniec gry.
Wynik to {wynik}""")
    else:
        print(f"""Koniec gry.
Wynik to {wynik}""")
else:
    print("odpadasz")


