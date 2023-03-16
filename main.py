def calk1(a, b):
    return a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk1, 5, 45)  # Мы можем передавать функции в функции


# ЛЯМБДА ФУНКЦИИ

calk1 = lambda a,b: a+b  # Сокращение функции по сравнению с прошлым примером

math(lambda a,b: a + b, 5, 45)  # Так можно выразить функцию ещё короче

# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа)

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)


def select(f, col):  # решение с помощью лямда функции
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(select(lambda x: (x, x**2), res))


list_1 = [x for x in range(1, 20)]  # решение с помощью функции map

list_1 = list(map(lambda x: x + 10, list_1))


# С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
# этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

data = '15 156 96 3 5 8 52 5'
data = list(map(int, data.split()))


ФУНКЦИЯ filter. Принимает на вход 2 аргумента: сама функция и объект. Возвращает только те элементы объекта,
для которых вызов функции возвращает значение true.

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5))


# Функция zip применяется к набору инерируемых объектов и возвращает итератор с кортежами из элементов входных данных.

zip ([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't'])
[(1, 'О', 'f'), (2, 'д', 's'), (3, 'т', 't')]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# пробегает по минимальногму входящему набору:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids), salary)
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)


# Функция enumerate применяется к итерируемому объекту и возвращает новый
# итератор с кортежами из индекса и элементов входных данных.

enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])

# функция enumerate позволяет пронумеровать набор данных.

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3')]
