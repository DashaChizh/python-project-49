from brain_games.engine import run_game
from brain_games.utils import get_random_num, get_random_length_and_index
from brain_games.consts import PROGRESSION_INSTRUCTION


def get_progression_and_answer():
    length, hidden_index = get_random_length_and_index()
    step = get_random_num()
    start = get_random_num()
    
    progression_elements = []

    for i in range(length):
        value = start + i * step
        if hidden_index == i:
            progression_elements.append('..')
            answer = str(value)
        else:
            progression_elements.append(str(value))
        progression = ' '.join(progression_elements)

    return progression, answer


def run_progression_game():
    run_game(get_progression_and_answer, PROGRESSION_INSTRUCTION)