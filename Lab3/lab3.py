import string
import random
import nltk

from Lab3.utils import exercise2, build_stop_words

build_stop_words()
scores, total_score = exercise2(2, 'puțin îi pasă că e rău')
print("Total score: ", total_score)
for score in scores:
    print(*score)
