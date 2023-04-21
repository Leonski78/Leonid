# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 2

# Output:  [4, 5, 1, 2, 3]

# Решения:
# List = [1, 2, 3, 4, 5]
# for i in range(len(List)):


my_list = [1, 2, 3, 4, 5, 7, 9]
k = 3
for i in range(k):
    my_list.insert(0, my_list.pop())
print(my_list)

# my_list = [1, 2, 3, 4, 5]
# k = 6 % len(my_list)

# print(my_list[-k:] + my_list[:-k])
