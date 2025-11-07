import prompt
from brain_games.consts import ROUNDS_NUM


def run_game(get_question_and_answer, game_instruction):
    # Общая часть приветствия для всех игр
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    # Инструкции к игре. Для каждой игры свои правила. Присваивается как аргумент функции запуска игры.
    # И связан с функцией в скрипте. То есть идет переприсвоение аргументов. 
    print(f'{game_instruction}')

    count_tries = 0

    while count_tries < ROUNDS_NUM:
        # Получаем запрашиваемое число и правильный ответ
        # question - это цифра или выражение для вопроса игроку
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            count_tries += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
                f"Let's try again, {name}!")
            count_tries = 0

    print(f'Congratulations, {name}!')



''' import prompt
import random

MIN_NUM, MAX_NUM = 1, 10
OPERATION_SIGNS = ('+', '-', '*')

def get_correct_answer(num_1, num_2, oper_sign):
    match oper_sign:
        case "+":
            correct_answer = num_1 + num_2
        case "-":
            correct_answer = num_1 - num_2
        case "*":
            correct_answer = num_1 * num_2

    return str(correct_answer)


def run_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')

    count_tries = 0

    while count_tries < 3:
        num_1 = random.randint(MIN_NUM, MAX_NUM)
        num_2 = random.randint(MIN_NUM, MAX_NUM)
        math_sign = random.choice(MATH_SIGNS)


        print(f'Question: {num_1} {math_sign} {num_2}')
        correct_answer = get_correct_answer(num_1, num_2, math_sign)

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            count_tries += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
              f"Let's try again, {name}!")
            count_tries = 0

    print(f'Congratulations, {name}!')

run_game() '''











