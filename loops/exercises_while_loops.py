print()
print("Q1: Sum of numbers (input ends when blank is entered)")
print()

sum = 0
n = input("Enter a number: ")

while n != "":
    sum += int(n)
    n = input("Enter a number: ") 

print(sum)

print()

print("Q2: Print odd numbers between 0 and the input number(inclusive)")
print()

odds = 1
num = int(input("Enter a number: "))

while odds <= num:
    print(odds)
    odds += 2

print()

print("Q3: Guess the number")
print()

target = 13
guess = int(input("Guess the number: "))

while guess != target:
    if guess < target:
        print("Too low!")
        # guess = int(input("Guess the number: "))
    else:
        print("Too high!")
        # guess = int(input("Guess the number: "))
    guess = int(input("Guess the number: "))
print("Correct!")

print()




