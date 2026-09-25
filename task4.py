# Написать функцию `flatten_list(lst)`, которая принимает вложенный список и возвращает плоский список.

# Пример:  
# `flatten_list([1, [2, [3, 4], 5], 6]) → [1, 2, 3, 4, 5, 6]`

def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            sub_list = flatten_list(item)
            result += sub_list
        else:
           result.append(item)
    return result;

#print(flatten_list([1, [2, 3 ,[4, [5]]]]))

assert flatten_list([1, [2, 3]]) == [1, 2, 3], "Ожидался простой плоский список"
assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4], "Ожидалась глубокая распаковка"
assert flatten_list([]) == [], "Ожидался пустой список"
assert flatten_list([[], [1], [], [2, [], 3]]) == [1, 2, 3], "Ожидалось игнорирование пустых вложенных списков"
assert flatten_list([1, ["a", ["b", "c"]], 2]) == [1, "a", "b", "c", 2], "Ожидалась корректная распаковка смешанных типов"

print("\033[32m Test completed\033[0m")