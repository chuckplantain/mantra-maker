import random
import string

with open('/usr/share/dict/words') as f:
        content = f.readlines()

vowels = list('aeiou')
consonants = [x for x in string.ascii_lowercase if x not in vowels]

base = random.choice(content)


print(base)
