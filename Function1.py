# -*- coding: utf-8 -*-

def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return 'x = ' + str(num1 - num2)
print(solve_eq('x + 4 = 9)'))