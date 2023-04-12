# Порядковый номер Числа Фибоначчи

n=int(input('Введите число: '))
f1=0
f2=1
fi=2

while f2 < n:
    f1, f2 = f2, f1 + f2
    fi +=1
if (f2==n):
    print(f'Номер {fi}')
else:
    print('Номер -1')
    