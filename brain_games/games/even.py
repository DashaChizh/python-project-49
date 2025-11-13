import random

from brain_games.consts import EVEN_INSTRUCTION, MAX_NUM, MIN_NUM
from brain_games.engine import run_game


def is_even(num):
    return num % 2 == 0


def get_num_and_answer():
    num = random.randint(MIN_NUM, MAX_NUM)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer


def run_even_game():
    run_game(get_num_and_answer, EVEN_INSTRUCTION)