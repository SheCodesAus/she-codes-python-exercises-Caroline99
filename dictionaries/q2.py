print()

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}


# colours = [
#     "purple",
#     "red",
#     "yellow",
#     "blue",
#     "purple",
#     "orange",
#     "blue",
#     "purple",
#     "orange",
#     "green"
# ]

colours = [
    "orange",
    "purple",
    "blue",
    "yellow",
    "green",
    "green",
    "purple",
    "purple",
    "green",
    "blue",
    "green",
    "orange",
    "purple",
    "blue",
    "green",
    "orange",
    "orange",
    "red",
    "yellow",
    "yellow"
]

for colour in colours:
    colour_counts[colour] += 1

for c in colour_counts:
    print(f"{c}: {colour_counts[c]}")

print()
