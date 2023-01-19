#双重加密
alphabet = "abcdefghijklmnopqrstuvwxyz"
morse_code = [".-","-...","-.-.","-..",
              ".","..-.","--.","....",
              "..",".---","-.-",".-..",
              "--","-.","---",".--.",
              "--.-",".-.","...","-",
              "..-","...-",".--","-..-",
              "-.--","--.."]
morse_dict = dict(zip(alphabet, morse_code))
x = ord("A")
y = ord("a")
plaintext = input("请输入需要加密的明文（只能由字母构成）：")
num = int(input("请输入需要移动的位数："))
ciphertext = []
for i in plaintext:
    if i == " ":
        ciphertext.append(" ")
    elif i.isupper():
        ciphertext.append(chr((ord(i) - x + num) % 26 + x))
    elif i.islower():
        ciphertext.append(chr((ord(i) - y + num) % 26 + y))
print("凯撒加密后的密文为{}".format("".join(ciphertext)))
print("凯撒·莫斯加密后的密文是{}".format(" ".join([morse_dict[i.lower()] for i in "".join(ciphertext) if i != " "])))
