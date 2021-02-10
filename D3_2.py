def info_user(**user_name):
    return ' '.join(user_name.values())


name = input ("Ваше имя -")
surname = input ("Ваша фамилия -")
birthday = input ('Дата рождения -')
city = input ('Город -')
email = input ('Эл.почта -')
Fphone = input ('Номер телефона -')

print(info_user(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))
