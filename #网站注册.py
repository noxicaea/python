#网站注册
user ={"小甲鱼":"I_love_FishC","不二如是":"FishC5201314"}
def register():
    username = input("请输入用户名:")
    if username in user:
        judge = True
    else:
        judge = False
    while judge:
        if username in user:
            print("用户名已存在！")
            username = input("请重新输入用户名:")
    password = input("请输入密码:")
    user.update({username:password})
    print("注册成功！")
    return user
def Already_registered():
    print("".center(30,"-"))
    print("目前已注册用户有：")
    for key in user:
        print(key)
register()
Already_registered()
