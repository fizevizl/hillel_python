
n = int(input("Введіть ціле додатне число n: "))
total = 0
i = 1

while i <= n:
    if i % 3 != 0:  
        total += i**3
    i += 1

print(n, total)
