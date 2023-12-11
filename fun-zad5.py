# stworzyć funkcje kantor

waluta = input("""podaj walute:
""")
kwota = float(input("""Podaj kwote:
"""))


def kantor(waluta):
    print("Przeliczam ", waluta)

    def euro(kwota):
        print(kwota * 4.32)

    def usd(kwota):
        print(kwota * 4.04)

    if waluta == 'euro':
        return euro
    else:
        return usd


kantor_waluta = kantor(waluta)
kantor_waluta(kwota)
