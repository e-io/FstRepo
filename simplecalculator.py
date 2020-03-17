# Простой калькулятор
# Предназначается для операций в одно действие

x = float(input())
y = float(input())
# o - operator
o = str(input())
# a - answer
a = 0.

if o == '+':
    a = x + y
elif o == '-':
    a = x - y
elif (o, y) == ('/', 0.):
    a = 'Деление на 0!'
elif o == '/':
    a = x / y
elif o == '*':
    a = x * y
elif (o, y) == ('mod', 0.):
    a = 'Деление на 0!'
elif o == 'mod':
    a = x % y
elif o == 'pow':
    a = x ** y
elif (o, y) == ('div', 0.):
    a = 'Деление на 0!'
elif o == 'div':
    a = x // y

print(a)
