print()

prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}

# quantity = {
#     "Baby Spinach": 2,
#     "Hot Chocolate": 1,
#     "Crackers": 4,
#     "Bacon": 0,
#     "Carrots": 8,
#     "Oranges": 5
# }

num_items = 0
total = 0

for item in quantity:
    num_items += quantity[item]
    total += quantity[item] * prices[item]
    print(f"{quantity[item]} {item} @ ${prices[item]} = ${quantity[item] * prices[item]:.2f}")

print()
print(f"Total number of items: {num_items}")
print(f"Total price = ${total:.2f}")
print()
