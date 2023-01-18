import os
import time
path2 = r"J:\MS数据\合成一部\0-MS待确认"
file1 = os.listdir(path2)
for i in range(len(file1)):
    try:
        if "zdec" in file1[i]:
            l = file1[i][:-13]
            if l[-1:] == "_":
                l = l[:-1]
            l = l + ".PNG"
            os.rename(path2 + "\\" + file1[i],path2 + "\\" + l)
            print("\r进度{:.2f}%".format(i/len(file1)*100),end="")
    except:
        pass
