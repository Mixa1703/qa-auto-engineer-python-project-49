import random

RULE = "Find the greatest common divisor of given numbers."


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    divider = 1
    max_divider = 1
    if number1 >= number2:
        max_number = number1
    else:
        max_number = number2
    while divider <= max_number:
        if number1 % divider == 0 and number2 % divider == 0:
            max_divider = divider
            divider += 1
        else:
            divider += 1

    return question, max_divider
