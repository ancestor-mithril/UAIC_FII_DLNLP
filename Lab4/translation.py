from googletrans import Translator
translator = Translator()


def get_sentence_pair():
    sentence = input("Insert sentence...\n")
    result = translator.translate(sentence, src='en', dest='ro')
    translate = result.text
    print("Translation: ", translate)
    perfect_translation = translate
    answer = input("Is the perfect translation? Y/N\n")

    if answer.lower() == 'y' or answer.lower() == 'yes':
        pass
    else:
        perfect_translation = input("Enter the right translation? Y/N\n")

    return translate, perfect_translation
