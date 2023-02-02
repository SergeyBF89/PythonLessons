# Задача 1. Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
"""
number = int(input('Введите трехзначное число: '))
summa = 0
while number > 0:
    x = number % 10
    summa += x
    number = number // 10
print(summa)
"""

# Задача 2. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
"""
crane = int(input('Введите количество журавликов: '))
name_k = (crane // 3) * 2
name_p = (name_k // 2) // 2
name_s = name_p
print(f'Количество журавликов Пети = {name_p}, количество журавликов Кати = {name_k}, количество журавликов Сережи = {name_s}')
"""

# Задача 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
"""
ticket_number = input('Введите номер биллета: ')
summa1 = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
summa2 = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
if summa1 == summa2:
    print('YES')
else:
    print('NO')
"""

# Задача 4. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
"""
n, m, k = [int(input()) for i in range(3)]
if k < n * m and (k % n == 0) or (k % m == 0):
    print('YES')
else:
    print('NO')
"""