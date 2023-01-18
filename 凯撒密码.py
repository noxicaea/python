# 凯撒密码
plaintext = input("请输入需要加密的明文（只能由字母构成）：")
num = int(input("请输入需要移动的位数："))
x = ord("A")
y = ord("a")
ciphertext = []
for each in plaintext:
    if each == " ":
        ciphertext.append(" ")
    elif each.isupper():
        ciphertext.append(chr((ord(each) - x + num) % 26 + x))
    elif each.islower():
        ciphertext.append(chr((ord(each) - y + num) % 26 + y))
print("".join(ciphertext))



