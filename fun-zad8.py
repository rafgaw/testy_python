def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)
allparams(1, 2, 3)
allparams(1, 2, 3, d=8)
allparams(1, 2, c=8, d=9)
allparams(1, 2, c=8, d=9, a=9)
allparams(1, 2, 8, 9, 6, 7, 8, 5, d=9, a=9)
