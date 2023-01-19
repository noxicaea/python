#奇偶排序
list_integers = [1, 8, 7, 3, 6, 5, 4, 2]
odd_number = sorted([i for i in list_integers if i % 2 == 1])
numbered = sorted([i for i in list_integers if i % 2 == 0])
print(odd_number + numbered)