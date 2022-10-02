from Lab1.crossword import  build_crossword
from Lab1.word_list_builder import get_words_and_definitions


word_list = [(key, value) for key, value in get_words_and_definitions('sports').items()]

crossword = build_crossword(word_list)
print(crossword.word_bank())
print(crossword.solution())
# print(crossword.word_find())
print(crossword.display())
print(crossword.legend())
