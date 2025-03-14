def sort_words():

    words = input("Entrez une séquence de mots séparés par des virgules : ")
    
    word_list = words.split(',')
    
    sorted_words = sorted(word_list)

    print(','.join(sorted_words))

# Exemple d'utilisation
if __name__ == "__main__":
    sort_words()