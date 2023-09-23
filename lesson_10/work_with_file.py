
line_1 = input("введіть першу строку")
line_2 = input("введіть другу строку")
line_3 = input("введіть третю строку")
line_4 = input("введіть четверту строку")

with open("myfile.txt", "w") as file:
    file.write(line_1 + "\n")
    file.write(line_2 + "\n")

with open("myfile.txt", "a") as file:
    file.write(line_3 + "\n")
    file.write(line_4 + "\n")
