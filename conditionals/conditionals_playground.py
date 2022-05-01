# is_raining = False
# is_cold = True

# print(type(is_raining))
# print(type(is_cold))

# print(is_raining)
# print(not is_raining)
# print(is_raining and is_cold)
# print(is_raining and not is_cold)

# is_raining = True
# print(f"is_cold: {is_cold}")
# print(f"is_raining: {is_raining}")
# print(f"not is_raining: {not is_raining}")
# print(f"is_raining or is_cold: {is_raining or is_cold}")
# print(f"is_raining and not is_cold: {is_raining and not is_cold}")
# print(f"is_raining or not is_cold: {is_raining or not is_cold}")
# print(f"not is_raining and not is_cold: {not is_raining and not is_cold}")

# print()

temperature = 16
print(temperature < 18)
wind_chill = 3
print(wind_chill > 4)
print(temperature - wind_chill < 16)

# name = "Hayley"
# print(name == "Hayley")
# print(name != "Hayley")

print()

## if statements
is_raining = False

# if
if is_raining:
    print("Take an umbrella.")

# if and else
if is_raining:
    print("Take an umbrella.")
else:
    print("Do not take an umbrella.")

# if, elif, else
if temperature - wind_chill < 16:
    print("Take a jumper.")
elif temperature - wind_chill > 30:
    print("Euck, it's hot today, stay home.")
else:
    print("Wow, what a lovely day!")

# nested if statements
if temperature - wind_chill < 16 and is_raining:
    print("Just stay home.")
else:
    if is_raining:
        print("You'll need an umbrella today.")
    if temperature - wind_chill < 16:
        print("You'll need a jumper today.")


# Class time
# Data Types - Strings, Integer, Floats, Boolean
b1 = True
b2 = False
print(type(b1))

knows_password = True
knows_name = True
login = knows_password and knows_name
print(type(login))
print(login)

print((9/3)== 3) 
