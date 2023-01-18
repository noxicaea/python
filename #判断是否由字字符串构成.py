#判断是否由字字符串构成
text = input("请输入一个由字母构成的字符串：")
x = len(text)
for i in range(1,x//2+1):
    if x % i == 0:
        if text.startswith(text[0:i]) and text.count(text[0:i]) == x//i:
            print("True")
            break
else:
    print("False")

