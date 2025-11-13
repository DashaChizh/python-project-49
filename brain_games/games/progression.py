import random

from brain_games.consts import (
    MAX_LENGTH,
    MAX_NUM,
    MIN_LENGTH,
    MIN_NUM,
    PROGRESSION_INSTRUCTION,
)
from brain_games.engine import run_game


def get_progression_and_answer():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    hidden_index = random.randint(0, length - 1)
    step = random.randint(MIN_NUM, MAX_NUM)
    start = random.randint(MIN_NUM, MAX_NUM)
    
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