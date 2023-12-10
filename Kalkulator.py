# Kalkulator
#  list = [1, 2, 3, 4, 0]

# from os import system, name
#
#
# # define our clear function
# def clear():
#     # for windows the name is 'nt'
#     if name == 'ce':
#         _ = system('cls')
#
#     # and for mac and linux, the os.name is 'posix'
#     else:
#         _ = system('clear')
# import pyautogui
#  pyautogui.hotkey('command', 'l')

# from __future__ import print_function

# def wipe():
#     os.system("clear && printf '\e[3J'")


#
# clear = lambda: os.system('cls')
#     # for windows
#     # if name == 'nt':
#          _ = system('cls')
# clear = "\r"

while True:
    menu = int(input("""Wybierz działanie:
1. Dodawanie
2. Odejmowanie
3. Mnożenie
4. Dzielenie
0. Wyjście
:"""))
    clear()
    #    print(menu)
    # if not menu.isnumeric():
    #     print(f"{menu} To nie cyfra")
    if menu not in [1, 2, 3, 4, 0]:
        print(f"{menu} nie ma na liscie menu")
    if menu == 1:
        a = int(input("""Podaj pierwszą liczbe:
        """))
        b = int(input("""Podaj druga liczbe:
        """))
        print(f"Wynik {a} + {b} to:")
        print(a + b)
    elif menu == 2:
        a = int(input("""Podaj pierwszą liczbe:
            """))
        b = int(input("""Podaj druga liczbe:
            """))
        print(f"Wynik {a} - {b} to:")
        print(a - b)
    elif menu == 3:
        a = int(input("""Podaj pierwszą liczbe:
            """))
        b = int(input("""Podaj druga liczbe:
            """))
        print(f"Wynik {a} * {b} to:")
        print(a * b)
    elif menu == 4:
        a = int(input("""Podaj pierwszą liczbe:
            """))
        b = int(input("""Podaj druga liczbe:
            """))
        print(f"Wynik {a} / {b} to:")
        print(a / b)
    if menu == 0:
        print("Wyjście")
        break
