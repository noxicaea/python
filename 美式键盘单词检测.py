American_keyboard_1 = "qwertyuiop"
American_keyboard_2 = "asdfghjkl" 
American_keyboard_3 =  "zxcvbnm"
words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
# outs = []
# for word in words:
#     _ = []
#     for letter in word:
#         if letter.lower() in American_keyboard_1:
#             for letter in word:
#                 if letter.lower() in American_keyboard_1:
#                     _.append(letter)
#                 else:
#                     _.clear()
#             if len(_) == len(word):
#                 outs.append(word)
#         if letter.lower() in American_keyboard_2:
#             for letter in word:
#                 if letter.lower() in American_keyboard_2:
#                     _.append(letter)
#                 else:
#                     _.clear()
#             if len(_) == len(word):
#                 outs.append(word)
#         if letter.lower() in American_keyboard_3:
#             for letter in word:
#                 if letter.lower() in American_keyboard_3:
#                     _.append(letter)
#                 else:
#                     _.clear()
#             if len(_) == len(word):
#                 outs.append(word)
# print(outs)




# words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
# res = []
# for i in words:
# #由于单词存在大小写，所以这里统一先转换为小写字母
#    j = i.lower()
#   # 灵活运用 strip() 方法，判断 j 是否所有字符都在键盘的同一行内
#    if j.strip("qwertyuiop") == '' or j.strip("asdfghjkl") == '' or j.strip("zxcvbnm") == '':
#        res.append(i)
# print(res)



keyboard = [American_keyboard_1, American_keyboard_2, American_keyboard_3]
outs = [word for word in words if any(all(letter.lower() in row for letter in word) for row in keyboard)]
print(outs)

