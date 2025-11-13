import random

from brain_games.consts import (
    PRIME_INSTRUCTION,
    MAX_NUM,
    MIN_NUM
)
from brain_games.engine import run_game


def is_prime(num):
    if num <= 1:
        return False
    deviders_num = 0
    square_root = int(num ** 0.5)
    for i in range(2, square_root + 1):
        if num % i == 0:
            deviders_num += 1
    return deviders_num == 0


def get_num_and_answer():
    num = random.randint(MIN_NUM, MAX_NUM)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return num, correct_answer


def run_prime_game():
    run_game(get_num_and_answer, PRIME_INSTRUCTION)