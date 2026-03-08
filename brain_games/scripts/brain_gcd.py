from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    run_game(gcd.RULE, gcd.generate_round)


if __name__ == "__main__":
    main()
