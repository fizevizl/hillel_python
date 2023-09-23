
input = input("Введіть число: ")

if input.isdigit():
    number = int(input)
    result = "парне" if number % 2 == 0 else "непарне"
    print(f"Ви ввели {result} число")
else:
    print("Не вірне введення")
