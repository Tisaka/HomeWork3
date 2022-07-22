# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# 
# Пример:
# 
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

def num (n, frst, last):
    return [round(uniform(frst,last), 2) 
    for i in range(n)]

def f(my_nums):
    nums = [round(x - int(x), 2) for x in (my_nums)]
    return max(nums) - min(nums)
    
n = 5
frst = 1
last = 10
my_nums = num(n, frst, last)

print(f(my_nums))