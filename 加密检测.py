plaintext = input("请输入需加密的明文：")
conditions = True
while conditions:
    password = input("请输入密文：")
    cipher = input("请输入密码：")
    if len(password) != len(cipher):
        print("密文和密码长度不一致！")
    else:
        print(f"加密后的密文为：{plaintext.translate(str.maketrans(password, cipher))}")
    if (plaintext.translate(str.maketrans(password, cipher))).translate(str.maketrans(cipher, password)) == plaintext:
        conditions = False
    else:
        print("密码和密文冲突！,无法解密！请重新输入！")
