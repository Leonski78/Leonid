# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

# Input: 5

# Output: yes

def simple(num):
    for i in range (2, num//2 + 1):
        if (num%i == 0):
            return False
    return True

N = int(input("Введите число:"))
print(simple(N))

# 
def f(some_list=None):
    if some_list is None:
        some_list = []
    some_list.append(2)
    print(some_list)