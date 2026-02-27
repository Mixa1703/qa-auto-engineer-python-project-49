import random
from brain_games.cli import welcome_user
def even_numbers():
    name = welcome_user()
    points = 0
    while points <3:
        number = random.randint(0,100)
        print('Answer "yes" if the number is even, otherwise answer "no"')
        print(f'Question: {number}')
        answer = input('Your answer: ')
        
        if number % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
            points += 1
        elif number %2 != 0 and answer.lower() == 'no':
            print('Correct!')
            points += 1
        elif number % 2 == 0 and answer.lower() == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'Yes'.")
            print(f"Let's try again, {name}!")
            break
        elif number % 2 != 0 and answer.lower() == 'Yes':
            print("'Yes' is wrong answer ;(. Correct answer was 'No'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print("'Yes' is wrong answer ;(. Correct answer was 'No'.")
            print(f"Let's try again, {name}!")
            break
    if points == 3:
        print(f'Congratulations, {name}!')
        
def main():
    even_numbers()

if __name__ == '__main__':
    main()