import random

RULE = "What number is missing in the progression?"


def generate_round():
    progress = random.randint(1, 10)
    number1 = random.randint(1, 100)
    number2 = number1 + progress
    number3 = number2 + progress
    number4 = number3 + progress
    number5 = number4 + progress
    number6 = number5 + progress
    number7 = number6 + progress
    number8 = number7 + progress
    number9 = number8 + progress
    number10 = number9 + progress
    numbers_list = [
        number1,
        number2,
        number3,
        number4,
        number5,
        number6,
        number7,
        number8,
        number9,
        number10,
    ]
    hidden_index = random.randint(0, len(numbers_list) - 1)
    correct_answer = numbers_list[hidden_index]
    numbers_list[hidden_index] = ".."
    question = " ".join(map(str, numbers_list))
    return question, correct_answer
