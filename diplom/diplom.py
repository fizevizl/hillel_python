
from operations import *

def menu():
    mnu_list = [
        (" МЕНЮ ", "═", "╔", "╗", "^"),
        (" 1. Генерування данних до файлу", "", "║", "║", "<"), 
        (" 2. Завантажити дані з файлу", "", "║", "║", "<"),
        (" 3. Зберегти данні до файлу", "", "║", "║", "<"),
        (" 4. Новий запис", "", "║", "║", "<"),
        (" 5. Пошук", "", "║", "║", "<"),
        (" ", "", "║", "║", "<"),
        (" 0. Вихід", "", "║", "║", "<"),
        ("", "═", "╚", "╝", "^"),
    ]
    mnu_width = 35
    for item in mnu_list:
        mnu, symb, left, right, style = item
        print(f'{left}{mnu:{symb}{style}{mnu_width}}{right}')
        

def main():
    while True:
        menu()
        choice = input("Введіть номер меню: ")

        if choice == "1":
            print("Ви вибрали №1")
            ...
        elif choice == "2":
            print("Ви вибрали №2")
            ...
        elif choice == "3":
            print("Ви вибрали №3")
            ...
        elif choice == "4":
            print("Ви вибрали №4")
            ...
        elif choice == "5":
            print("Ви вибрали №5")
            ...
        elif choice == "0":
            quit()
            break



if __name__ == "__main__":
    main()