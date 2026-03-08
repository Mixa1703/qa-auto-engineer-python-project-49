import random

import prompt

from brain_games.cli import welcome_user


def even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    points = 0
    while points < 3:
        number = random.randint(1, 100)
        correct_answer = "yes" if number % 2 == 0 else "no"

        print(f"Question: {number}")
        answer = prompt.string("Your answer: ").lower()

        if answer == correct_answer:
            points += 1
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    even()


if __name__ == "__main__":
    main()
