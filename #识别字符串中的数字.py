#识别字符串中的数字
text = input("请输入一段字符串：")
num = "".join([i for i in text if i.isdigit()])
string = "".join([i for i in text if i.isalpha()])
print(f"数字为：{num} 数量：{len(num)}")
print(f"字符为：{string} 数量：{len(string)}")
if abs(len(num)-len(string)) > 1:
    print("字符串中数字和字母的数量不满足重新格式化的条件")
else:
    if len(num) > len(string):
        shoter = string
        longer = num
    else:
        shoter = num
        longer = string
    print("".join([longer[i]+shoter[i] for i in range(len(shoter))]))