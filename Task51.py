'''
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

Ввод:							Вывод:
values = [0, 2, 10, 6]				same
if same_by(lambda x: x % 2, values):
	print(‘same’)
else:
	print(‘different’)
'''
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) in [0, 1]
    
    # return True if len(set(map(characteristic, objects))) == 1 else (True if len(set(map(characteristic, objects))) == 0 else False)


values = [0, 2, 10, 6]
# print('same' if same_by(lambda x: x % 2, values) else 'different')
if same_by(lambda x: x % 2, values):
	print('same')
else:
	print('different')