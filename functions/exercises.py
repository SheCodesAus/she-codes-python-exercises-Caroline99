print("Q1: Convert fahrenheit to celsius")
print()

def convert_fahr_to_cels(temp_in_f):
    return (temp_in_f - 32) * 5 / 9

DEGREE_SYMBOL = u"\N{DEGREE SIGN}"
print(f"32{DEGREE_SYMBOL}F: {convert_fahr_to_cels(32)}")
print(f"0{DEGREE_SYMBOL}F: {convert_fahr_to_cels(0)}")
print(f"350{DEGREE_SYMBOL}F: {convert_fahr_to_cels(350)}")


print()

print("Q2: is_odd")
print()

def is_odd(num):
    return num % 2 == 1

print(f"2: {is_odd(2)}")
print(f"7: {is_odd(7)}")
print(f"-1: {is_odd(-1)}")

print()

print("Q3: Calculate mean of list")
print()

def mean(numbers):
    return sum(x for x in numbers) / len(numbers)

print(f"[4, 3, 2, 6] {mean([4, 3, 2, 6])}")
print(f"[10, 5, 6] {mean([10, 5, 6])}")

print()

print("Q4: Total cost, given item price and how many")
print()

def total_cost(price_per_unit, num_units):
    return f"${price_per_unit * num_units}"

print(f"$4.25 * 3 = {total_cost(4.25, 3)}")
print(f"$3.79 * 1 = {total_cost(3.79, 1)}")
print(f"$1.49 * 7 = {total_cost(1.49, 7)}")