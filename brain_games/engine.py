import prompt

from brain_games.cli import welcome_user


def run_game(rule, generate_round):
    name = welcome_user()
    print(rule)
    points = 0
    while points < 3:
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").lower()
        if (answer) == str(correct_answer).lower():
            points += 1
            print("Correct!")
        else:
            print(
                f'"{answer}" is wrong answer ;(.'
                f'Correct answer was "{correct_answer}".'
            )
            print(f"Let's try again, {name}!")
            return
        if points == 3:
            print(f"Congratulations, {name}!")


def main():
    run_game()


if __name__ == "__main__":
    main()
