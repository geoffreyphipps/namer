from random import randint
import sys
from typing import List, Tuple

from namer.numbers import random_bucket


class Phonemes:
    """
    File format is:
      First block is pattern with percentages:
    v is vowel, c is consonant. The leading integer is the percentage chance it occurs.
      Following that is a VOWEL
        then one vowel sounds per line
      Following that is a CONSONANTS
        then one consonant sounds per line
    """

    def __init__(self):
        self.phoneme_probabilities: List[Tuple[int, str]] = []
        self.vowels: List[str] = []
        self.consonants: List[str] = []

    def read_language_definitions(self, filename: str):
        with open(filename) as f:
            # First sequence is phoneme probabilities
            total = 0
            while True:
                line = f.readline()
                if len(line) == 0 or line[0] == '#':
                    continue
                if line[:-1] == "VOWELS":
                    break
                r = line.split()
                self.phoneme_probabilities.append((int(r[0]), r[1]))
                total += int(r[0])

            if not total == 100:
                raise ValueError(f"Probabilities add up to {total}, not 100")

            while True:
                line = f.readline()
                if len(line) == 0 or line[0] == '#':
                    continue
                if line[:-1] == "CONSONANTS":
                    break
                self.vowels.append(line[:-1])
            while True:
                line = f.readline()
                if line[:-1] == "END":
                    break
                self.consonants.append(line[:-1])

    def generate(self, number_of_syllables: int, output_file_name: str):
        last_vowel_index = -1
        with open(output_file_name, "w") as f:
            for _ in range(number_of_syllables):
                phoneme_pattern = random_bucket(self.phoneme_probabilities)
                # sys.stdout.write(f"{phoneme_pattern}: ")
                for x in phoneme_pattern:
                    if x == "v":
                        while True:
                            vowel_index = randint(0, len(self.vowels) - 1)
                            if not vowel_index == last_vowel_index:
                                break
                        f.write(self.vowels[vowel_index])
                        last_vowel_index = vowel_index
                    elif x == "c":
                        consonant_index = randint(0, len(self.consonants) - 1)
                        f.write(self.consonants[consonant_index])
                    else:
                        raise ValueError(f"Invalid character _{x}_ in phoneme pattern {phoneme_pattern}")

                f.write('\n')


def generate_phonemes_in_language(filename: str, number_of_syllables: int, output_file_name: str):
    p = Phonemes()
    p.read_language_definitions(filename)
    p.generate(number_of_syllables, output_file_name)


if __name__ == "__main__":
    generate_phonemes_in_language(sys.argv[1], int(sys.argv[2]), sys.argv[3])
