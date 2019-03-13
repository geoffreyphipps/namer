from random import randint
import sys
from typing import List, Tuple

from namer.numbers import random_bucket


class Namer:
    """
      Generates a bunch of words, severl per line
      The Input File format is:
      First line is a series of integers that add up to 100.
      That is the percentage chance of that number of syllables.
      Following that is one syllable per line.
    """

    def __init__(self) -> None:
        self.syllable_probabilities: List[Tuple[int, int]] = []
        self.syllables: List[str] = []

    def read_language_definitions(self, filename: str) -> None:
        with open(filename) as f:
            # First line is syllable probabilities
            raw = ['#']
            while raw[0][0] == '#':
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
                if len(line) > 0 and not line[0] == '#':
                    self.syllables.append(line[:-1])

    def generate(self, number_of_words: int, output_file_name: str, words_per_line: int = 3) -> None:
        word_count = 0
        char_count = 0
        with open(output_file_name, "w") as f:
            for _ in range(number_of_words):
                number_of_syllables = random_bucket(self.syllable_probabilities)
                f.write(f"{number_of_syllables}: ")
                for _ in range(number_of_syllables):
                    syllable_number = randint(1, len(self.syllables))
                    syllable = self.syllables[syllable_number - 1]
                    char_count += len(syllable)
                    f.write(syllable)
                word_count = (word_count + 1) % words_per_line
                if word_count == 0:
                    f.write('\n')
                else:
                    f.write(' ' * (30 - char_count))
                char_count = 0


def generate_words_in_language(word_file_name: str, number_of_words: int, output_file_name: str) -> None:
    n = Namer()
    n.read_language_definitions(word_file_name)
    n.generate(number_of_words, output_file_name)


if __name__ == "__main__":
    generate_words_in_language(sys.argv[1], int(sys.argv[2]), sys.argv[3])
