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
        