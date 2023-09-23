
import random

guest_num = 0
number = random.randint(1, 10)

while guest_num < 5:
    guess = int(input("введите число: "))
    guest_num += 1

    if guess < number:
        print("твоё число меньше моего")
    elif guess > number:
        print("твоё число больше моего")
    elif guess == number:
         break

if guess == number:
    print(f"ты угадал моё число за {guest_num}  попыток ")
else:
    print(f"не угадал моё число было {number} ")
