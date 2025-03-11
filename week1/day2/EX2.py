family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15
    
total_cost = 0
for name, age in family.items():
    price = calculate_ticket_price(age)
    print(f"{name} has to pay: ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")

#Bonus:
family = {}

while True:
    name = input("Enter a family member's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

total_cost = 0
for name, age in family.items():
    price = calculate_ticket_price(age)
    print(f"{name} has to pay: ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")