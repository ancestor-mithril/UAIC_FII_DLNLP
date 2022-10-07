import nltk
from nltk import CFG
import spacy
from spacy import displacy

grammar = CFG.fromstring("""
S -> N VP
S -> NP V

NP -> N N

VP -> V NP
VP -> AdvT V

V -> VP NP
V -> AdvT V
V -> V AdvM
V -> V AdvT


N -> Atr N
N -> P N


N -> 'Papa'
N -> 'octopus'
N -> 'pajamas'
N -> 'John'
N -> 'food'
N -> 'Mary'
V -> 'eats'
V -> 'eat'
P -> 'in'
P -> 'or'
P -> 'and'
AdvT -> 'often'
AdvM -> 'together'
Atr -> 'sea'
""")

raw_sentence1 = 'Papa eats octopus in pajamas.'
raw_sentence2 = 'John often eats sea food or octopus.'
raw_sentence3 = 'John and Mary eat often together.'


sentence1 = raw_sentence1.replace('.', '').split()
sentence2 = raw_sentence2.replace('.', '').split()
sentence3 = raw_sentence3.replace('.', '').split()
sentences = [sentence1, sentence2, sentence3]


parser = nltk.ChartParser(grammar)
for idx, sentence in enumerate(sentences):
    print("Sentence ", idx)
    print(sentence)
    print(parser.parse(sentence))

    for tree in parser.parse(sentence):
        print(str(tree).replace('(', '[').replace(')', ']'))

nlp = spacy.load('en_core_web_sm')

doc1 = nlp(raw_sentence1)
doc2 = nlp(raw_sentence2)
doc3 = nlp(raw_sentence3)
docs = [doc1, doc2, doc3]


for idx, doc in enumerate(docs):
    print("Doc " + str(idx))
    for word in doc1:
        print(word.text, word.pos_, word.dep_)
    print()

print()
print(spacy.explain('nsubj'))

displacy.serve(docs, style="dep")
