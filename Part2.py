print("hello_world")
#выводит сообщение

name="alex gashev"
print(name.title())
#выводит титульное имя
name="Alex Gashev"
print(name.upper())
#выводит все капсом
print(name.lower())
#ыводит все мелким шрифтом

first_name="alex"
last_name="gashev"
full_name=f"{first_name} {last_name}"
print(full_name)
#выводит имя с использование переменных F

first_name="alex"
last_name="gashev"
full_name=f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
#приветствие с переменной F

first_name="alex"
last_name="gashev"
full_name=f"{first_name} {last_name}"
message=(f"Hello, {full_name.title()}!")
print(message)
#присвоение переменной message имени через F

print("\tPython")
#Использование \t для отступа

print("Languages:\nPython\nC\nJavaScript")
#Использование \n для переноса текста на новую строку

print("Languages:\n\tPython\n\tC\n\tJavaScript")
#Совместное использование табуляции с переносом на новую строку \n \t

favorite_language='python '
favorite_language=favorite_language.rstrip()
favorite_language
#Запись усеченого значения в переменную для удаление лишнего пробела

print('python ')
favorite_language='python '
favorite_language=favorite_language.rstrip()
favorite_language
#Исключение пропуска из строки





#ЗАДАНИЯ

name="Eric"
print('Hello', name, ', would you like to learn some Python today?')
#Заданя 2.3 Имя пользователя в переменной с выводом сообщеняи для конкретного человека

name="eric cartman"
print(name.title())
print(name.upper())
print(name.lower())
#Заданя 2.4 Имя пользователя в переменной с выводом в нижнем регистре, в верхнем регистре и с капитализацией начальных букв каждого слова

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
#Заданя 2.5 Вывод цитаты с именем автора и ковычками

famous_person='Albert Einstein'
message='"A person who never made a mistake never tried anything new."'
print(famous_person, 'once said,', message)
#Заданя 2.6 сохранение имени автора и сообщение в отдельных переменных

famous_person1=' Albert Einstein '
favorite_language=' Albert Einstein '
favorite_language=favorite_language.strip()
message1='\n\t\t"A person who never made a mistake never tried anything new."'
print(famous_person1, '\n\tonce said:', message1)
favorite_language='python '
favorite_language=favorite_language.rstrip()
favorite_language
#Заданя 2.7 Использование переменных и \t и \n и удаление пробелов.

a=1
b=2
c=3
d=4
e=5
f=6
g=7
k=8
print(a+g)
print(c+e)
print(a+b+c+b)
print(((d+g-k+e)*2)/4+d)
#Заданя 2.8 и 2.9 зделано 16.08.2022

#Задание 2.10 добавление комментариев

#ДЗЕН PYTHON
#Красивое лучше, чем уродливое.
#Простое лучше, чем сложное.
#Сложное лучше, чем запутанное.
#Удобочитаемость имеет значение.
#Должен существовать один - и желательно тольео один - очевидный способ сделать это.
#Сейчас лучше, чем никогда.

#Задание 2.11 ввод команды import this в терминальном сеансе Python и просмотр всех принципов
#The Zen of Python, by Tim Peters
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!