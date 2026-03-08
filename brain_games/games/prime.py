import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    number = random.randint(1, 10)
    points = 0
    question = str(number)
    divider = 2
    while divider <= number:
        if number % divider == 0 and divider != number:
            points += 1
            divider += 1
        else:
            divider += 1
    if number > 1 and points == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
