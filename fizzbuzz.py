import fire
from fizzbuzz.fizzbuzz import fizzbuzz


def main(low, high):
    """
    The program implementing the FizzBuzz game.

    :param low: The number you want to start the game with.
    :param high: The number at which you want to end the game.
    """
    for n in range(low, high):
        print(fizzbuzz(n))


if __name__ == "__main__":
    fire.Fire(main)
