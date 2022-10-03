# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число: ")) #разбор домашнего из Семинара 3
def factorial(n):
    listA = []
    buf = 1
    for i in range (1,n+1):
        listA.append(i*buf)
        buf*=i
    return listA
print (factorial(number))
