from brain_games.engine import run_game
from brain_games.utils import get_random_num
from brain_games.consts import EVEN_INSTRUCTION


def is_even(num):
    return num % 2 == 0


def get_num_and_answer():
    num = get_random_num()
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer


def run_even_game():
    run_game(get_num_and_answer, EVEN_INSTRUCTION)