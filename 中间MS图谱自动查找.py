import os,xlrd,shutil,time,datetime
import pandas as pd
path1 =r"\\192.168.1.232\MS数据\中间质检\A-合成一部" #绝对路径，如果程序不运行就检查路径是否有不同
path2=r"\\192.168.1.232\MS数据\合成一部\0-MS待确认" #绝对路径
path3=r"V:\03_纯化\中间MS" #绝对路径
t=datetime.datetime.now()
ti = t.strftime("%m-%d") #获取当前日期
file1 = os.listdir(path1) #获取【U:\MS数据\中间质检\A-合成一部】的中间MS数据的文件名称
file2 = os.listdir(path2) #获取【U:\MS数据\合成一部\0-MS待确认】的MS图谱文件名
for i in file2:
    try:
        if "zdec" in i:
            l = i[:-13]
            if l[-1:] == "_":
                l = l[:-1]
            l = l + ".PNG"
            os.rename(path2 + "\\" + i,path2 + "\\" + l)
    except:
        pass
try:
    os.mkdir(r"V:\03_纯化\中间MS" + "\\" + ti) #创建当前日期的文件夹
except:
    pass
file2 = os.listdir(path2)
file3 = os.listdir(r"V:\03_纯化\中间MS" + "\\" + ti) #获取已完成MS数据完成的文件名
print("已完成：",file3 )

for i in file3:     
    if i in file1:
        os.rename(path1 + "\\" + i,path1 + "\\" + "已完成-" + i)
        file1.remove(i) #如果此MS文件数据已经完成则移出列表不再搜索

for i in file1:   
    k = []
    if "AZMH" in str(i[:4]): #如果文件名为'AZMH'中间MS分析格式则把引物编号列表翻倍
        df = pd.read_excel(path1+"\\"+i,header=0)
        list1 = list(df.iloc[:,2])
        list1 = list1*2
        print(i[:-4] + ":")
        for j in file2: 
            try:
                list1.index(j[12:-4])
                k.append(j)
                list1.pop(list1.index(j[12:-4]))
            except:
                pass
        if list1 == []:
            try:
                os.mkdir(r"V:\03_纯化\中间MS" + "\\" + ti + "\\" +i)
            except:
                pass
            shutil.copy(path1 + "\\" + i,r"V:\03_纯化\中间MS" + "\\" + ti + "\\" + i) 
            for a in k:
                shutil.move(path2 + "\\" + a,r"V:\03_纯化\中间MS" + "\\" + ti + "\\" +i)
                file2.remove(a)
                #移动MS图谱至中间MS文件夹中
            print(i[:-4],":已完成")
        else:
            print(list1,"未出图")
    elif"AZM" in str(i[:3]) or "AZH" in str(i[:3]):
        df = pd.read_excel(path1+"\\"+i,header=0)
        list1 = list(df.iloc[:,2])
        print(i[:-4] + ":")
        for j in file2: 
            try:
                list1.index(j[12:-4])
                k.append(j)
                list1.pop(list1.index(j[12:-4]))
            except:
                pass
        if list1 == []:
            try:
                os.mkdir(r"V:\03_纯化\中间MS" + "\\" + ti + "\\" +i)
            except:
                pass
            shutil.copy(path1 + "\\" + i,r"V:\03_纯化\中间MS" + "\\" + ti + "\\" + i) 
            for a in k:
                shutil.move(path2 + "\\" + a,r"V:\03_纯化\中间MS" + "\\" + ti + "\\" +i)
                file2.remove(a)
                #移动MS图谱至中间MS文件夹中
            print(i[:-4],":已完成")
        else:
            print(list1,"未出图")
               
input("按<enter>继续：")
                
                
            
            


