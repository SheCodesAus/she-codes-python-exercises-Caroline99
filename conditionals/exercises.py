print("Q1: Is it time for Roary to catch moths?")

moths_in_house = True
# moths_in_house = False

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected")

print()

print("Q2: Roary and Mitch")

# moths_in_house = True
moths_in_house = False
mitch_is_home = True
# mitch_is_home = False

if moths_in_house and mitch_is_home:
    print("Hooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooow! Hissssss!")
else:
    print("Climb on Mitch")

print()

print("Q3: Red Light Cameras")
light_colour = "Red"
# light_colour = "Green"
# light_colour = "Amber"
car_detected = True
# car_detected = False

if light_colour == "Red" and car_detected:
    print("Flash!")
else:
    print("Do nothing.") 

print()

print("Q4: Can they ride the rollercoaster?")
height = input("How tall are you? (in cms): ")

if float(height) >= 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")

print()

print("Q5: Username and password")
username = input("Username: ")
password = input("Password: ")

if username == "fleur" and password == "password123":
    print("Correct!")
else:
    print("Incorrect!")

print()

print("Q6: Is the email address valid (in this weird world)?")
email = input("Enter an email address: ")
print("Email: " + email)
if '@' in email and '.' in email:
    print("Valid email address.")
else:
    print("Invalid email address.")

