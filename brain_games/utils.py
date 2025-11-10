import random
from brain_games.consts import MIN_NUM, MAX_NUM, MATH_SIGNS, MIN_LENGTH, MAX_LENGTH


# Получение случайного числа
def get_random_num():
    num = random.randint(MIN_NUM, MAX_NUM)
    return num

# Получение случайной длины прогрессии и индекса для спрятанного элемента
def get_random_length_and_index():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    hidden_index = random.randint(0, length - 1)
    return length, hidden_index


# Получение случайного математического оператора
def get_math_sign():
    math_sign = random.choice(MATH_SIGNS)
    return math_sign