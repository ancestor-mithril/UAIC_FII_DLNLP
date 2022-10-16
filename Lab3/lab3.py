import string
import random
import nltk

from Lab3.utils import exercise2

scores = exercise2(4, 'puțin îi pasă că e rău')
for score in scores:
    print(*score)
