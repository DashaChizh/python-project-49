import random
from brain_games.consts import MIN_NUM, MAX_NUM, MATH_SIGNS

# Получение случайного числа
def get_random_num():
    num = random.randint(MIN_NUM, MAX_NUM)
    return num


# Получение случайного математического оператора
def get_math_sign():
    math_sign = random.choice(MATH_SIGNS)
    return math_sign