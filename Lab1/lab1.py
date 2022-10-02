import ipuz
import puz
from crossword import Crossword, to_ipuz
from Lab1.crossword_creation import build_crossword
from Lab1.word_list_builder import get_words_and_definitions
import json


word_list = [(key, value) for key, value in get_words_and_definitions('sports').items()]

c = build_crossword(word_list)
if c is None:
    raise "Please use another thematic for your crossword puzzle"

print(c.word_bank())
crossword_solution = c.solution()
print(crossword_solution)
crossword_solution = crossword_solution.replace(' ', '').split('\n')
json_solution = c.solution2json()
print(json_solution)

settings_file = 'settings.json'
json.dump(json_solution, open(settings_file, 'w'))


puzzle = Crossword(json_solution["size"]["rows"], json_solution["size"]["cols"])
for x, y in puzzle.cells:
    cell_value = crossword_solution[x][y]
    if cell_value != '*':
        puzzle[x, y].cell = 0
        puzzle[x, y].solution = cell_value
        # puzzle[x, y].style = {'background-color': 'red'}
    else:
        puzzle[x, y].cell = None
        # puzzle[x, y].style = {'background-color': 'white'}

for index, word in enumerate(json_solution["words"]):
    if word["direction"] == 'across':
        puzzle.clues.down[index + 1] = word["clue"]
    else:
        puzzle.clues.across[index + 1] = word["clue"]
    puzzle[word["row"] - 1, word["col"] - 1].cell = index + 1

for direction, number, clue in puzzle.clues.all():
    print(direction, number, clue)

ipuz_dict = to_ipuz(puzzle)

print(puzzle)

with open('puzzle.ipuz', 'w') as puzzle_file:
    puzzle_file.write(ipuz.write(ipuz_dict))

