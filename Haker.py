''' Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1'''

def change_rating(input_list):
    maxx = max(input_list)
    minn = min(input_list)

    for i in range(len(input_list)):
        if input_list[i] == maxx:
            input_list[i] = minn

    return input_list

print (change_rating([1, 3, 5, 2, 5]))