from brain_games.engine import run_game
from brain_games.utils import get_random_num, get_math_sign
from brain_games.consts import CALC_INSTRUCTION




def get_math_expression_and_answer():
    num_1 = get_random_num()
    num_2 = get_random_num()
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
    










