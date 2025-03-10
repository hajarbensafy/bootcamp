#Exercise 1 :
print("Hello world\n" * 4)

#Exercice 2 :
result = (99 ** 3) * 8
print(result)

#Exercice 3 :
name = input("What is your name? ")
if name == "VotreNom":  # Remplacez "VotreNom" par votre nom
    print("Hey, we have the same name! Twinsies!")
else:
    print(f"Nice to meet you, {name}! But my name is way cooler.")

    #Exercice 4 :
height = int(input("Enter your height in centimeters: "))
if height > 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")

    #Exercice 5 :
    my_fav_numbers = {7, 13, 21}
my_fav_numbers.add(42)
my_fav_numbers.add(99)
my_fav_numbers.remove(99)  # Supprime le dernier nombre ajouté

friend_fav_numbers = {10, 20, 30}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercice 6 :
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)
print(new_tuple)

#Exercice 7 :
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
basket.clear()
print(basket)

#Exercice 8 :
sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"
]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.lower()}")

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
