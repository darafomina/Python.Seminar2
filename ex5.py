# 5. Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


n = int(input("Введите число: "))
fib1 = fib2 = 1
print(fib1, fib2, end=' ')
list1= [1, 1]
list2=[0]
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
    list1.append(fib2)
for i in range(len(list1)):
    if i%2!=0 and i!=0:
        elem = list1[i]*-1
    else:
        elem = list1[i]
    list2.insert(0, elem)      
print(list2)   
list3 = list2 + list1
print(list3)