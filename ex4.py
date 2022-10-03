# 4.Реализуйте алгоритм перемешивания списка.
import random #решение из Семинара №3

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

list_shuffled =[]

for i in range(0, len(list)):
    j= random.ranrange(0, len(list))
    list_shuffled.append(list[j])
    list.remove(list[j])
print(list_shuffled)

exit()
#Перемешивание списка через .shuffle

import random

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a)
print(a)