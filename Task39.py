# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
#  Ввод: 					Вывод:
# 7					3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1			(каждое число вводится с новой строки)

#способ 1

'''
for i in test_list1:
    if i not in test_list2:
        list_res.append(i)
        
print(list_res)
'''

#способ 2
test_res = set(test_list1)-set(test_list2)
print(test_res)
[3, 1, 3, 4, 2, 4, 12]
{2, 3, 12}
for i in test_list1:
    if i in test_res:
        print(i)

'''
def list_diference(list_1, list_2):
    list_dif = list()
    for i in list_1:
        for j in list_2:
            if i == j:
                break
        else:
            list_dif.append(i)
    return list_dif
'''

def serch_dif(list_1: list[int], list_2: list[int]) -> list[int]:
    list_res = []
    for i in list_1:
        if i not in list_2:
            list_res.append(i)
    return list_res