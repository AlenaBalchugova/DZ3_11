def summa():
    s = 0
    while True:
        in_list = input('Введите числа, или введите Exit для выхода: ').split()
        for num in in_list:
            if num == 'Exit':
                return s
            else:
                try:
                    s+= int(num)
                except ValueError:
                    print('Чтобы выйти из программы укажите  Exit - ')

        print(f'Сумма чисел = {s}')
summa()