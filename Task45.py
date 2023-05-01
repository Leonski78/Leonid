# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284

# def sum_del(n):
#     result = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             result += i
#     return result
            
# def func(k: int):
#     for i in range(2, k):
#         if i == sum_del(i):
#             print(f'{i} {sum_del(i)}')
        
# k = 300
# func(k)

'''
def get_divisors_sum(n):
    return sum([i for i in range(1, n) if n % i == 0])


k = int(input('Введите число k: '))
amicable_pairs = []

for i in range(1, k):
    for j in range(i + 1, k):
        if get_divisors_sum(i) == j and get_divisors_sum(j) == i:
            amicable_pairs.append((i, j))

 '''

def find_sum_delitel(num: int) -> int:
    summ = 0
    for i in range(1, num // 2 +1):
        if (num % i == 0):
            summ += i
    return summ

k = int(input('Введите число: '))

for num_1 in range(2, k):
    num_2 = find_sum_delitel(num_1)

    if (find_sum_delitel(num_2) == num_1) and (num_1 < num_2):
        print (num_1, num_2)

'''
def summarize(number, sum=0):
    for item in range(1, number//2+1):
        if number % item == 0:
            sum += item
    return sum

k = 10000
print(my_list := [i for i in range(k)])
lst = list()

for i in range(len(my_list)):
    item = my_list[i]
    sum1 = summarize(item)
    sum2 = summarize(sum1)
    if (sum2 == item) and (item < sum1):
        print(item, sum1)
        lst.append((item, sum1))
print(lst)
''''''