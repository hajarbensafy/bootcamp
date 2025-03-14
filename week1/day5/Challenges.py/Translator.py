from googletrans import Translator

def translate_words(word_list):
    translator = Translator()
    translated_dict = {}

    for word in word_list:
        # Traduit le mot du français vers l'anglais
        translated = translator.translate(word, src='fr', dest='en')
        translated_dict[word] = translated.text

    return translated_dict

# Liste de mots français
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Traduction des mots
translated_words = translate_words(french_words)

# Affichage du résultat
print(translated_words)