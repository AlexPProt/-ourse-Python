from random import randint

# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

list1=list()
a1=int(input("Введите первый элемент последовательности - "))
n=int(input("Введите кол-во элементов последовательности - "))
d=int(input("Введите коэфециент - "))

for i in range(1,n+1):
    list1.append(a1+(i-1)*d)
print (list1)


# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

n=int(input("Введите кол-во элементов массива - "))
n_lim=int(input("Введите максивальное значение элемента массива - "))
n_min=int(input("Введите нижний предел обработки значений - "))
n_max=int(input("Введите верхний предел обработки значений - "))

list1=[randint(1,100) for _ in range(n)]
print (f'Исходный массив {list1}')

list_rez=[i for i in range(0,len(list1)) if list1[i]>=n_min and list1[i]<=n_max]

print (f'Массив индексов соответсвующих гарницам поиска {list_rez}')


# colors=['red','green','black','yellow']
# data = open('file.txt','a')
# data.writelines(colors)
# data.close()

# def quck_sort (array):
#     if len(array)<=1:
#         return array
#     pivot=array[0]
#     less =[i for i in array[1:] if i<=pivot]
#     grater =[i for i in array[1:] if i>pivot]
#     return quck_sort(less) + [pivot] + quck_sort(grater)

# array=(9,5,1,23,64,42,45,75)
# print(quck_sort(array))
# print(array)

# num = int(input("Введите число - "))
# def posled(count:int):
#     if count==0:
#         return ""
#     char=input("-")
#     return (char+posled(count-1)+char)

# print(posled(num))

# num = int(input("Введите число - "))
# def chackNum (n : int) -> bool:
#     for i in range(2,n):
#         if n%i==0:
#             print(i, n%i)
#             return False
#         return True
# print (chackNum(num))

# list1=list()
# # for i in range(1,10):
# #     list1.append(randint(1,5))
# list1=[randint(1,5) for _ in range(10)]
# print (list1)
# def changeMinMax(listNum: list[int]) -> list[int]:
#     maxn=max(listNum)
#     minn=min(listNum)
#     print (minn, maxn)
#     return [mark if mark!=maxn else minn for mark in listNum]
# print (changeMinMax(list1))

# str1=[2,4,8]

# my_funct= lambda x : x%2==0

# def same_by(str1,funct):
#     new_l=list(filter(funct,str1))
#     if len(new_l)==len(str1):
#         return True
#     return False

# print(same_by(str1,my_funct))


# transformation = lambda x:x
# values=[2,4,5,7,6]
# transformated_values=list(map(transormation,lam))


# #  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# print ("Задание №1: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии")
# def stepen(a,b):
#     if b==0:
#         return 1
#     return a*stepen(a,b-1)
# num=int(input("Введите число для возведения в степень -"))
# step=int(input("Введите степень числа -"))
# print (stepen (num,step)) 
# print()

# # Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# #  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# print("Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.")
# print("Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.")
# num1=int(input("Введите первое число -"))
# num2=int(input("Введите первое число -"))
# def sumnum (a,b):
#     if (a+b)==0:
#         return 0
#     return 1+sumnum(a,b-1)

# print (sumnum (num1,num2)) 


# def fibonach(num):
#     if num==1:
#         return 1
#     if num==2:
#         return 2
#     return fibonach(num-1)+fibonach(num-2)
# print (fibonach(7))


# #  В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# # Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число 
# # ягод — на i-ом кусте выросло ai ягод.
# # В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит
# #  из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# # находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# # Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# # собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# num = int(input("Введитеткол-во кустов - "))
# bush=list()
# for i in range (0,num): #генерируем кол-во ягод на кусте
#     bush.append(randint(1,10))
# print (bush)
# tempmax=0
# totalmax=0
# for i in range(1,num):   #расчет сбора по каждому заходу и определение максимума
#     if i<num-1:
#         tempmax=bush[i-1]+bush[i]+bush[i+1]
#     else:
#         tempmax=bush[i-1]+bush[i]+bush[0]
#     if tempmax>totalmax:
#         totalmax=tempmax
#     print(totalmax,' ',tempmax)
# print(f'макисмальное кол-во ягод за один заход -{totalmax}')


# # Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# #Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
# #второго множества. Затем пользователь вводит сами элементы множеств.

# n1=int(input("Введите кол-во элементов первого списка -"))
# n2=int(input("Введите кол-во элементов второго списка -"))
# list1=[]
# list2=[]
# i=0
# for i in range(0,n1):
#     list1.append(randint(0,10))
# for i in range(0,n2):
#     list2.append(randint(0,10))
# print (list2)
# print (list1)
# set1=set(list1)
# set2=set(list2)
# print (set1)
# print (set2)
# reszset=set1.intersection(set2)
# print (reszset)




