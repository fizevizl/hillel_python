
n = int(input("Введіть ціле додатне число n: "))
total = 0

for i in range(1, n + 1):
    if i % 3 != 0: 
        total += i**3

print(n, total)
