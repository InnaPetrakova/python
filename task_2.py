t = int(input("Введите время в секундах "))
h = t // 3600
m = (t % 3600) // 60
c = (t % 3600) % 60
print("%02d:%02d:%02d" % (h, m, c))
