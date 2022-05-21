print()

names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
    "Joy", "Katie", "Maddie", "Tash", "Nic",
    "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
    "Viv", "Anna", "Catherine", "Catherine", "Debby",
    "Gab", "Megan", "Michelle", "Nic", "Roxy",
    "Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

# names = [
#     "Miranda", "Sophie", "Emily", "Taylor", "Anne",
#     "Djuarli", "Anika", "Rosie", "Miranda", "Taylor",
#     "Abby", "Sarah", "Teagen", "Abby", "Abby",
#     "Maddie", "Miranda", "Rosie"
# ]

name_counts = {}.fromkeys(names, 0)

for name in names:
    name_counts[name] += 1

for name, count in name_counts.items():
    print(f"{name}: {count}")

print()