import csv
from random import randint

rnd_index = randint(1, 5756)
random_word = ""

with open('5_letter_words.csv') as word:
    csv_reader = csv.reader(word)
    for index, row in enumerate(csv_reader):
            if index == rnd_index:
                 random_word = (row[1])
                 print(random_word)
                 
