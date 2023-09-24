
import csv
import random as rnd
import json

def gen_phones(count):
    code = ['095', '066', '098', '096', '050', '097']
    is_phones = rnd.choices([True, False], weights=[0.75, 0.25], k=count)
    result = []
    for item in is_phones:
        if item:
            phone = f"({rnd.choice(code)}) {rnd.randint(1_000_000, 9_999_999)}"
        else:
            phone = None
        result.append(phone)
    return result


with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

phones = gen_phones(len(data))

csvdata = []
for i, item in enumerate(data):
    id = item
    name, age = data[item]
    name = name['name']
    age = age['age']
    phone = phones[i]
    csvdata.append([id, name, age, phone])

headers = ["id", "name", "age", "phone"]

with open('task.csv', 'w', newline='\n', encoding='utf-8') as f:
    csv_file = csv.writer(f, delimiter=',')
    csv_file.writerow(headers)
    csv_file.writerows(csvdata)