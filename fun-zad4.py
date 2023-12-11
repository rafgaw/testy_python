# funkcja zagnieżdżona

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")
    return fun2

    # def fun3():
    #     print("To jest fun3")
    # return fun2


fun1()
print(fun1())
xFun = fun1()
print(xFun)
print(type(xFun))
xFun()  # To jest fun2
