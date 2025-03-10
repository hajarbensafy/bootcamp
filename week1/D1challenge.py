#challenge 1 :
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples = [number * i for i in range(1, length + 1)]

print(multiples)

#challenge 2 :
user_word = input("Enter a word: ")

new_word = ""
previous_char = "" 

for char in user_word:
    if char != previous_char: 
        new_word += char
    previous_char = char  

print(new_word)