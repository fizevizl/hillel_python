
list_num = [1, 2, 2, 3, 3, 3, 4, 6, 4, 4, 4]

num_rep = {}

for num in list_num:
    num_rep[num] = list_num.count(num)

for num, qty in num_rep.items():
    print(f"{num}: {qty} разів")
