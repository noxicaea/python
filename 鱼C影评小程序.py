Continue_with_entry = "y"
dict_movie = {}
print("欢迎进入鱼C影评小程序")
print("1.数据录入\n2.数据查询\n3.退出程序")
def fun1():
    Continue_with_entry = "y"
    dict_movie_fun1 = {}
    while Continue_with_entry == "y":
        Movie_name = input("请输入电影名称：")
        date_1 =input("请输入上映日期：")
        director_name = input("请输入导演名称(多人请用/分割)：")
        actor_name = input("请输入主演名称(多人请用/分割)：")
        Movie_rating = input("请输入电影评分：")
        dict_movie_fun1.update({Movie_name:{"电影名称":date_1,"上映日期":director_name,"导演名称":actor_name,"电影评分":Movie_rating}})
        print("录入成功！")
        Continue_with_entry = input("是否继续录入(y/n)：")
        if Continue_with_entry == "n":
            return dict_movie.update(dict_movie_fun1)
def fun2():
    Continue_with_entry = "y"
    while Continue_with_entry == "y":
        Movie_name = input("请输入电影名称：")
        if Movie_name in dict_movie:
            outs = dict_movie.get(Movie_name)
            for key,value in outs.items():
                print(f"{key}:{value}")
        else:
            print(f"没有{Movie_name}此电影！")
        Continue_with_entry = input("是否继续录入(y/n)：")
while Continue_with_entry == "y":
    fun = int(input("请输入想要的功能(1/2/3)："))
    if fun == 1:
        fun1()
    elif fun == 2:
        fun2()
    elif fun == 3:
        a = input("谢谢使用,按任意键退出！")
        break

