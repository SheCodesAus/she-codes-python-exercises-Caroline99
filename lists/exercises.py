print("Q1: Foods")
print()

foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[7:])
print(foods[6][2])

print()

print("Q2: Format and print the mailing list")
print()

mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"]
]

print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")

print()

print("Q3: Three name inputs into a list")
print()

name1 = input("Enter a name: ")
name2 = input("Enter a name: ")
name3 = input("Enter a name: ")

name_list = [name1, name2, name3]
print(name_list)

# alt method
# print([name1, name2, name3])

print()

print("Q4: Make lists from lists")
print()

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

d.append(a)
d.append(b)
d.append(c)
print(d)

e.extend(a)
e.extend(b)
e.extend(c)
print(e)

print()


