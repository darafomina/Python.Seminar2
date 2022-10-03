# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

number=(input("Введите число: "))  #самостоятельное решение
sum=0
for i in number:
    if i==","or i=="." :
        continue
    sum +=int(i)
print(sum)
exit()

#Примеры решения из Семинара №3
number=(input("Введите число: "))
sum=0
for i in number:
    if i.isdigit():
        sum+=int(i)
print(sum)

#Ещё один вариант решения:
number = (float(input("Введите число: ")))
sum = 0
number = abs(number)
def digit_after_dot_counter(num:float):
    count = 0
    div = 1
    while True:
        if not(num*div == int(num*div)):
            count += 1
            div *= 10
        else: break
    return count

num=number*(10**digit_after_dot_counter(number))
while num != 0:
    sum += num%10
    num //= 10
print(int(sum))






