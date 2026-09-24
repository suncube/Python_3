# Написать функцию, которая принимает строку текста и возвращает слово, встречающееся чаще всего.  
# Функция должна учитывать, что в тексте могут быть знаки препинания и разные регистры букв.

def most_common_word(text):
    txt = str(text).lower()
    for letter in '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~`':
        txt = txt.replace(letter, '')

    words = txt.split()
    words_info = {}

    for word in words:
        #if len(word) < 2: continue

        if word in words_info.keys():
            words_info[word] += 1
        else:
            words_info[word] = 1

    sorted_dict = sorted( words_info.items(), key = lambda x: x[1], reverse = True)
    return sorted_dict.pop(0)[0]
    pass # тут ваш код

print(most_common_word("кот кот собака"))
assert most_common_word("кот кот собака") == "кот", "Самое частое слово — кот"
assert most_common_word("Кот кот КОТ собака") == "кот", "Регистр должен игнорироваться"
assert most_common_word("молоко, молоко! молоко? хлеб.") == "молоко", "Знаки препинания должны игнорироваться"
assert most_common_word("слово") == "слово", "Ожидалось единственное слово"
res = most_common_word("а б а б")
assert res in ("а", "б"), "Ожидалось одно из слов с максимальной частотой"

GREEN  = "\033[32m"
print(f"{GREEN}Test completed")