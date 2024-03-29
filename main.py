import random
import string
import sqlite3
import datetime
import ipdb

con = sqlite3.connect('mantras.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS mantras
               (date text, mantra text)''')


# brap-da-sa

vowels = list('aeiou')
vowels.append('oo')

consonants = [x for x in string.ascii_lowercase if x not in vowels]
consonants.remove('q')
consonants.extend(['ch', 'sh', 'qu'])

beginning_consonants = consonants + ['shr', 'fr', 'br']
beginning_consonants.remove('x')

non_ending_consonants = ['v', 'x', 'c', 'j', 'q', 'qu', 'v', 'w', 'y']
ending_consonants = [x for x in consonants if x not in non_ending_consonants] + ['ck']

def main():
    how_many_words = random.randint(3, 6)
    mantra = ''
    i = 0

    while i < how_many_words:
        i += 1
        should_we_make_longer_syllable = random.random()
        if should_we_make_longer_syllable > 0.85:
            new_word = random.choice(vowels) + random.choice(ending_consonants)
        elif should_we_make_longer_syllable > 0.7:
            new_word = random.choice(beginning_consonants) + random.choice(vowels) + random.choice(ending_consonants)
        else:
            new_word = random.choice(beginning_consonants) + random.choice(vowels)
        if i < how_many_words:
            new_word += '-'
        mantra += new_word
    return mantra
# ipdb.set_trace()
word = main()
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cur.execute("INSERT INTO mantras (mantra, date) VALUES (?, ?)", (word, now))
con.commit()
print(word)
