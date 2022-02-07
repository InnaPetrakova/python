a=int(input("Введите целое положительное число "))
tmax=0
while a>0:
    t1 = a % 10
    if t1>tmax:
        tmax = t1
    a = a // 10
print(tmax)
