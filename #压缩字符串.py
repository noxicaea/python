#压缩字符串
text = input("请输入待压缩字符串:")
string = []
count = 0
each = text[0]
for i in text:
    if i == each:
        count += 1
    else:
        if count < 3:
            string.append(each * count)
        else:
            string.append(each + str(count))
        count = 1
        each = i
else:
    if count < 3:
        string.append(each * count)
    else:
        string.append(each + str(count))
print("压缩后的字符串为:{} 压缩率：{:.2%}".format("".join(string),len(string)/len(text)))


# import re
# text = input("请输入待压缩字符串:")
# string = re.sub(r"(.)\1{2,}",lambda m: m.group(1) + str(len(m.group(0))),text)
# print("压缩后的字符串为:{} 压缩率：{:.2%}".format(string,len(string)/len(text)))

# re.sub()函数：
# 它是python中正则表达式库(re)中的一个函数。
# 它可以在字符串中查找匹配的模式，并将其替换为指定的字符串。
# 它使用了一个正则表达式模式和一个替换字符串，对字符串进行匹配和替换操作。
# 使用方法为:re.sub(pattern, repl, string, count=0, flags=0)
# re.sub()函数中的lambda函数的作用是替换字符串,m.group(1)表示获取第一个捕获组，即字符本身， m.group(0)表示获取整个字符串。

# import itertools
# text = input("请输入待压缩字符串:")
# string = []
# for key, group in itertools.groupby(text):
#     count = len(list(group))
#     if count < 3:
#         string.append(key * count)
#     else:
#         string.append(key + str(count))
# print("压缩后的字符串为:{} 压缩率：{:.2%}".format("".join(string),len(string)/len(text)))

# itertools.groupby()函数：
# 它是Python标准库中的一个函数，位于itertools模块中。
# 它可以对迭代器中的元素进行分组，并且每组元素按照关键函数返回值进行分组。
# 它使用了一个关键函数，按照该函数返回值进行分组，元素将被分组在一起，其关键函数返回值相同。
# 使用方法为:itertools.groupby(iterable, key=None)


