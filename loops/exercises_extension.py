print("Q1: Izzy's Food Emporium receipt")
print()

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

totals = []
print("Please enter 6 quantities - click Enter after each one")
for i in range(6):
    totals.append(int(input()) * groceries[i][1]) 

print()
print("====Izzy's Food Emporium====")
for i in range(6):
    print(f"{groceries[i][0]}{' '*(18 - len(groceries[i][0]))}${totals[i]:.2f}")
print("============================")
print(f"{' '*18}${sum(totals):.2f}")

print()

print("Q2: String to position and character")
print()

s = input("Please enter a string: ")

for i in range(0, len(s)):
    print(i, s[i])

print()

print("Q3: Pyramid")
print()

height = int(input("Pyramid size: "))

counter = 1
while counter <= height:
    print("*" * counter)
    counter += 1

print()

print("Q4: A different pyramid")
print()

height = int(input("Pyramid size: "))
counter = 1
spaces = height - 1
stars = 1
while counter <= height:
    print(" " * spaces + "*" * stars)
    counter += 1
    stars += 2
    spaces -= 1

print()