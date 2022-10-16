import string

from datasets import load_dataset
from nltk.corpus import stopwords
from nltk.util import pad_sequence, ngrams
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import flatten
from nltk.lm import Laplace


def load_sentences():
    """
    https://github.com/dumitrescustefan/ronec
    :return: list of sentences, each sentence is a list of tokens (words + punctuation)
    """
    return [i["tokens"] for i in load_dataset("ronec")["train"]]


def build_stop_words():
    stop_words = set(stopwords.words('romanian'))
    punctuation = string.punctuation + '-' + '''+''' + '—' + '„' + "”"
    return list(stop_words) + list(punctuation)


def pad_sentence(sentence, n):
    """

    :param sentence: the sentence to be padded
    :param n: the n from n-gram, padding is done with no, one ore more start (<s>) and end (</s>) tokens
    :return: the padded sentence
    """
    return tuple(pad_both_ends(sentence, n=n))


def pad_sentences(sentences, n):
    """

    :return: tuple of padded sentences
    """

    def pad(sentence):
        return pad_sentence(sentence, n)

    return tuple(map(pad, sentences))


def sentence_to_lower(sentence):
    return tuple(map(str.lower, sentence))


def sentences_to_lower(sentences):
    return tuple(map(sentence_to_lower, sentences))


def flatten_sentences(sentences):
    """

    :param sentences: list of sentences <=> list of list of tokens
    :return: list of tokens
    """
    return tuple(flatten(sentences))


def create_ngrams(sentences, n):
    def to_ngram(sentence):
        return tuple(ngrams(sentence, n))

    return tuple(map(to_ngram, sentences))


def build_ngram_vocabulary(sentences, n):
    sentences = sentences_to_lower(sentences)
    sentences = pad_sentences(sentences, n)
    n_grams = create_ngrams(sentences, n)
    vocabulary = flatten_sentences(sentences)
    return n_grams, vocabulary


def get_ngram_vocabulary(n):
    sentences = load_sentences()
    return build_ngram_vocabulary(sentences, n)


def create_and_train_model(n_grams, vocabulary, n):
    model = Laplace(n)
    model.fit(n_grams, vocabulary)
    return model


def compute_probability_of_new_sentence(model, sentence, n):
    words = sentence.split()  # we assume no punctuation
    words = pad_sentence(sentence_to_lower(words), n)
    scores = list()
    min_score = model.score("<UKN>");

    def limit_context(context):
        context = context[-n + 1:]
        if len(context) == 0 or n == 1:
            return None
        return context

    for i in range(n - 1, len(words) - n + 1):
        context = limit_context(words[:i])
        current = words[i]
        score = model.score(current, context)
        if abs(score - min_score) < 1e-8:
            score = "MIN"

        scores.append(
            [f"{current} | {' '.join(context) if context is not None else '':<16}", score])
    return scores


def exercise1(n):
    n_grams, vocab = get_ngram_vocabulary(n)
    model = create_and_train_model(n_grams, vocab, n)
    return model


def exercise2(n, sentence):
    model = exercise1(n)
    scores = compute_probability_of_new_sentence(model, sentence, n)
    return scores
