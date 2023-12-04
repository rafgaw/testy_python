# match case od python 3.10

lista = []
# lang = input("podaj znany Ci język programowania ")

lang = [1, 2, 3]

match lang:
    case "python":
        print("Lubie pythona")
        lista.append(lang)
    case "java":
        print("Java to kawa")
        lista.append(lang)
    case [a, b, c]:
        print(f"lista z trzema elementami {a} {b} {c}")
    case _:  # wartość domyślna
        print("nie znam takiego")
