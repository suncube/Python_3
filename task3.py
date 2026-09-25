# Требуется:
# 1. Определить, в каком магазине каждый товар самый дешёвый.
# 2. ```*```Определить, в каком магазине выгоднее всего купить **все товары сразу**.


def cheapest_items(shops):
    items = {}
    for item in shops:
        for key in item.keys():
            if key not in items.keys():
                items[key] = (shops.index(item), item[key])
            elif item[key] < items[key][1]:
                items[key] = (shops.index(item), item[key])
    return items

def cheapest_shop_total(shops):
    cheapest_shop = False 
    index = 0
    for item in shops:
        current_sum = sum(item.values())
        if not cheapest_shop:
            cheapest_shop = (current_sum, index)
        elif current_sum < cheapest_shop[0]:
            cheapest_shop = (current_sum, index)
        index += 1
    return cheapest_shop[1]


# --- Набор 1 ---
shops1 = [
    {"хлеб": 1, "молоко": 2},
    {"хлеб": 0.8, "молоко": 2.5},
    {"хлеб": 1.2, "молоко": 1.9},
]

print(cheapest_items(shops1))
print(cheapest_shop_total(shops1))

assert cheapest_items(shops1)["хлеб"][0] == 1, "Неверный магазин для хлеба (shops1)"
assert cheapest_items(shops1)["молоко"][0] == 2, "Неверный магазин для молока (shops1)"
assert cheapest_items(shops1)["хлеб"][1] == 0.8, "Неверная цена хлеба (shops1)"
assert cheapest_items(shops1)["молоко"][1] == 1.9, "Неверная цена молока (shops1)"
assert cheapest_shop_total(shops1) == 0, "Неверный магазин по сумме (shops1)"
print("\033[32m Test 1 completed\033[0m")

# --- Набор 2 ---
shops2 = [
    {"яблоко": 3, "банан": 2, "киви": 5},
    {"яблоко": 2.5, "банан": 2.2, "киви": 4.8},
    {"яблоко": 3.1, "банан": 1.9, "киви": 5.1},
]
print(cheapest_items(shops2))
print(cheapest_shop_total(shops2))
assert cheapest_items(shops2)["яблоко"][0] == 1, "Неверный магазин для яблок (shops2)"
assert cheapest_items(shops2)["банан"][0] == 2, "Неверный магазин для бананов (shops2)"
assert cheapest_items(shops2)["киви"][0] == 1, "Неверный магазин для киви (shops2)"
assert cheapest_shop_total(shops2) == 1, "Неверный магазин по сумме (shops2)"
assert cheapest_items(shops2)["банан"][1] == 1.9, "Неверная цена банана (shops2)"
print("\033[32m Test 2 completed\033[0m")

# --- Набор 3 ---
shops3 = [
    {"рис": 4.5, "гречка": 3.2},
    {"рис": 4.4, "гречка": 3.5},
    {"рис": 4.6, "гречка": 3.0},
]

print(cheapest_items(shops3))
print(cheapest_shop_total(shops3))
assert cheapest_items(shops3)["рис"][0] == 1, "Неверный магазин для риса (shops3)"
assert cheapest_items(shops3)["гречка"][0] == 2, "Неверный магазин для гречки (shops3)"
assert cheapest_items(shops3)["гречка"][1] == 3.0, "Неверная цена гречки (shops3)"
assert cheapest_items(shops3)["рис"][1] == 4.4, "Неверная цена риса (shops3)"
assert cheapest_shop_total(shops3) == 2, "Неверный магазин по сумме (shops3)"
print("\033[32m Test 3 completed\033[0m")

# --- Набор 4 ---
shops4 = [
    {"масло": 5.5, "сыр": 7.2, "йогурт": 2.1},
    {"масло": 5.4, "сыр": 7.5, "йогурт": 2.0},
    {"масло": 5.6, "сыр": 7.0, "йогурт": 2.3},
]

print(cheapest_items(shops4))
print(cheapest_shop_total(shops4))

assert cheapest_items(shops4)["масло"][0] == 1, "Неверный магазин для масла (shops4)"
assert cheapest_items(shops4)["сыр"][0] == 2, "Неверный магазин для сыра (shops4)"
assert cheapest_items(shops4)["йогурт"][0] == 1, "Неверный магазин для йогурта (shops4)"
assert cheapest_items(shops4)["сыр"][1] == 7.0, "Неверная цена сыра (shops4)"
assert cheapest_shop_total(shops4) == 0, "Неверный магазин по сумме (shops4)"
print("\033[32m Test 4 completed\033[0m")