﻿# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег. 
# Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек. 
# Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков 
# В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка. 
# Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков. 
# В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника. 
# Программа должна вывести одно число - минимальное количество лодок, необходимое для переправки всех рыбаков на противоположный берег.


m = int(input("Введите максимальную массу, которую может выдержать лодка: "))
n = int(input("Введите количество рыбаков: "))
o = 0 # Создаем пустой счетчик с общей массой рыбаков
l = 0 # Счетчик лодок

#if 1 <= m <= 10**6:
for p in range(n):
    mr = int(input("Введите массу рыбака: "))
    o += mr
# Нужно повторять цикл (n) количество раз. Числа введеные в (mr) нужно суммировать и добавить в переменную (o)
# Нужно что бы при привышении максимальной массы лодки (m), тикнул счетчик лодок (l)        
print(o)