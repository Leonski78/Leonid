# print ("Введите трезначное число: ")
# n = int(input())
# if n>999 or n<100:
#     print ("Это не трехзначное число!")
# else:
#     sum = n//100 + n//10%10 + n%10
# print ("Сумма цифр числа равна: ")
# print (sum)
'''
my_arr = list('info'+'loop'+ '12')
print (my_arr)

my_arr = [1, 2, 3] * 2
print(my_arr)

a = set([1, 2, 3]) == set([3, 2, 1])
print(a)

s = "1" + "2"
print(s)

s = "python"
print(s[:-2])

t = [2, 3 , 4]
t.append((1, 5))
print(t)

#  не верно.  Кортеж не изменяемый:
# t = (2, 3 ,4)
# t.append((1, 5))
# print(t)

d = {1: 2, 3: 4}
print(len(d))

a = []
for i in range(3):
    a += [i]
print(a)

b = len({1: 2, 3: 4}) == len([1, 2])
print(b)

e = [1] + [2]
print(e)

e = [1, 45, 3, 5, 23][3] + 12
print(e)

# e = [1][1, 2] + 3
# print(e)

b = [(1, 2)] == (1, 2)
print(b)

a = [1, 2, 3]
a.extend([4, 5, 6, 7])
print(a)
'''


b = 5
def func(a):
    c = a % 2
    return c
b = func(b)
print(b)

def my_func(a=5, b=10):
    print(a, b)

my_func(3)

def my_func(*args, **kwargs):
    print(args, kwargs)

my_func()

def foo():
    print("foo")
foo()
def bar():
    print("bar")
bar()

b = [1, 2] == [2, 2]
print(b)

def func():
    a = 10
    return a
func()
print(func())