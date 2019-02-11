# namer
Generate words using simple phonetic rules.

There are two executables: words.py and phonemes.py
Sample input files are in the data directory.

words.py generates words from syllable definitions. There is a
sample syllable definition in data/vignan_syllables.txt
words takes three arguments:
  1. The path of syllable file
  2. The number of words to generate
  3. The path of the output file
  
The first line of the syllable file gives the percentage chance
of a word having that many syllables. For example,
  10 20 70
would mean that there is a 10% chance of a word having one
syllable, 20% chance of 2, and 70% chance of three. The 
probabilities must be integers that add to 100. Each syllable
is chosen randomly, there are no phonetic rules between 
syllables.
  
The phonemes.py prgram generates syllables from vowels
and consonants. It could generate whole words if the 
vowel-consonant rules were extended. I currently use it
to generate syllables to put into the syllables file to feed
to words.py.

phoneme.py takes three arguments:
  1. The path of phoneme file
  2. The number of syllables to generate
  3. The path of the output file
  
The phoneme file has three sections:
  1. Phoneme patterns, expressed as strings of 'v' (for vowel) and 'c' (for consonant),
  followed by the list of vowels, followed by a list of consonants. Each vowel or consonant
  appears one per line. If you can read the international phonetic
  alphabet (I can't) then you could have one character per line.
  The samples use either single English letters (when there is little
  ambiguity), somewhat standard English digraphs, surrounded by parentheses
  and some letters with cedillas and breves to distinguish voiced/voiceless
  consonants and short/long vowels. eth (ð) is voiced, as in "mother".
  Thorn (þ) is voiceless, as in "moth" (in British Englishes, I have heard Americans pronounce
  that word using eth.
  2. The number of syllables
  3. The path to the output file
