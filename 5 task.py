import csv
import random

# Выполнение функции для нахождения индекса
def hash(s):
    res = ''.join(random.choice(i) for i in range(0, 1024))
    ind = res % 1024
    return ind

# Открываем файл и создаем новый файл с измененными данными по задаче
with open('scientist.txt', encoding='utf-8') as file, open('scientist_with_hash.csv', 'w', encoding='utf-8') as new_file:
    data = list(csv.reader(file, delimiter='#'))
    res = csv.writer(new_file, delimiter='#')

# Нахождения нужной строки
    data = data.append('hash')
    for stroka in data[1:]:
        k = hash(stroka)
        sm = (sum(k) % 2048)
        stroka.append(sm)
    res.writerow(stroka)
