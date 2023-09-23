
while True:
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")
    if not age.isdigit():
        print("Помилка, повторіть введення.")
        continue 

    age = int(age)

    if age == 0:
        print("Помилка, повторіть введення.")
    elif age < 10:
        print(f"Привіт, шкет {name}!")
    elif age <= 18:
        print(f"Як справи, {name}?")
    elif age < 100:
        print(f"Що бажаєте, {name}?")
    else:
        print(f"{name}, ви брешете - у наш час стільки не живуть...")

    exit = input("Бажаєте вийти? (Д/Y)").lower()
    if exit in ("y", "д"):
        break
