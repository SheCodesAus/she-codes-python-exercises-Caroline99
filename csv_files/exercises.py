import csv

print("Q1: Output colour data from colours_20_simple.csv")
print()

colours = []
with open("csv_files/colours_20_simple.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

for colour in colours:
    print(f"{colour[0]} {colour[1]} {colour[2]}")

print()

print()
print("Q2: Reformat colour from colours_20_simple.csv")
print()

# Use this if not running with Q1
# colours = []
# with open("csv_files/colours_20_simple.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)

titles = colours.pop(0)
for colour in colours:
    print(f"{colour[2]}, {titles[1].capitalize()}: {colour[1]}, {titles[0]}: {colour[0]}")

print()

print("Q3: Reformat colours from colours_20.csv")
print()

intl_colours = []
with open("csv_files/colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        intl_colours.append(line)

headers = intl_colours.pop(0)
for header in headers:
    if "English" in header:
        english_index = headers.index(header)
    if "HEX" in header:
        hex_index = headers.index(header)
    if "RGB" in header:
        rgb_index = headers.index(header)

for i in intl_colours:
    print(f"{i[english_index]}, {headers[hex_index].lstrip().capitalize()}: {i[hex_index]},{headers[rgb_index]}: {i[rgb_index]}")

print()  

print("Q4: Counting the colours")
print()

print("Available files:")
print("1. colours_20_simple.csv")
print("2. colours_20.csv")
print("3. colours_213.csv")
print()

choice = input("Choose an option: ")

while choice not in ["1", "2", "3"]:
    choice = input("Please select 1, 2 or 3: ")

if choice == "1":
    f = "csv_files/colours_20_simple.csv"
elif choice == "2":
    f = "csv_files/colours_20.csv"    
elif choice == "3":
    f = "csv_files/colours_213.csv"

colours = []
with open(f) as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

titles = colours.pop(0)

for title in titles:
    if "English" in title:
        place = titles.index(title)

colour_list = []
red_count = 0
green_count = 0
blue_count = 0
yellow_count = 0

for colour in colours:
    colour_list.append(colour[place])

for x in colour_list:
    if 'red' in x:
        red_count += 1
    if 'green' in x:
        green_count += 1
    if 'blue' in x:
        blue_count += 1
    if 'yellow' in x:
        yellow_count += 1

print()
print(f"Red: {red_count}")
print(f"Green: {green_count}")
print(f"Blue: {blue_count}")
print(f"Yellow: {yellow_count}")
print()

print("Q5: Galaxies - find min and max velocities")
print()

galaxies = []
with open("csv_files/galaxies.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        galaxies.append(line)

# headers = galaxies.pop(0)
galaxies.pop(0)

velocities = []
for galaxy in galaxies:
    velocities.append(int(galaxy[1]))

min_vel = min(velocities)
max_vel = max(velocities)
min_index = velocities.index(min_vel)
max_index = velocities.index(max_vel)

print(f"Galaxy {galaxies[min_index][0]} has the min velocity of {min_vel}km/sec.")
print(f"Galaxy {galaxies[max_index][0]} has the max velocity of {max_vel}km/sec.")
print()

