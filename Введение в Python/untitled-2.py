'''
a=int(input())
if a%2==0:
	print('Число четное')
else:
	print('Число нечетное')
'''
'''
a=input().split('-')
#print(type(a))
if a[0]==a[1]:
	print('Строки равны')
else:
	print('Строки содержат разное количество символов')
'''
'''
a=int(input())
l=False
if a%400==0:
	l=True
elif not(a%100==0) and (a%4==0):
	l=True
if l:
	print('Високосный')
else:
	print('Обычный')
'''

'''
n = int(input())
print(('Это число не 1, 2, 3', 'Один', 'Два', 'Три')[n * (str(n) in '123')])	
'''
'''
a=int(input())
while a<=100:
	if a>10:
		print(a)
	a=int(input())
'''

'''
a=int(input())
while a<=100:
	if a<10:
		a=int(input())
		continue
	if a>100:
		break
	print(a)
	a=int(input())
'''

'''
a=input()

c=len(a)
#print(c)
b=a[::-1]
print(b)
print(a)
print('Число символов в строке:',a,'=',c)
'''

'''
a=int(input())
for i in range(a):
	print(int(i*i), end='.')
'''
'''
a=input()
k=0
for i in a:
	print(f'{k}-{i}',end=' ')
	k=k+1
'''
'''
a,b=map(int,input().split())
s=0
for i in range(a,b+1):
	#print(i)
	if int(i%2)==0:
		s=s+i
print(s)
'''

'''
# Числа Фибоначчи

arr = [1, 1]
print(arr[0])
while True:
	print(arr[-1])
	if arr[-1] == 21:break
	tmp = sum(arr)
	arr.append(tmp)
	del arr[0]
'''

#students = ['Ivan', 'Masha', 'Sasha']

'''

M[1]                        # Получить строку 2: [4, 5, 6]
M[1][2]  # Получить строку 2, а затем элемент 3 в этой строке: 6
М          # возвращает весь список [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in M] # Выбирает элементы второго столбца [2, 5, 8]
col1 = [row[0] for row in M] # Выбирает элементы первого столбца [1, 4, 7	

'''

'''
a=[1,2,3]
b = a
print(b)
a[1]=10
print(b)
b[0]=20
print(a)
print(b is a)
a=[5,6]
print(b)
print(b is a)
'''

'''
a=list(input().split())
for i in a[::-1]:
	print(i,end=' ')
'''
'''
# генератор списка, ввод целых чисел в одной строке через пробел
a=[int(i) for i in input().split()]
# условие: если длина введенной строки больше, чем один элемент (символ)
if len(a)>1:
# цикл, с реализацией перебора элементов по индексу: от первого до числа, равного длине введенной строки
for i in range(len(a)):
# вывод суммы соседних элементов в строку через пробел
print(a[i-1]+a[i+1-len(a)], end = “ “)
# иначе, если условие не выполнено, т.е. введено одно число, вывод этого числа
else:
print(a)
'''



'''
n=int(input())
b=[]
for i in range(n):
	b.append(i**2)
print(b)
c=[]
for i in range(n):
	print(b[i+1-n]+b[i-n],end=' ')
	c.append(b[i+1-n]+b[i-n])
'''

'''
b=int(input())
arr = [1, 1]
print(arr[0],end=', ')
k=0
while True:
	print(arr[-1],end=', ')
	tmp = sum(arr)
	#print(tmp)
	if (b-4)<k:
		print(tmp)
		break
	arr.append(tmp)
	k=k+1
	del arr[0]
'''

'''
a=set(input().split())
b=set(input().split())
print(a&b)
'''

'''	
a = [i for i in input().split()]
print(type(a))
b = set(a)
print(b)
print(*b)   #Здесь оператор * — не просто синтаксический сахар. Без фиксированной длины списка было бы невозможно передать элементы итерируемого объекта как отдельные аргументы, не используя *.
'''



'''
d = {}
d = dict(ключ_1='значение_1', ключ_2='значение_2’)
d = dict([(1, 1), (2, 4)])
d = dict.fromkeys(['a', 'b'], 50)
d = {a: a ** 2 for a in range(7)}
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
создание пустого словаря с помощью литерала
c помощью функции dict()
внутри списка кортежи из ключей и значений: {1: 1, 2: 4}
с помощью метода fromkeys: {'a': 50, 'b': 50}
с помощью генератора словарей: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
c помощью функции zip(): {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
'''



'''
a=int(input())
dict={}
for i in range (a):
	b,b1=input(str()).split()
	dict[b]=b1
	dict[b1]=b
print(dict[input()])
'''

'''
a = list(input().lower().split())  # создание списка всех слов без учета регистра
a_set = set(a)                     # создание множества всех уникальных слов
for i in a_set:                    # цикл по значениям множества всех уникальных слов
	print(i, a.count(i))           # печать уникальных слов и их количества
'''

