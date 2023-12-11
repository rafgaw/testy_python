# funkcja, ktora oblicza srednia

def liczby(name=None, *cyfry):
    print(cyfry)
    suma = 0
    try:
        for cy in cyfry:
            suma += cy
        count = len(cyfry)
        print(f"Uczeń {name} Średnia {suma / count}")
    except Exception as e:
        print("Błąd ", e)


liczby(1, 2, 3, 4, 5)
liczby()
liczby('Rafał', 1, 2, 3, 4, 5, 6)