# import re
# text = "dasfasdfg,sfg saeg eegga  aegg"
# list1= text.split()
# print (list1)


# from string import ascii_uppercase
# from random import choice

# text=''.join([choice(ascii_uppercase+'0123456789') for _ in range (30)])
# print(text)
# array=[]
# rezstring=''
# print(type(array))
# k=0
# for i in text:
#     array.append(i)
#     if array.count(array[k])>1:
#         print(f'{array[k]}_{array.count(array[k])-1}',end=" ")
#         rezstring+=array[k]+'_'+str(array.count(array[k])-1)+' '
#     else:
#         print(array[k],end=" ")
#         rezstring+=array[k]+" "
#     k+=1
# print()
# print (rezstring)

# text="Вот текст с презентации:She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# i=0
# words=set()
# tempstr=''
# for i in range(0,len(text)):
#     if text[i]!='.' and text[i]!=' ' and text[i]!=':':
#         tempstr+=text[i]
#     else:
#         words.add(tempstr)
#         tempstr=''
# print(words)
# print("Кол-во слов в тексте - ",len(words))


# from string import ascii_uppercase
# from random import choice

# print(ascii_uppercase + '1234567890')

# new_line = ''.join([choice(ascii_uppercase + '1234567890') for _ in range(30)])
# print(new_line)

# dict_count = {}
# new_list = []

# for char in new_line:
#     if char in dict_count:
#         dict_count[char] += 1
#         new_list.append(f"{char}_{dict_count[char]}")
#     else:
#         dict_count[char] = 0
#         new_list.append(char)
# for ch in new_line:
#     dict_count[ch] = dict_count.get(ch, 0) + 1
#     if dict_count.get(ch) > 1:
#         new_list.append(f'{ch}_{dict_count.get(ch)-1}')
#     else:
#         new_list.append(ch)

# print(*new_list)

# input_string = "aaabcaadcdd"
# char_count = {}
# output = []

# for char in input_string:
#     if char in char_count:
#         char_count[char] += 1
#         output.append(f"{char}_{char_count[char]}")
#     else:
#         char_count[char] = 0
#         output.append(char)

# output_string = ' '.join(output)
# print(output_string)


# from flask import Flask
# app=Flask(__name__)

# @app.route('/')
# def main():
#     return "<h1>Hellow, world</h1><br><a href='/index'>перейти на 2ю страницу</a>"

# # @app.route('/index')
# # def index():
# #     return 'Its my first project'

# @app.route('/index/<x>/<y>')
# def index(x,y):
#     return f'Result - {int(x)+int(y)}'



# if __name__=='__main__':
#     app.run()




# my_dict= {1: "AEIOULNSTRАВЕИНОРСТ",2:"DGДКЛМПУ", 3:"BCMPБГЁЬЯ",4:"ЙFHVWYЫ",5:"KЖЗХЦЧ",8:"ШJXЭЮ",10:"QZФЩЪ"}
# print(type(my_dict))
# word=input("Введите слово дл обработки - ")
# word=word.upper()
# sum_scrabl=0
# print(sum([k for i in word for k,v in my_dict.items() if i in v]))


# for l in word:
#     for ind,nabor in my_dict.items():
#         for i in nabor:
#             if l==i: 
#                 sum_scrabl+=ind
# print (sum_scrabl)

# list_1 = [1, 3, 3, 9, 10,7,3,3,80]
# k = 0
# warm=abs(list_1[0]-k)
# temp=0
# for i in range(1,len(list_1)):
#     print (i)
#     if warm>abs(list_1[i]-k):
#         warm=abs(list_1[i]-k)
#         temp=i
# print (list_1[temp])



#Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# my_dict= {"V": "S001", "V": "S002", "VI": "S001","VI": "S005", "VII": "S005", " V ":" S009 ", " VIII":" S007 "}
# print(my_dict)
# outPut=set()
# for i in my_dict.values():
#     print(i)
#     outPut.add(i)
# print (type(outPut))
# print (outPut)




# from random import randint
# long=int(input('Введите длину списка -'))
# list1=[]
# print(list1)
# list2=set()
# for i in range(0,long):
#     list1.append(randint(0,10))
#     list2.add(list1[i])
# list3=set(list1)
# print(list1)
# print(list2)
# print(list3)
# print(len(list2))

# import random
# print(my_list:=[random.randint(0,5) for _ in range(int(input('Введите длину-')))])
# print(len(my_list))
# print(7%5)

#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# from random import randint
# quant = int (input("Введите кол-во монет - "))
# abvCoin=0
# revCoin=0
# for i in range(1,quant):
#     sideCoin = randint(0,1)
#     print(sideCoin, end=" ")
#     if sideCoin:
#         abvCoin+=1
#     else:
#         revCoin+=1
# print(("необходимо перевернуть ", {abvCoin}, "монет аверсом") if revCoin>abvCoin else ("необходимо перевернуть ", {revCoin}, "монет лежащих реверсом") )


# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# sumNum = int (input("Введите сумму чисел - "))
# prodNum = int (input("Введите произведение чисел - "))
# i=0
# j=0
# flag = False
# for i in range (0,sumNum+1):
#     if flag: break
#     for j in range (0,sumNum+1):
#         if (i+j==sumNum and i*j==prodNum):
#             print ("Загаданные числа -", i," ",j)
#             flag=True
#             break



# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# num = int(input("Введите число для обработки - "))
# doubleStep =1
# i=1
# while doubleStep<num:
#     print(doubleStep, end=" ")
#     doubleStep=2**i
#     i+=1



# Найдите сумму цифр трехзначного числа.
#num = int (input("Введите целое число для обработки -"))
#startNum = num
#count=10
#sum=0
#while num%count or num//count:
#    sum+=num%count
#    num//=count
#print('Сумма цифр в числе -',startNum,' составляет - ',sum)
#
#------------------------------------------------------------------------------------------
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа
# сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# # quant=int(input("Введите кол-во поделок сделанное детьми - "))
# # childKat = float(quant/3*2)
# # childPet = float(quant/3/2)
# # childSer=childPet
# # if childPet-int(childPet/1) and childKat-int(childKat/1):
# #     print ("Кол-во поделок некорректно")
# # else:
# #     print ("Кол-во поделок выполненое Катей - ",int(childKat))
# #     print ("Кол-во поделок выполненое Петей - ",childPet)
# #     print ("Кол-во поделок выполненое Сергеем - ",childSer)


    #-------------------------------------------------------------------------------------------
    # Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
    # билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма
    # первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
    # т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# ticketNum=int (input("Введите номер полученного билета - "))
# count=10
# razr=1
# while ticketNum//count>0:
#     razr=razr+1
#     count=count*10
# if razr%2:
#     print("Возможна проверка относительно среднего разряда")
# sumL=0
# sumR=0
# num=ticketNum
# print (razr%10)
# for i in range(1,razr//2+1):
#     sumR+=num%10
#     sumL+=num//10**(razr-(2*i-1))
#     num=num%10**(razr-(2*i-1))
#     num=num//10
#if sumL==sumR:
#    print('Ура, у Вас счастливый билет')
#else:
#    print("Повезет в следующий раз")

#--------------------------------------------------------------
# Вариант решение №1 как оказалось некорректно работает если первые знаки билета 0
# Этот вариант позволяет учитывать, но пришлось испльзовать массив

# ticketNum=str (input("Введите номер полученного билета - "))
# razr=int(len(ticketNum))
# if razr%2>0:
#     print("Возможна проверка относительно среднего разряда")
# sumL=0
# sumR=0
# for i in range(0,int(razr/2)):
#     sumL+=int(ticketNum[i])
#     sumR+=int(ticketNum[razr-i-1])
# if sumL==sumR:
#     print('Ура, у Вас счастливый билет')
# else:
#     print("Повезет в следующий раз")


#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку
# на два прямоугольника).
# n=int(input("Введите кол-во долек по ширине -"))
# m=int(input("Введите кол-во долек по длине -"))
# k=int(input("Введите желаемое кол-во долек -"))
# if (k%m==0 and k/m<n) or (k%n==0 and k/n<m):
#     print("Вы можете отломить ", k, " кусочков от плитка размером", m,"x",n)
# else:
#     print ("Такой отлом невозможен")


# Дополнительная задача - высокосный год
# year = int(input("Введите год для проверки на высокосность - "))
# if year%4!=0 or (year%100==0 and year%400!=0):
#     print("Введенный год, ", year, " не является высокосным")
# else:
#     print("Введенный год, ", year, " высокосный")


#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# num = int (input("Введите число для обработки - "))
# i=1
# temp=0
# temp1=0
# temp2=1

# while num>temp:
#     temp=temp2+temp1
#     temp1=temp2
#     temp2=temp
#     i+=1
#     print(temp)
# if num==temp:
#     print ("Введенное число принадлежит ряду фибоначи, его позиция", i)
# else:
#     print ("-1")

#Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель
#за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись
#исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
#Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
#Напишите программу, помогающую синоптикам в работе.

# from random import randint
# days = int(input("Введите кол-во дней для наблюдения - "))
# countTemp=0
# countMax=0
# dtemp=3
# i=0
# while i<days:
#     dtemp+=randint(-3,3)
#     print(dtemp,end=" ")
#     if dtemp>0:
#         countTemp+=1
#         if countMax<countTemp:
#            countMax=countTemp
#     else:
#         countTemp=0
#     i+=1
# print("мах послед температур - ", countMax)

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!

