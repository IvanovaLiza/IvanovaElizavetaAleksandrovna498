import csv

with open('scientist.txt', encoding='utf-8') as file, open('scientist_origin.txt.csv', 'w', encoding='utf-8') as new_file:
    data = list(csv.reader(file, delimiter='#'))
    res = csv.writer(new_file, delimiter='#')

    prep = 'Аллопуринола'
    a = []
    for stroka in data[1:]:
        if stroka[1] == prep:
            a.append(int(stroka[1]))
    for i in a:
        sort = sorted(i[2])
        if sort < sort[-1]:
            print()