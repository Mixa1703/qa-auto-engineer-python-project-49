import prompt


def welcome_user():
    name = prompt.string('May i have your name?')
    if name:
        print(f'Hello,{name}!')
