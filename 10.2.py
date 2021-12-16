variant = int(input('Выберите вариант конвертации: \n 1. Метры в сантиметры\n 2. Метры в футы\n 3. Метры в дюймы\n 4. Метры в сажени\n '))

if variant == 1:
    result = float(input('Сколько метров? :\n'))
    print(result, 'метров составляют', round((result * 100), 2), 'сантиметров')
elif variant == 2:
    result = float(input('Сколько метров? :\n'))
    print(result, 'метров составляют', round((result * 3.281), 2), 'футов')
elif variant == 3:
    result = float(input('Сколько метров? :\n'))
    print(result, 'метров составляют', round((result * 39.37), 2), 'дюймов')
elif variant == 4:
    result = float(input('Сколько метров? :\n'))
    print(result, 'метров составляют', round((result / 1.829), 2), 'саженей')
else:
    print('Unknown')
