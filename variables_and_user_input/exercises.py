number1 = input("Enter a number: ")
number2 = input("Enter another number: ")

print("Q1: Add the numbers")
print(float(number1) + float(number2))

print()

print("Q2: Multiply the numbers and show the full equation")
print(f"{float(number1)} * {float(number2)} = {float(number1) * float(number2)}" ) 

print()

print("Q3: Kilometres converted to metres and centimetres")
kms = input("How many kilometres? ")
print(f"{float(kms)}km = {int(float(kms) * 1000)}m")
print(f"{float(kms)}km = {int(float(kms) * 100000)}cm")

print()

print("Q4: Name and their height")
name = input("What is your name? ")
height = input("How tall are you (cms)? ")
print(f"{name} is {height}cms tall.")

print()