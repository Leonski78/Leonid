# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем 
# (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. 
# Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

list = []
number = None
while number != 0:
    number = int(input("Введите число: "))
    list.append(number)
print(max(list))

# 
maxx = -1
while (number:=int(input("Введите число: "))) != 0:
    if number > maxx:
        maxx = number

print(maxx)
# 
n = int(input())
nMax = n

while n != 0:
    n = int(input())
    if n > nMax:
        nMax = n

print(nMax)