import csv

print()

colours = []
with open("dictionaries/colours_20_simple.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

hex_colours = {c[1]:[c[0], c[2]] for c in colours}

for hex, rgb_eng in hex_colours.items():
    print(f"{hex}: {rgb_eng}")

print()