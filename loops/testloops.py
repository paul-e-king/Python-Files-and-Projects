for i in "spam":
    print(i)

import random

num = random.randrange(1,10,1)

guess = -1
correct = False

print ("I am thinking of a number between 1 and 10.")
print ("Can you guess what it is?")
while not correct:
    guess = int(input("What is your guess? "))
    correct = (guess == num)
    if correct:
        print("You guessed right! My number is:", num)
    else:
        print("Nope. Please try again.")

print ("Thanks for playing!")

valid = False
choice = ""
while not valid:
    print ("Please enter 'a' if you like apples, or 'b' if you like bananas.")
    choice = input("A or B? ")
    choice = choice.lower()
    valid = (choice == "a" or choice == "b")
    if not valid:
        print("Your input was not understood. Please try again.")

print("You chose:", choice)

num = ""

while True:
    num = input("Please enter a number or 'stop' to quit: ")
    if num.lower() == "stop":
        break
    elif num.isdigit():
        print("The square of your number is:", int(num) ** 2)
    else:
        try:
            print("The square of your number is:", float(num) ** 2)
        except:
            print("I can't understand your input: ", num)

print("Bye")

for i in range(5):
    print(i, "^2 =", i ** 2)


