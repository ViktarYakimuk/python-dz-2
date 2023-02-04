# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


n = float(input('Введите число-> '))
def summa(n):                            
   if float(n) < 0:                            
        x = float(n) * (-1)
   number = 0

   for i in str(n):
      if i != '.':
            number += int(i)
   return number

   
print(f'Сумма чисел равна {summa(n)}')