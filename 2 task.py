import csv
with open('scientist.txt', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter='#'))