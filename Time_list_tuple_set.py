# время выполнения цикла в списке-кортеже-множестве

from time import time
number = 15000
my_set = set(range(number))
my_list = list(range(number))
my_tuple = tuple(range(number))

t = time()
for i in range(number):
    if i in my_list:
        pass
print(f"Операция со списком: {time() - t} секунд")
my_list.clear()

t = time()
for i in range(number):
    if i in my_tuple:
        pass
print(f"Операция с кортежeм: {time() - t} секунд")

t = time()
for i in range(number):
    if i in my_set:
        pass
print(f"Операция со множеством: {time() - t} секунд")
my_set.clear()