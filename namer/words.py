from random import randint
import sys
from typing import List, Tuple

from namer.numbers import random_bucket


class Namer:
    """
    File format is:
      First line is a series of integers that add up to 100. That is the percentage chance of that number
      of syllables.
      Following that is one syllable per line
    """

    def __init__(self):
        self.syllable_probabilities: List[Tuple[int,int]] = []
        self.syllables: List[str] = []

    def read_language_definitions(self, filename: str):
        with open(filename) as f:
            # First line is syllable probabilities
            raw = f.readline().split()

            i = 0
            total = 0
            for r in raw:
                self.syllable_probabilities.append((int(r), i))
                i += 1
                total += int(r)

            if not total == 100:
                raise ValueError(f"Probabilities add up to {total}, not 100")

            for line in f:
                self.syllables.append(line[:-1])

    def generate(self, number_of_words: int, output_file_name: str):
        with open(output_file_name, "w") as f:
            for _ in range(number_of_words):
                number_of_syllables = random_bucket(self.syllable_probabilities)
                f.write(f"{number_of_syllables}: ")
                for _ in range(number_of_syllables):
                    syllable_number = randint(1, len(self.syllables))
                    f.write(self.syllables[syllable_number - 1])
                f.write('\n')


def main(filename: str, number_of_words: int, output_file_name: str):
    n = Namer()
    n.read_language_definitions(filename)
    n.generate(number_of_words, output_file_name)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
