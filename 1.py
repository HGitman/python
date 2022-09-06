# 1. Напишите программу, которая принимает на вход цифру, 
#обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#6 -> Yes
#7 -> yes
#1 -> NO

 
day = int(input('Enter day: '))
if day > 7 or day < 1:
    print('Please, repeat the input')
elif day == 6 or day == 7:
    print("Yes, it's weekend!")
else:
    print("No, it's not weekend!")
