from faker import Faker
import random
import json

fake = Faker()
data = {}

for i in range(10):
    id = random.randint(100_000, 999_999)
    age = random.randint(25, 45)
    name = fake.first_name()
    data[id] = ({'name': name}, {'age': age})

print(data)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1)