# Логика:

# одно число a → вернуть кортеж от 0 до a (или от a до 0, если a < 0);
# два числа a и b → вернуть кортеж от меньшего к большему;
# больше двух чисел → вернуть кортеж из этих чисел;
# нет чисел → вернуть пустой кортеж.

def sequence(*args):
    switch_index = len(args)
    match switch_index:
        case 0:
            return tuple()
        case 1:
            return tuple(range(args[0]+1)) if args[0] >= 0 else tuple(range(args[0],1))
        case 2:
            return tuple(range(args[0],args[1]+1)) if args[1] > args[0] else tuple(range(args[1],args[0]+1))
        case _:
            return args
    pass

assert sequence(5) == (0, 1, 2, 3, 4, 5), "Ожидался диапазон от 0 до 5"
assert sequence(-3) == (-3, -2, -1, 0), "Ожидался диапазон от -3 до 0"
assert sequence(2, 6) == (2, 3, 4, 5, 6), "Ожидался диапазон от 2 до 6"
assert sequence(10, 7) == (7, 8, 9, 10), "Ожидался диапазон от 7 до 10"
assert sequence(1, 2, 3, 4) == (1, 2, 3, 4), "Ожидался кортеж из переданных чисел"


GREEN  = "\033[32m"
print(f"{GREEN}Test completed")