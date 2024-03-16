import csv
import random

# создаем логин из ФИО человека
def create_login(s):
    fio = s.split(' ')
    login = fio[0] + '_' + fio[1][0] + fio[2][0]
    return login

# создаем пароль с помощью random
def create_password(lenght):
    num, upper, lower = '0123456789', 'йцукенгшщзхъфывапролджэячсмитьбюё', 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
    alf = num + upper + lower
    while True:
        res = ''.join(random.choice(alf) for _ in range(lenght))
        n_n, n_u, n_l = 0, 0, 0
        for i in res:
            if i in num:
                n_n += 1
            if i in upper:
                n_u += 1
            if i in lower:
                n_l += 1
        if (n_u > 0) and (n_n > 0) and (n_l > 0):
            return res

# Открываем файл и создаем новый с измененными данными по задаче
with open('scientist.txt', encoding='utf-8') as file, open('scientist_password.csv', 'w', encoding='utf-8') as new_file:
    data = list(csv.reader(file, delimiter=','))
    res = csv.writer(new_file, delimiter=',')

# добавляем нужные столбцы и для каждой строки прописываем логин и пароль
    data[0].append('login')
    data[0].append('password')
    res.writerow(data[0])
    for stroka in data[1:]:
        fio = stroka[0]
        login = create_login(fio)
        password = create_password(8)
        stroka.append(login)
        stroka.append(password)
        res.writerow(stroka)