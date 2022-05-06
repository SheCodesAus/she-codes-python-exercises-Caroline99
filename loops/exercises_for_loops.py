print()
print("Q1: Times tables")
print()

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(f"{n} * {i} = {n * i}")

print()

print("Q2: Triangular numbers")
print()

t = int(input("Enter a number: "))

total = 0
for i in range(0, t+1):
    total += i

print(total)

print()

print("Q3: Sum a list")
print()

random_numbers = [3, 5, 9, 1]
# random_numbers = [-3, -5, 9, 1]
# random_numbers = []

output = 0
for num in random_numbers:
    output += num
print(f'The list is: {random_numbers}')
print(output)

print()

print("Q4: Format a list")
print()

mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]

for item in mailing_list:
    print(f"{item[0]}: {item[1]}")

print()




