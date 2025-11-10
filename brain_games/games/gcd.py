from brain_games.engine import run_game
from brain_games.utils import get_random_num
from brain_games.consts import GCD_INSTRUCTION


def get_nums_and_answer():
    num_1 = get_random_num()
    num_2 = get_random_num()
    a, b = num_1, num_2
    gcd_value = ''
  
    if b == 0 or a == b:
        gcd_value = a
    else:
        remainder = a % b
        while remainder != 0:
            remainder = a % b
            a = b
            b = remainder
            gcd_value = a

    return f'{num_1} {num_2}', str(gcd_value)


def run_gcd_game():
    run_game(get_nums_and_answer, GCD_INSTRUCTION)