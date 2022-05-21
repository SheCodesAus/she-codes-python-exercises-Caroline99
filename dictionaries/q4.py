import csv

print()

colours = []
with open("colours_20_simple.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

hex_colours = {c[1]:c[2] for c in colours}

for hex, colour in hex_colours.items():
    print(f"{hex}: {colour}")

print()
