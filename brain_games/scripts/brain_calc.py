from brain_games.engine import run_game
from brain_games.games import calc


def main():
    run_game(calc.RULE, calc.generate_round)


if __name__ == "__main__":
    main()
