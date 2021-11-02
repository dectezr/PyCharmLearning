import math
import argparse


def args_check_preprocessing(args):
    flag = True
    if args.type not in ["annuity", "diff"]:  # 类型检查
        flag = False
    if args.type == 'diff' and args.payment:  # 变率计算不能给定每期付款
        flag = False
    if not args.interest:  # 利率不可缺少
        flag = False
    if not ((args.payment or args.principal) and (args.principal or args.periods) and (args.periods or args.payment)):
        # 三个变量中只允许一个变量为空，不可以有两个以上为空
        # 两个以上为空则必然出现某一个or为None，从而and为None，判断式为真
        flag = False
    if args.payment and args.principal and args.periods:
        # 三个变量不能全部为满
        flag = False
    if not flag:  # 检查失败
        print('Incorrect parameters.')
        exit(1)
    # 接下来进入正负检查和预处理
    loan_interest = float(args.interest) / (100.0 * 12.0)
    if loan_interest < 0:
        flag = False
    if not args.payment:
        monthly_payment = 0
        loan_principal = float(args.principal)
        number_of_periods = float(args.periods)
        if args.type == 'annuity':
            action = 'a'
        elif args.type == 'diff':
            action = 'd'
    elif not args.principal:
        monthly_payment = float(args.payment)
        loan_principal = 0
        number_of_periods = float(args.periods)
        action = 'p'
    elif not args.periods:
        monthly_payment = float(args.payment)
        loan_principal = float(args.principal)
        number_of_periods = 0
        action = 'n'
    if monthly_payment < 0 or loan_principal < 0 or number_of_periods < 0:
        # 出现任何非负项
        flag = False
    if not flag:  # 检查失败
        print('Incorrect parameters.')
        exit(2)
    number_of_periods = int(number_of_periods)
    return action, monthly_payment, loan_principal, number_of_periods, loan_interest


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()
action, monthly_payment, loan_principal, number_of_periods, loan_interest = args_check_preprocessing(args)
overpayment = -loan_principal

if action == 'd':
    for i in range(1, number_of_periods + 1):
        monthly_payment = math.ceil(loan_principal / number_of_periods +
                                loan_interest * (loan_principal - loan_principal * (i - 1) / number_of_periods))
        print(f'Month {i}: payment is {monthly_payment}')
        overpayment += monthly_payment
    print()
if action == 'n':
    number_of_periods = math.ceil(math.log(monthly_payment / (monthly_payment - loan_interest * loan_principal),
                                           1 + loan_interest))
    overpayment += number_of_periods * monthly_payment
    years = number_of_periods // 12
    months = number_of_periods % 12
    dates = ''
    if years == 1:
        dates = dates + '1 year and '
    elif years != 0:
        dates = dates + f'{years} years and '
    if months == 0:
        try:
            dates = dates[0:-4]
        except IndexError:
            dates = 'no time '
    elif months == 1:
        dates = dates + '1 month '
    else:
        dates = dates + f'{months} months '
    print('It will take ' + dates + 'to repay this loan!')
elif action == 'a':
    power_result = math.pow((loan_interest + 1.0), number_of_periods)
    monthly_payment = math.ceil(loan_principal * loan_interest * power_result
                                / (power_result - 1))
    print(f'Your monthly payment = {monthly_payment}!')
    overpayment += number_of_periods * monthly_payment
elif action == 'p':
    power_result = math.pow((loan_interest + 1.0), number_of_periods)
    loan_principal = math.ceil(monthly_payment /
                               (loan_interest * power_result / (power_result - 1)))
    print(f'Your loan principal = {loan_principal}!')
    overpayment = number_of_periods * monthly_payment - loan_principal
print(f'Overpayment = {round(overpayment)}')

# Task 2
# print('Enter the loan principal:')
# loan_principal = int(input())
# print('''What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment:''')
# action = input()
# if action == 'm':
#     print('Enter the monthly payment:')
#     monthly_payment = int(input())
#     print()
#     numbers = math.ceil(float(loan_principal)/monthly_payment)
#     if numbers == 1:
#         print('It will take 1 month to repay the loan')
#     else:
#         print(f'It will take {numbers} months to repay the loan')
# elif action == 'p':
#     print('Enter the number of months:')
#     numbers = int(input())
#     if loan_principal % numbers == 0:
#         print(f'Your monthly payment = {loan_principal/numbers}')
#     else:
#         monthly_payment = math.ceil(float(loan_principal)/numbers)
#         print(f'Your monthly payment = {monthly_payment} and the last payment = {loan_principal - (numbers - 1) * monthly_payment}.')


# Task 3
# print('''What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:''')
# action = input()
# if action not in ['n', 'a', 'p']:
#     print('Wrong input! Please start again.')
#     exit()
# loan_principal = monthly_payment = number_of_periods = 0
# if action != 'p':
#     print('Enter the loan principal:')
#     loan_principal = float(input())
# if action != 'a':
#     print('Enter the monthly payment:')
#     monthly_payment = float(input())
# if action != 'n':
#     print('Enter the number of periods:')
#     number_of_periods = float(input())
# print('Enter the loan interest:')
# loan_interest = float(input()) / (12 * 100)
# if action == 'n':
#     number_of_periods = math.ceil(math.log(monthly_payment / (monthly_payment - loan_interest * loan_principal),
#                                            1 + loan_interest))
#     years = number_of_periods // 12
#     months = number_of_periods % 12
#     dates = ''
#     if years == 1:
#         dates = dates + '1 year and '
#     elif years != 0:
#         dates = dates + f'{years} years and'
#     if months == 0:
#         try:
#             dates = dates[0:-5]
#         except IndexError:
#             dates = 'no time '
#     elif months == 1:
#         dates = dates + '1 month '
#     else:
#         dates = dates + f'{months} months '
#     print('It will take ' + dates + 'to repay this loan!')
# elif action == 'a':
#     power_result = math.pow((loan_interest + 1), number_of_periods)
#     monthly_payment = math.ceil(loan_principal * loan_interest * power_result
#                                 / (power_result - 1))
#     print(f'Your monthly payment = {monthly_payment}!')
# elif action == 'p':
#     power_result = math.pow((loan_interest + 1), number_of_periods)
#     loan_principal = math.ceil(monthly_payment /
#                                (loan_interest * power_result / (power_result - 1)))
#     print(f'Your loan principal = {loan_principal}!')
