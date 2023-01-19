import random
x = [random.randint(1, 100) for i in range(100)]
y = [random.randint(50, 150) for i in range(100)]
inter = dict.fromkeys([z for z in x if z in y])
print(list(inter.keys()))