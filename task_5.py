viruchka=float(input("Введите выручку компании  "))
ubitki=float(input("Введите убытки компании  "))
if viruchka>ubitki:
     rentabelnost=(viruchka-ubitki)/viruchka
     print("Вы работаете в прибыль")
     print("Рентабельность ", "%.2f" % (rentabelnost))
     chisl=int(input("Введите количество сотрудников "))
     prib=(viruchka-ubitki)/chisl
     print("Прибыль фирмы в расчете на одного сотрудника ", "%.1f" % (prib))
elif viruchka<ubitki:
    print("Вы работаете в убыток")
else: print("Вы работаете в ноль")