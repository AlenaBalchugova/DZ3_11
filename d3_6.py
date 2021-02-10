def int_func(word):
    abc = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(abc) else False

words = input('Введите слова через пробелы ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')