from random import randint

def tylko_parzyste(func):
    def wrapper():
        result = func()
        result = [x for x in result if x % 2 == 0]
        return result
    return wrapper

@tylko_parzyste
def losowe():
    return [randint(0, 20) for i in range(30)]

@tylko_parzyste
def lista_liczb():
    return list(range(0, 40))


print(losowe())
print(lista_liczb())