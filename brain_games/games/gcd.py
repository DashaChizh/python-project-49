from brain_games.consts import GCD_INSTRUCTION
from brain_games.engine import run_game
from brain_games.utils import get_random_num


def get_nums_and_answer():
    num_1 = get_random_num()
    num_2 = get_random_num()
    a, b = num_1, num_2

    while b != 0:
        a, b = b, a % b 
    gcd_value = a

    return f'{num_1} {num_2}', str(gcd_value)


def run_gcd_game():
    run_game(get_nums_and_answer, GCD_INSTRUCTION)