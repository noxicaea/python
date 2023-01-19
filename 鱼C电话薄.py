Phone_book = {}
Continue_with_entry = "Y"
print("欢迎进入鱼C电话薄")
def Entry_mode():
    Continue_with_entry = "Y"
    Phone_book_Entry_mode = {}
    print("录入模式".center(30,"-"))
    while Continue_with_entry == "Y":
        name = input("请输入姓名:")
        telephone_number = input("请输入电话号码:")
        judge = all([i.isdigit() for i in telephone_number]) and len(telephone_number) == 11
        while judge == False:
            telephone_number = input("输入不合法，请重新输入电话号码:")
            judge = all([i.isdigit() for i in telephone_number]) and len(telephone_number) == 11
        Phone_book_Entry_mode.update({name:{"姓名":name,"电话号码":telephone_number}})
        Continue_with_entry = input("是否继续录入(Y/N)：")
        if Continue_with_entry == "N":
            return Phone_book.update(Phone_book_Entry_mode)
def query_mode():
    Continue_with_entry = "Y"
    print("查询模式".center(30,"-"))
    while Continue_with_entry == "Y":
        name = input("请输入姓名:")
        if name in Phone_book:
            outs = Phone_book.get(name)
            for key,value in outs.items():
                print(f"{key}:{value}")
        else:
            print(f"没有{name}此人！")
        Continue_with_entry = input("是否继续查询(Y/N)：")
def delete_mode():
    Continue_with_entry = "Y"
    print("删除模式".center(30,"-"))
    while Continue_with_entry == "Y":
        name = input("请输入姓名:")
        if name in Phone_book:
            del Phone_book[name]
            print(f"{name}已删除！")
        else:
            print(f"没有{name}此人！")
        Continue_with_entry = input("是否继续删除(Y/N)：")
        if Continue_with_entry == "N":
            return Phone_book
def print_mode():   
    print("打印模式".center(30,"-"))
    for key in Phone_book:
        print(f"{key}:{Phone_book[key]['电话号码']}")
def exit_mode():
    _ = input("谢谢使用,按任意键退出！")
while Continue_with_entry == "Y":
    command = input("请输入命令（I:录入，C:查询，D:删除，P:打印，E:退出）：")
    if command == "I":
        Entry_mode()
    elif command == "C":
        query_mode()
    elif command == "D":
        delete_mode()
    elif command == "P":
        print_mode()
    elif command == "E":
        exit_mode()
        break