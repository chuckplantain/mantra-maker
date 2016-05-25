import random
import string

with open('/usr/share/dict/words') as f:
        content = f.readlines()

vowels = list('aeiou')
consonants = [x for x in string.ascii_lowercase if x not in vowels]

words = random.randint(3, 7)

mantra = ''

i = 0
while i < words:
    i += 1
    if i == words:
        lastWord = ''
    else:
        lastWord = '-'
    new_word = random.choice(consonants) + random.choice(vowels) + lastWord
    mantra += new_word

print(mantra)
