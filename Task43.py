# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:			Вывод:
# 1 2 3 2 3			2

list_start = [1, 2, 1, 2, 2, 4, 5]

def cnt_pair(lst: list[int]) -> int:
    cnt = 0
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[i] == lst[j]:
                cnt += 1
    return cnt

print(cnt_pair(list_start))

# 
def how_many_pairs(new_list):
    counter = 0
    for i in range(len(new_list) - 1):
        for j in range(i + 1, len(new_list)):
            if new_list[i] == new_list[j]:
                counter += 1
    return(counter)