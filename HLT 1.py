print("Hello World!")

#Q1
#Write a program that does the following:
#a) Stores a random number (1-10) in a variable – see hint below.
#b) Asks a user for their name and stores this in a variable.
#c) Asks a user to guess the number between 1 and 10.
#d) Tells the user whether they have guessed correctly

import random
myName = input("Hello! What is your name?")
myNumber = random.randint(1,10)
print("Well," + myName + "I am thinking of a number between 1 and 10.")
guess = int(input("Take a guess:"))
if guess == myNumber:
    print ("Good job," + myName + "! You guessed my number")
else:
    print("Wrong! Better luck next time.")


#Q2
#Write a program that asks a user for their favourite number between 1 and 100 and then tells them a joke based on the number. 
# You should use a minimum of 3 jokes.

import random
myName = input("Hello! What is your name?")
favouriteNumber = random.randint(1,100)
print("Well," +myName + "what is your favourite number between 1 and 100?")
answer = int(input("Favourite number answer:"))
if answer == favouriteNumber <25:
    print("Joke one.")
elif favouriteNumber <50:
    print ("Joke two.")
elif favouriteNumber <75:
    print("Joke three.")
elif favouriteNumber <100:
    print("Joke four.")
else:
    print("Better luck next time!")


#Q3
#Write a program that allows user to enter their favourite starter, main course, dessert and drink.
#Concatenate these and output a message which says – “Your favourite meal is ………with a glass of….”.

import random
myName = input("Hello! What is your name?")
starter = int(input("What is your favourite starter?"))
mainCourse = int(input("What is your favourite main course?"))
dessert = int(input("What is your favourite dessert?"))
drink = int(input("What is your favourite drink?"))
print("Your favourite meal is made of a starter of" + starter+ "with a main course of" + mainCourse + "a dessert of" + dessert + "and a drink of" + drink + "to complete it!", myName)


#Q4
#A motorbike costs £2000 and loses 10% of its value every year. 
#Using a loop, print the value of the bike every following year until it falls below £1000.

bike = 2000
while bike > 1000:
    print("The value of the bike ever year with depreciation", bike)
    bike *=0.90

#Q5
#Write a program which will ask for two numbers from a user. Then offer a menu to the user giving them a choice of operator:
#e.g. – Enter “a” if you want to add “b” if you want to subtract
#Include +, -, /, *, ** square (to the power of). Once the user has selected which operator they wish to use, perform the calculation.

x = int(input("What is your first number?"))
y = int(input("What is your second number?"))
operator = input("Enter your operator:")
if operator == "+":
    print("x+y")
elif operator == "-":
    print("x-y")
elif operator == "*":
    print("x*y")
elif operator == "/":
    print("x/y")
elif operator == "**":
    print("x**y")
else:
    print("Invalid operator! Please try again.")
    


