ford = ["mondeo", "focus", "kuga"]
fiat = ["tipo", "panda", "500"]
renault = ["clio", "megan", "duster"]
x = str("exit")
while True:
    print("Введите название автомобиля:")
    action = input()
    if action in ford:
        print("Ford")
    elif action in fiat:
        print("Fiat")
    elif action in renault:
        print("Renault")
    elif action in x == str("exit"):
        break
    else:
        print("Соответствие не найдено")
