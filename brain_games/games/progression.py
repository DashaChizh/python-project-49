from brain_games.engine import run_game
from brain_games.utils import get_random_num, get_random_length_and_index
from brain_games.consts import PROGRESSION_INSTRUCTION


def get_progression_and_answer():
    length, index = get_random_length_and_index()
    step = get_random_num()
    start = get_random_num()
    
    progression = ''

    for i in range(length):
        if index == i:
            answer = str(start + i * step)
            progres_element = '..'
        else:
            progres_element = str(start + i * step)
        progression = progression + ' ' + progres_element

    return progression, answer


def run_progression_game():
    run_game(get_progression_and_answer, PROGRESSION_INSTRUCTION)