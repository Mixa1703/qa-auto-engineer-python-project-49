from brain_games.engine import run_game
from brain_games.games import prime


def main():
    run_game(prime.RULE, prime.generate_round)


if __name__ == "__main__":
    main()
