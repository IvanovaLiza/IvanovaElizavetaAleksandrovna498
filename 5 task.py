import csv
import random

def hash(s):
    res = ''.join(random.choice(i) for i in range(0, 1024))
    ind = res % 1024
    return ind

with open('scientist.txt', encoding='utf-8') as file, open('scientist_with_hash.csv', 'w', encoding='utf-8') as new_file:
    data = list(csv.reader(file, delimiter=','))
    res = csv.writer(new_file, delimiter=',')

    res = res[-1].append('hash')
    res.writerow(data[0])
    for stroka in data[1:]:
        if stroka == hash(stroka):
            k = hash(stroka)
        sm = sum(k)
        res.writerow(sm)
