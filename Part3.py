bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
#[Цифра] присвоение индекса в списке
#[0] выводит только первый в списке элемент
#[1] [2] [3] выводят последующие по очередности элементы

bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0].title())

# ИНДЕКСЫ НАЧИНАЮТСЯ С 0, А НЕ С 1

bicycles=['trek','cannondale','redline','specialized']
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
#[-1] выводит последний элемент в списке
#[-2] выводит предпослений элемент в списке и т.д.

bicycles=['trek','cannondale','redline','specialized']
message=f"My first bicycle was a {bicycles[0].title()}."
print(message)
#Использовние F строки для построения сообщения содержащего значение из списка

names=['adele','sasha','viktor','tanya','olga']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
#Задание 3.1 создание списка имен и вывод каждого имени по отдельности

names=['adele','sasha','viktor','tanya','olga']
message0=f"Hello {names[0].title()}! \nHow do you do?"
message1=f"\nMy name is {names[1].title()}. \nI'm is student GeekBrains"
message2=f"\n{names[2].title()} like drink is Coca-Cola!"
print(message0,message1,message2)
#Задание 3.2 Вывод сообщение с использование имен из списка

motocycles=['honda','yamaha','suzuki']
messagemoto1=f'"I wanna buy {motocycles[1].title()}!"'
print(messagemoto1)
#Задание 3.3 Использование списка для вывода утверждения.

motocycles1=['honda','yamaha','suzuki']
motocycles1[0]='ducati'
print(motocycles1)
#Изменение элементов в списке

motocycles2=['honda','yamaha','suzuki']
motocycles2.append('ducati')
print(motocycles2)
#Применение метода append() для добавление жлемента в список

moto=[]
moto.append('honda')
moto.append('yamaha')
moto.append('suzuki')
print(moto)
#Добваление элементов в список

moto1=['honda','yamaha','suzuki']
moto1.insert(0,'ducati')
print(moto1)
#Добавление нового элемента в произвольную позицию списка

moto2=['honda','yamaha','suzuki']
del moto2[0]
print(moto2)
#Удаление эелемна из списка, удаленный элемент становится недоступен.

moto3=['honda','yamaha','suzuki']
popped_moto3=moto3.pop()
print(moto3)
print(popped_moto3)
#Удаление элемента из списка методом pop(), позволяет использовать эелемент после удаления.

moto4=['honda','yamaha','suzuki']
last_owned=moto4.pop()
print(f"The last motocycle I owned was a {last_owned.title()}.")
#Список в хронологическом порядке, вывод сообщения с использованием посленего в списке элемента.

moto5=['honda','yamaha','suzuki']
first_owned=moto5.pop(0)
print(f"The firts motocycle I owned was a {first_owned.title()}.")
#Извлечение элементов из произвольной позиции pop(число)

#После каждого вызова pop() элемент, с которым вы работаете, уже не находится в списке.
#Если вы собираетесь просто удалить элемент из списка, никак не используя его, выбирайте команду del.
#Если вы намерены использовать элемент после его удаления из, выбирайте метод pop().

moto6=['honda','yamaha','suzuki','ducati']
moto6.remove('ducati')
print(moto6)
#Удаление элементов по значению.

moto7=['honda','yamaha','suzuki','ducati']
too_expensive='ducati'
moto7.remove(too_expensive)
print(moto7)
print(f"\nA {too_expensive.title()} is too expensive for me.")
#Удаление элемента из спииска с выводом причины.


#!!!!!!!!!!ЗАДАНИЯ!!!!!!!!!!


guests=['adele','olga','tanya']
vip1=f"Hello! {guests[0].title()} go to in my home?"
vip2=f"Hi {guests[1].title()}! Maybe I cooking lanch?"
vip3=f"Hello {guests[2].title()}! How are you?"
print(vip1)
print(vip2)
print(vip3)
#Задание 3.4 составление списка людей и написание сообщениея каждому из них.

too_expensive='olga'
guests.remove(too_expensive)
print(guests)
print(f"\nA {too_expensive.title()} didn't answer me.")
#Задание 3.5.1 удаление человека из списка с выводом причины удаления.

guests=['adele','oleg','tanya']
guests[1]='vadim'
print(guests)
#Задание 3.5.2 изменение списка 

vip1=f"Hello! {guests[0].title()} go to in my home?"
vip2=f"Hi {guests[1].title()}! Maybe I cooking lanch?"
vip3=f"Hello {guests[2].title()}! How are you?"
print(vip1)
print(vip2)
print(vip3)
#Задание 3.5.3 вывод сообщение с измененным ранее списком.

guests.insert(0,'albert')
guests.insert(3,'irina')
guests.append('rishat')
print(guests)
vip1=f"Hello! {guests[0].title()} go to in my home?"
vip2=f"Hi {guests[1].title()}! Maybe I cooking lanch?"
vip3=f"Hello {guests[2].title()}! How are you?"
vip4=f"Priv! {guests[3].title()} go to in theater?"
vip5=f"Holla {guests[4].title()}! Maybe I cooking coffe?"
vip6=f"Privet {guests[5].title()}! How are you man?"
print(vip1)
print(vip2)
print(vip3)
print(vip4)
print(vip5)
print(vip6)
#Задание 3.6 довабление людей в список и написание сообщения каждому человеку.

first_owned=guests.pop()
print(f"Please sorry me {first_owned.title()}.")
print(guests)
first_owned=guests.pop()
print(f"Please sorry me {first_owned.title()}.")
print(guests)
first_owned=guests.pop()
print(f"Please sorry me {first_owned.title()}.")
print(guests)
first_owned=guests.pop()
print(f"Please sorry me {first_owned.title()}.")
print(guests)
#Задание 3.7.1 и 3.7.2 сокращение списка людей с выводом сообщение об извенениях.

vip1=f"Hello! {guests[0].title()} go to in my home?"
vip2=f"Hi {guests[1].title()}! Maybe I cooking lanch?"
print(vip1)
print(vip2)
#Задание 3.7.3 отправки сообщений оставшимся участникам списка

del guests[1]
del guests[0]
print(guests)
#Задание 3.7.4 Удаление оставшихся двух участников и проверка списка на отсутвие людей в списке.

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#Сортировка в алфавитном порялке

cars.sort(reverse=True)
print(cars)
#Сортировка в обратном порядке

cars1=['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars1)

print('\nHere is the sorted list:')
print(sorted(cars1))

print('\nHere is the original lisd again:')
print(cars1)
#Использование временной сортировка используя функцию sorted()

print(cars1)
cars1.reverse()
print(cars1)
#вывод списка в обратном порядке используя функцию reverse()

len(cars)
#Определение длины списка используя функцию len(). Длина списка подсчитывается с 1.


#!!!!!!!!!ЗАДАНИЯ!!!!!!!!!!


mir=['russia','china','japan','mexico','tukey']
print(mir)
print(sorted(mir))
#временная сортировка в алфовитном порядке

print(mir)
print(sorted(mir, reverse=True))
#временная сортировка в обратном алфовитному порядку

print(mir)
mir.reverse()
print(mir)
mir.reverse()
print(mir)
mir.sort()
print(mir)
mir.sort(reverse=True)
print(mir)
#Задание 3.8 осортировка списков

#Задание 3.9 использование функции len() для посчета количества элементов в списке

#Задание 3.10 использование всех функции описанных в главе в месте на нескольких списках