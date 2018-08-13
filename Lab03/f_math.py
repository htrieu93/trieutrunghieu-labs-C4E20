import random as rd
import eval

y_n = ''

while y_n != 'STOP':
    x = rd.randint(1,10)
    y = rd.randint(1,10)
    ops = rd.choice(['+', '-' , '*', '/'])

    res = eval.calc(x, y, ops)
    ans = [res - 1, res, res + 1]
    ans_choice = rd.choice(ans)

    print('* ' * 10)
    print('{} {} {} = {}'.format(x, ops, y, ans_choice))
    print('* ' * 10)

    y_n = input('(Y/N)? ').upper()

    # if (y_n == 'Y') & (ans_choice == res):
    #     print('Yay', end = '')
    # elif (y_n == 'Y') & (ans_choice != res):
    #     print("You're wrong", end = '')
    # elif (y_n == 'N') & (ans_choice == res):
    #     print("You're wrong", end = '')
    # elif (y_n == 'N') & (ans_choice != res):
    #     print("Yay", end = '')

    if ans_choice == res:
        if (y_n) == 'Y':
            print("Yay", end = '')
        elif (y_n) == 'N':
            print("You're wrong", end = '')
    else:
        if (y_n) == 'Y':
            print("You're wrong", end = '')
        elif (y_n) == 'N':
            print("Yay", end = '')