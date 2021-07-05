print ("Hello, World!")


import  random
name = input("What is your name?")
number  = random.randint(1,10)
print("Well," + name + "I am thinking of a number between 1 and 10.")
guess = int(input("Take a guess:"))
if guess == number:
    print("Good job," + name + "! You guessed my number.")
else:
    print("Wrong, better luck next time.")


import random
name = input("What is your name?")
favouriteNumber = random.randint(1,100)
print("Well," + name + "What is your favourite number betwen 1 and 100?")
answer = int(input("Favourite number answer:"))
if answer == favouriteNumber <25:
    print("joke one")
elif favouriteNumber <50:
    print("joke two")
elif favouriteNumber <75:
    print ("joke three")
elif favouriteNumber <100:
    print("joke four")
else:
    print("Better luck next time.")


    starter = int(input("What is your favourite starter?"))
    mainCourse = int(input("What is your favourite main course?"))
    dessert = int(input("What is your favourite dessert?"))
    drink = int(input("What is your favourite drink?"))
print("Your favourite starter is" + starter + "your favourite main course is" + mainCourse + "your favourite desser is" + dessert + "your favourite drink is" + drink)


bike = 2000
while bike > 1000:
    print("Value of bike every year", bike)
    bike *=0.90


x = int(input("What is your first number?"))
y = int(input("What is your second number?"))
operator = input("Enter your operator:")
if operator == "+":
    print(x + y)
elif operator == "_":
    print(x - y)
elif operator == "/":
    print(x / y)
elif operator == "*":
    print(x * y)
elif operator == "**":
    print(x ** y)
else:
    print("Invalid operator, please try again.")
    