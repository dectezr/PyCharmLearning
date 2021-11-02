# put your python code here
a = float(input())
b = float(input())
operation = input()
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '/':
    print(a / b if b != 0 else "Division by 0!")
elif operation == '*':
    print(a * b)
elif operation == 'mod':
    print(a % int(b) if b != 0 else "Division by 0!")
elif operation == 'pow':
    print(a ** b)
elif operation == 'div':
    print(a // int(b) if b != 0 else "Division by 0!")

# Better Solution
# from operator import add, sub, mul, truediv, mod, floordiv
# ops = {'+': add, '-': sub, '*': mul, '/': truediv, 'mod': mod, 'pow': pow, 'div': floordiv}
# lhs, rhs, op = float(input()), float(input()), input()
# try:
#     print(ops[op](lhs, rhs))
# except ZeroDivisionError:
#     print('Division by 0!')
