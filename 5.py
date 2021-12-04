x = int(input("Введите число: "))
lst = []
for i in range(2, x+1):
    for c in lst:
        if i % c == 0:
            break
    else:
        lst.append(i)
print(lst)
