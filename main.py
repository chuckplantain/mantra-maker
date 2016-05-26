import random
import string

with open('/usr/share/dict/words') as f:
        content = f.readlines()

vowels = list('aeiou')
vowels.append('oo')
consonants = [x for x in string.ascii_lowercase if x not in vowels]
consonants.remove('q')
consonants.extend(['ch', 'sh', 'qu'])
beginning_consonants = consonants + ['shr', 'fr', 'br']
beginning_consonants.remove('x')
non_ending_consonants = ['v', 'x', 'c', 'j', 'q', 'qu', 'v', 'w', 'y']
ending_consonants = [x for x in consonants if x not in non_ending_consonants] + ['ck']
how_many_words = random.randint(3, 5)

mantra = ''

i = 0
while i < how_many_words:
    i += 1

    if i == how_many_words:
        last_word = ''
    else:
        last_word = '-'
    should_we_make_longer_syllable = random.random()

    if should_we_make_longer_syllable > 0.75:
        new_word = random.choice(vowels) + random.choice(ending_consonants) + last_word
    elif should_we_make_longer_syllable > 0.5:
        new_word = random.choice(beginning_consonants) + random.choice(vowels) + random.choice(ending_consonants) + last_word
    else:
        new_word = random.choice(consonants) + random.choice(vowels) + last_word

    mantra += new_word

print(mantra)
