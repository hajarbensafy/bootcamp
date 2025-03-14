def longest_word(sentence):
    
    words = sentence.split()

    longest = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    return longest

if __name__ == "__main__":
    print(longest_word("Margaret's toy is a pretty doll."))  # "Margaret's"
    print(longest_word("A thing of beauty is a joy forever."))  # "forever."
    print(longest_word("Forgetfulness is by all means powerless!"))  # "Forgetfulness"