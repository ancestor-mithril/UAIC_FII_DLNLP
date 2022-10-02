from nltk.corpus import wordnet as wn
import random


def get_related_words(word):
    related_words = set()
    for synset in wn.synsets(word):
        hypernyms = lambda s: s.hypernyms()
        hyponyms = lambda s: s.hyponyms()
        related_words = related_words.union(synset.closure(hypernyms))
        related_words = related_words.union(synset.closure(hyponyms))
    return related_words


def get_hint_for_synset(synset):
    lemmas = synset.lemmas()
    name = lemmas[0].name()
    synonyms = []
    antonyms = []
    meronyms = []
    hyponyms = []
    hypernyms = []
    for syn in wn.synsets(name):
        for l in syn.lemmas():
            if l.name().lower() != name.lower():
                synonyms.append(l.name())
            if l.antonyms():
                antonyms += [x.name() for x in l.antonyms()]
            if l.member_meronyms():
                meronyms += [x.name() for x in l.member_meronyms()]
            if l.hyponyms():
                hyponyms += [x.name() for x in l.hyponyms()]
            if l.hypernyms():
                hypernyms += [x.name() for x in l.hypernyms()]

    synonyms = set(synonyms)
    antonyms = set(antonyms)
    meronyms = set(meronyms)
    hyponyms = set(hyponyms)

    help_text = ["is synonym of " + x for x in synonyms]
    help_text += ["is antonym of " + x for x in antonyms]
    help_text += ["is part of " + x for x in meronyms]
    help_text += ["is sort of " + x for x in hyponyms]
    help_text += ["is a " + x for x in hypernyms]
    help_text += [synset.definition()]
    return name.replace('_', ' '), (random.sample(list(help_text), 1)[0]).replace('_', ' ')


def get_words_and_definitions(input_word):
    related_words = get_related_words(input_word)
    word_and_definitions = dict()
    for i in related_words:
        word, definition = get_hint_for_synset(i)
        word_and_definitions[word] = definition
        # print(word, definition)
    return word_and_definitions

# print(get_words_and_definitions('sports'))
