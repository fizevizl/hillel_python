
def check_num(x):
    try:
        num = int(x)
        return num
    except ValueError:
        try:
            num = float(x.replace(',', '.'))
            return num
        except ValueError:
            return x
        
# ============

def signum(x):
    if x < 0:
        return "від\'ємне"
    elif x > 0:
        return "додатне" 
    else:
        return "нуль"
    
# ============       

def exit_quest(x): 
    check_list = ["вихід", "exit", "quit", "e", "q"]
    return x.lower() in check_list

# ============

def work(st):
    value = check_num(st)

    if isinstance(value, int):
        znak = signum(value)
        if znak == "нуль":
            txt = "Ви ввели нуль"
        else: 
            txt = f"Ви ввели {znak} ціле число: {value}"
    elif isinstance(value, float):
        znak = signum(value)
        if znak == "нуль":
            txt = "Ви ввели нуль"
        else:
            txt = f"Ви ввели {znak} дробове число: {value}"
    else:
        txt = f"Ви ввели некоректне число: {value}"
    return txt

# ============

while True:
    user_input = input("Введіть число: ")
    if exit_quest(user_input):
        break
    print(work(user_input), "\n")

print("\nfinish")   
        