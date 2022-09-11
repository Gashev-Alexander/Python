megicians=['alice','david','carolina']
for megician in megicians:
	print(megician)

	print(f"{megician.title()}, that was a great trick!")

	print(f"I can't wait to see your next trick, {megician.title()}.\n")
#Работа с циклами в списках. Обязательно надо использовать табуляцию, иначе программа будет работать некоректно.

print('Thank you, everyone. That was a great magic show!\n')
#При табулировании итогового сообщения- оно выводится для всех предыдущих сообщений

pizzas=['pepperoni','chease','diablo']
for pizza in pizzas:
	print(f"I loved {pizza.title()} pizza")
print(f"I realy love pizza")
#Задание 4.1 использование функции for


wilds=['leo','tiger','wolf']
for wild in wilds:
	print(f"A {wild.title()} would make a great pet")
print('Any of these animals would make a great pet!')
#Задание 4.2


for value in range(1,6):
	print(value)
#Смещение на 1, выводи не 123456 а 12345. Особенность python

numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)
#вывод чсиле с приращение +2

squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)
#Создание пустого списка с добавление в него числе возведенных во вторую степень

squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)


#>>> digits=[1,2,3,4,5,6,7,8,9,0]
#>>> min(digits)
#0
#>>> max(digits)
#9
#>>> sum(digits)
#Простая статистика с числовыми списками.


squares=[value**2 for value in range(1,11)]
print(squares)

#!!!!!!!!!!!!!ЗАДАНИЯ!!!!!!!!!!!!!!

for value in range(1,21):
	print(value)
#Задание 4.3 Вывод чисел от 1 до 20 включительно.

#Задание 4.4 создание списка чисел от 1 до 1000000
#Задание 4.5 вывод минимального, максимального и суммы чисел 1000000

even_numbers=list(range(1,21,2))
print(even_numbers)
#Задание 4.6 вывод нечетных чисел от 1 до 20

even_numbers=list(range(3,31,3))
print(even_numbers)
#Заданеи 4.7 создание списка чисел кратных 3. от 3 до 30

squares=[value**3 for value in range(1,11)]
print(squares)


players=['charles','martina','michael','florence','eli']
print(players[-3:])

print('Here are the first three players on my team:')
for player in players[:3]:
	print(player.title())

my_food=['pizza','falafel','carrot cake']
friend_food=my_food[:]
print("My favorite foods are:")
print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_food)
#Копирование списка

my_food.append('cannoli')
friend_food.append('ice cream')

print("My favorite foods are:")
print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_food)
#Копирование списка с добавление в отдельные списки новых данных

friend_pizzas=pizzas[:]
print(friend_pizzas)

pizzas.append('memfis')
friend_pizzas.append('bbq')

print("\nMy pizza list:")
print(pizzas)

print("\nFriend pizza list:")
print(friend_pizzas)

#!!!!!! Обязательное добавление [:] при копировании списка чтоб отделить
#                                   изначальные списки при добавлении 
#                                   новых элементов в раздельные списки\

print('My friend top pizza list:')
for friend_pizza in friend_pizzas[:2]:
	print(friend_pizza.title())

dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
	print(dimension)


print('Original dimensions:')
for dimension in dimensions:
	print(dimension)

dimensions=(400,100)
print('\nModified dimensions:')
for dimension in dimensions:
	print(dimension)



menus=("soup","fish","meat","vodka","lime")
print(menus)
print('Menu in my restoran:')
for menu in menus:
	print(menu)

menus=("tekkila","vodka","salo","fish","meat")
print("\nNew menu:")
for menu in menus:
	print(menu)

