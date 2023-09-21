print ("Привет это калькулятор в Python")
num_1 = = int (input('Введите число 1: '))
num_2 == int (input('Введите число 2: '))

act = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))
if act == 1:
   exmp = num_1 + num_2
    addition = 'сложения'
    res_op = addition
if act == 2:
    exmp = num_1 - num_2
    subtraction = 'вычитания'
    res_op = subtraction
if act == 3:
    exmp = float(num_1 / num_2)
    division = 'деления'
    res_op = division
if act == 4:
    exmp = num_1 * num_2
    multiplication = 'умножения'
    res_op = multiplication
print ('Результат ',res_op,' = ',exmp)