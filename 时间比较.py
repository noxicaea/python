times = [1, 3, 3.5, 6.5, 9.5, 10, 10.8]
names = ["A", "B", "C", "D", "E", "F", "G"]
time_1 = [round(times[i]-times[i-1],2) for i in range(1,len(times))]
time_1.insert(0, times[0])
list_1 = list(zip(time_1, names))
print(list_1)
time_min = min(time_1)
time_max = max(time_1)
print(f"速度最快：{[i[1] for i in list_1 if i[0] == time_min]}，耗费时间：{time_min}")
print(f"速度最慢：{[i[1] for i in list_1 if i[0] == time_max]}，耗费时间：{time_max}")



#答案

# times = [1, 3, 3.5, 6.5, 9.5, 10, 10.8]
# names = ["A", "B", "C", "D", "E", "F", "G"]

# max_name = [names[0]]
# min_name = [names[0]]
# max_time = times[0]
# min_time = times[0]

# for i in range(1, len(names)):
#     each_name = names[i]
#     each_time = times[i] - times[i-1]

#     if each_time > max_time:
#         max_name.clear()
#         max_name.append(each_name)
#         max_time = each_time
#     elif each_time == max_time:
#         max_name.append(each_name)
#     elif each_time < min_time:
#         min_name.clear()
#         min_name.append(each_name)
#         min_time = each_time
#     elif each_time == min_time:
#         min_name.append(each_name)

# print(f"速度最快的是：{min_name}，耗费时间是：{min_time}")
# print(f"速度最慢的是：{max_name}，耗费时间是：{max_time}")
