# -*- coding: utf-8 -*-

def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return 'x = ' + str(num2 - num1)
print(solve_eq('x + 4 = 9'))

def solve_eq2(equationn):
    num1, add, x, equal, num2 = equationn.split()

    num1, num2, = int(num1), int(num2)

    return 'x = ' + str(num2 -num1)
print(solve_eq2('2 + x = 9'))

