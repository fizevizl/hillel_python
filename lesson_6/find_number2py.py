
import random

def chek(num, x):
    if num == x:
        return True
    numtype = "меньше" if num > x else "больше" 
    print(f"твоё число {numtype} моего")
    return False

def printresult(g, c, n):
    print("=======")   
    if g == n:
        print(f"ты угадал моё число за {c}  попыток ")
    else:
        print(f"не угадал моё число было {n} ")


count = 0
number = random.randint(1, 10)

while count < 5:
    guess = int(input("введите число: "))
    count += 1
    if chek(number, guess):
        break
   
printresult(guess, count, number)