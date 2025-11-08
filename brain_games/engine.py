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
            print(f"'{answer}' is wrong answer ;(. " 
                  f"Correct answer was '{correct_answer}'."
                  f"Let's try again, {name}!")
            count_tries = 0

    print(f'Congratulations, {name}!')










