import random

from brain_games.consts import GCD_INSTRUCTION, MAX_NUM, MIN_NUM
from brain_games.engine import run_game


def get_nums_and_answer():
    num_1 = random.randint(MIN_NUM, MAX_NUM)
    num_2 = random.randint(MIN_NUM, MAX_NUM)
    a, b = num_1, num_2

    while b != 0:
        a, b = b, a % b 
    gcd_value = a

    return f'{num_1} {num_2}', str(gcd_value)


def run_gcd_game():
    run_game(get_nums_and_answer, GCD_INSTRUCTION)