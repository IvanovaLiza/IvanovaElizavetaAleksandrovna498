import csv

# по введенной дате находим нужную строку
def search(dt, data):
    for stroka in data:
        if stroka[2] == dt:
            return stroka
    return None

with open('scientist.txt', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter='#'))


    dt = input()
    while dt != "эксперимент":
        res = search(dt, data)
        if res == None:
            print("В этот день ученые отдыхали")
        else:
            print(f"Ученый {res[0]} создал препарат: {res[1]} - {dt}")
        dt = input()
