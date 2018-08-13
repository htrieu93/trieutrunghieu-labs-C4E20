from random import *
from eval import calc

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1, 10)
    y = randint(1, 10)
    op = choice(['+', '-', '*', '/'])
    err = [-1, 0, 1]

    result = calc(x, y, op) + choice(err)

    return([x, y, op, result])

def check_answer(x, y, op, result, user_choice):

    display_res = calc(x, y, op)     

    if result == display_res:
        return user_choice
    else:
        return not user_choice
        
            
