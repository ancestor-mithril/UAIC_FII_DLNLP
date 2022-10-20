from Lab4.translation import get_sentence_pair
from scores import bleu, precision, f_measure, recall
from nltk.tokenize import word_tokenize


translated, reference = get_sentence_pair()
translated = word_tokenize(translated)
reference = word_tokenize(reference)
print(translated)
print(reference)
print("Precision", precision(translated, reference))
print("Recall", recall(translated, reference))
print("F Measure", f_measure(translated, reference))
print("BLEU", bleu(translated, reference))


print("\n\n\n")
translated, reference = get_sentence_pair()
translated = word_tokenize(translated)
reference = word_tokenize(reference)
print(translated)
print(reference)
print("Precision", precision(translated, reference))
print("Recall", recall(translated, reference))
print("F Measure", f_measure(translated, reference))
print("BLEU", bleu(translated, reference))