'''
f = open('family.txt', 'w')
f.write('Кочнов')
f.write('Захар Павлович')
f.close()
f = open('family.txt')
f.read()
'''

'''
with open('family_1.txt', 'w') as f:
	f.write('Кочнов ')
	f.write('Захар Павлович')
	f.close
f = open('family_1.txt')
f .read()
'''

'''
def modify_list(l):
	b = []
	for x in l:
		if x % 2 == 0:
			b.append(x // 2)
		l = b
	return l
lst = [int(i) for i in input().split()]
mod_lst=modify_list(lst)
print(*mod_lst)
'''

'''
# Числа Фибоначчи
def fibo(x):
	arr = [1, 1]
	
	#print(arr[0])
	for i in range(x-1):
		#print(arr[-1])
		#if arr[-1] == x:break
		tmp = sum(arr)
		arr.append(tmp)
		del arr[0]
	return arr[0]
print(fibo(10))
'''

'''
#Комментирование кода

class Shark: #создание класса

	def swim(self): #определение функции
		print("The shark is swimming.") #печать "The shark is swimming."

	def be_predator(self): #определение функции
		print("The shark is a predator.") #печать "The shark is a predator."
a=Shark()
a.swim()
a.be_predator()
'''

'''

class Table: #создание класса Table

	def __init__(self, l, w, h, c): #создание метода класса Table с помощью конструктора объектов класса

		self.length = l # атрибут класса: length

		self.width = w # атрибут класса: width

		self.height = h # атрибут класса: heigh

		self.color = c # атрибут класса: color

class KitchenTable(Table): #создание дочернего класса KitchenTable

	def setPlaces(self, p): #создание метода класса: setPlaces

		self.places = p # частный атрибут класса KitchenTable: places

		print("Количество посадочных мест кухонного стола = ", p) #вывод на печать

class DeskTable(Table):   #создание дочернего класса DeskTable

	def square(self): #создание метода класса: square

		print("Площадь письменного стола = ", "%.2f" % (self.width * self.length)) #вывод на печать

t1 = KitchenTable(2, 2, 0.7, "орех") #создание экземпляра дочернего класса KitchenTable, с заданными атрибутами

t2 = DeskTable(1.5, 0.8, 0.75, "ольха") #создание экземпляра дочернего класса DeskTable,  с заданными атрибутами

t2.square() # запрос метода square

t1.setPlaces(5) # запрос метода setPlaces

print("Цвет кухонного стола: ", t1.color) #вывод на печать 

print("Цвет письменного стола: ", t2.color) #вывод на печать 
'''


'''
import numpy
a=[1,2,3]
b=[4,5,6]

c=numpy.array([a,b])
print('Массив:\n',c)
'''

'''
import numpy
a=numpy.eye(4,4,k=0,dtype=int)
print(a)
'''

'''
import numpy
a=numpy.zeros((8),dtype=int)
print(a)
'''
'''
import numpy
a=numpy.zeros((8,1),dtype=int)
print(a)
'''

'''
import numpy
a=numpy.full((2,2),5.0)  #a=numpy.full((2,2),5,dtype=float) 
print(a)
'''

'''
import random
import numpy
a=[1,2,3,4,5,6,7,8]

def sample(b):
	i, j = random.sample(range(0, len(b)), 2)
	prom=b[i]
	b[i]=b[j]
	b[j]=prom
	return b

for i in range(3):
	a=sample(a)
	
print(a)
'''


'''
import numpy

Z = numpy.ones((5,5),dtype=int)
Z[1:-1,1:-1] = 0
print(Z)
'''

'''
import numpy

Z = numpy.zeros((5,5),dtype=int)
Z[1:-1,1:-1] = 1
print(Z)
'''

'''
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
b=a.min(axis=None)
c=a.max(axis=None)
d=a.mean(axis=None)
f=a.std(axis=None)
m=a.argmin(axis=None)
l=a.argmax(axis=None)
print(b,c,d,f,m,l)
'''

import numpy
a=numpy.array([[5,9,1],[8,17,55],[44,91,3]])
minim=a.min(axis=None)
minim_X=a.min(axis=0) #вдоль столбцов
maxim=a.max(axis=None)
maxim_X=a.max(axis=0) #вдоль столбцов
sredn=a.mean(axis=None)
sredn_X=a.mean(axis=0) #вдоль столбцов
otklon=a.std(axis=None)
otklon_X=a.std(axis=0) #вдоль столбцов
min_index=a.argmin(axis=None)
max_index=a.argmax(axis=None)
print('Минимальное значение в массиве',minim)
print('Минимальное значение по оси X',minim_X)
print('Максимальное значение в массиве',maxim)
print('Максимальное значение по оси X',maxim_X)
print('Среднее значение в массиве',sredn)
print('Среднее значение по оси X',sredn_X)
print('Отклонение значение в массиве',otklon)
print('Отклонение значение по оси X',otklon_X)
print('Индекс минимального значения в массиве',min_index)
print('Индекс максимального значения в массиве',max_index)

