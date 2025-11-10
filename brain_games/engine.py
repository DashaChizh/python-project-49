import prompt

from brain_games.consts import ROUNDS_NUM


def run_game(get_question_and_answer, game_instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    print(f'{game_instruction}')

    for _ in range(ROUNDS_NUM):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer.lower() == correct_answer:
            print('Correct!')            
        else:
            print(f"'{answer}' is wrong answer ;(. " 
                  f"Correct answer was '{correct_answer}'."
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')










