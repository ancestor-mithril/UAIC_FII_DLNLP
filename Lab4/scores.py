from nltk import ngrams


def precision(translated, reference):
    if len(translated) == 0:
        return 0
    return len([word for word in translated if word in reference]) / len(translated)


def recall(translated, reference):
    if len(reference) == 0:
        return 0
    return len([word for word in translated if word in reference]) / len(reference)


def f_measure(translated, reference):
    p = precision(translated, reference)
    r = recall(translated, reference)
    return 2 * p * r / (p + r)


def to_ngram(sentence, n):
    return tuple(ngrams(sentence, n))


def bleu(translated, reference):
    a = min(1.0, len(translated) / len(reference))
    precision1 = precision(to_ngram(translated, 1), to_ngram(reference, 1))
    precision2 = precision(to_ngram(translated, 2), to_ngram(reference, 2))
    precision3 = precision(to_ngram(translated, 3), to_ngram(reference, 3))
    precision4 = precision(to_ngram(translated, 4), to_ngram(reference, 4))
    return a * ((precision1 * precision2 * precision3 * precision4) ** (1 / 4))
