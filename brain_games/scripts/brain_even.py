import prompt
import random


MIN_NUM, MAX_NUM = 1, 150


def is_even(num):
    return num % 2 == 0


def run_even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_tries = 0

    while count_tries < 3:
        num = random.randint(MIN_NUM, MAX_NUM)
        correct_answer = 'yes' if is_even(num) else 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            count_tries += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
                f"Let's try again, {name}!")
            count_tries = 0

    print(f'Congratulations, {name}!')


def main():
    run_even_game()
    
    
if __name__ == "__main__":
    main()










