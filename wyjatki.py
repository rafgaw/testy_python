try:
#  print(5 / 0)
#    print("a" / 2)
except ZeroDivisionError:
    print("nie dziel przez zero!")
except TypeError:
    print("blad typu")
except ValueError:
    print("blad wartosci")
except Exception as e:
    print("błąd", e)
else:
    print("wykona sie jesli nie ma bledu")
finally:
    print("wykona sie niezaleznie czy blad wystapi czy nie")
