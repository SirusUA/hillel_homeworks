x = [i for i in input().split()]
x.sort()
lst = []
b = len(x) - 2
for i in range(0, len(x) - 1):
    if x.count(x[i]) > 1 and x[i] not in lst:
        lst.append(x[i])
print(lst[0])
