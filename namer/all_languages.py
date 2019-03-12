import fnmatch
import os

from namer.words import generate_words_in_language
from namer.phonemes import generate_phonemes_in_language


def generate_all_syllabic_structures():
    os.makedirs(f"output/tmp", 0o755, True)
    os.makedirs(f"output/syllables", 0o755, True)
    for file in os.listdir('input/phonemes'):
        if fnmatch.fnmatch(file, '*_phonemes.txt'):
            language_name = '_'.join(file.split('_')[:-1])
            final_file = f"output/syllables/{language_name}_syllables.txt"
            probabilities_file = f"input/syllables/{language_name}_syllabic_probabilities.txt"
            tmp_file = f"output/tmp/{language_name}_list.tmp"
            generate_phonemes_in_language(f"input/phonemes/{file}", 1000, tmp_file)
            os.system(f"cat {probabilities_file} {tmp_file} > {final_file}")
            #os.remove(tmp_file)


def generate_all_languages():
    for file in os.listdir('output/syllables'):
        if fnmatch.fnmatch(file, '*_syllables.txt'):
            language_name = '_'.join(file.split('_')[:-1])
            generate_words_in_language(f"output/syllables/{file}", 1000, f"output/{language_name}_words.txt")


if __name__ == "__main__":
    generate_all_syllabic_structures()
    generate_all_languages()
