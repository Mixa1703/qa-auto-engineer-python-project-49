import random

RULE = "What is the result of the expression?"


def generate_round():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operand = random.choice(["+", "-", "*"])
    question = str(f"{number1} {operand} {number2}")
    if operand == "+":
        correct_answer = number1 + number2
    elif operand == "-":
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return question, correct_answer
