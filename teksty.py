txt = '\tHello Worldśćź'
print(txt)
txt2 = txt.lower()
print(txt2)
txt3 = txt2.upper()
print(txt3)

print(txt.removesuffix("World"))
print(txt.removeprefix("Hello"))

encoded_s = txt.encode('utf-8')
print(encoded_s)



imie = "rafal"

tekst_format = F'asdasd {imie} sd'  # f pozwala dodawać zmienne

print(tekst_format)

starszy = "Witaj %s!"
print(starszy % imie)
