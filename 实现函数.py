x = [1,2,0]
#all()
for each in x:
    if not each:
        print(False)
        break
else:
    print(True)
#any()
for each in x:
    if each:
        print(True)
        break
else:
    print(False)
#enumerate()
num = 1
for each in x:
    print(num,each)
    num += 1
#zip()
y = ["a","b","c"]
shoter = min(len(x),len(y))
for i in range(shoter):
    print(x[i],y[i])