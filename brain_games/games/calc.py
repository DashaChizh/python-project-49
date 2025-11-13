import random

from brain_games.consts import CALC_INSTRUCTION, MATH_SIGNS, MAX_NUM, MIN_NUM
from brain_games.engine import run_game


def get_math_sign():
    math_sign = random.choice(MATH_SIGNS)
    return math_sign


def get_math_expression_and_answer():
    num_1 = random.randint(MIN_NUM, MAX_NUM)
    num_2 = random.randint(MIN_NUM, MAX_NUM)
    math_sign = get_math_sign()
    math_expression = f'{num_1} {math_sign} {num_2}'

    match math_sign:
        case "+":
            correct_answer = num_1 + num_2
        case "-":
            correct_answer = num_1 - num_2
        case "*":
            correct_answer = num_1 * num_2

    return math_expression, str(correct_answer)


def run_calc_game():
    run_game(get_math_expression_and_answer, CALC_INSTRUCTION)
    










