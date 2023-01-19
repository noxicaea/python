import random
import timeit

haystack = [random.randint(1, 10000000) for i in range(10000000)]
needles = [random.randint(1, 1000) for i in range(1000)]
haystack = set(haystack)
needles = set(needles)
# 请在此处添加一行代码，使得查找过程的执行效率提高 10000 倍以上。

def find():
    found = haystack & needles
    print(f"一共找到{len(found)}个匹配。")

t = timeit.timeit("find()", setup="from __main__ import find", number=1)
print(f"查找过程一共消耗{t}秒。")
