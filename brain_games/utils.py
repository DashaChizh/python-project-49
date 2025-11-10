import random

from brain_games.consts import (
    MATH_SIGNS,
    MAX_LENGTH,
    MAX_NUM,
    MIN_LENGTH,
    MIN_NUM,
)


def get_random_num():
    num = random.randint(MIN_NUM, MAX_NUM)
    return num


def get_random_length_and_index():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    hidden_index = random.randint(0, length - 1)
    return length, hidden_index


def get_math_sign():
    math_sign = random.choice(MATH_SIGNS)
    return math_sign