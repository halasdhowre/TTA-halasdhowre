#################################Home Learning Task 2

#Q1
#Create your own Flow Diagram, a subject of your own choice, Example: Fast food order and convert it into code.

import random

#dice throw number 1 to 6
dice_throw1 = random.randint(1,6)
#die2 throw number 1 to 6
dice_throw2 = random.randint(1,6)
#die3 throw number 1 to 6
dice_throw3 = random.randint(1,6)
#display("Dice_throw1:" + dice_throw1)
print("Dice_throw1:" + str(dice_throw1))
#display("Dice_throw2:" + dice_throw2)
print("Dice_throw2:" + str(dice_throw2))
#display("Dice_throw3:" + dice_throw3)
print("Dice_throw3:" + str(dice_throw3))
#if dice_throw1 equals dice_throw2 and dice_throw2 equals dice_throw3
if dice_throw1 == dice_throw2 & dice_throw2 == dice_throw3:
    print("Three of a kind.")
#if dice_throw1 equals dice_throw2 OR dice_throw 2 equals dice_throw3 OR dice_throw1 equals dice_throw3
if dice_throw1 == dice_throw2 or dice_throw2 == dice_throw3 or dice_throw1 == dice_throw3:
    print("1 Pair.")
#else
else:
    print("Better luck next time.")

#end of loop

#end of program


#Q2
#As an extension to the motorbike task that costs £2000 and loses 10% of its value every year. 
# Set up a function that performs the calculation by passing in parameters. 
# Then using a loop, print the value of the bike every following year until it falls below £1000.

cost_of_bike = 2000

def calculate_depreciation(motorbike, amount_of_depreciation, cost_of_bike):
    while motorbike > 1000:
        print("The motorbike is:", motorbike)
        cost_of_bike = motorbike * amount_of_depreciation

calculate_depreciation(cost_of_bike, 0.9)


#Q3
#Write a program which will ask for two numbers from a user. 
#Then offer an option menu to the user giving them a choice of maths operators. 
#Once the user has selected which operator they wish to use, perform the calculation by using a procedure and passing parameters.

def procedure_num(first, second):
    first_num = first
    second_num = second

#ask for two numbers
first_num = int(input("Enter your first number:"))
second_num = int(input("Enter your second number:"))

#Choose maths character
print("Enter the operation you would like to execute.")
maths_char = input("Enter chosen maths character for selected operation +, -, *, /: ")

#selcted operations options
result = 0
if maths_char == '+':
    result = first_num + second_num
elif maths_char == '-':
    result = first_num - second_num
elif maths_char == '*':
    result = first_num * second_num
elif maths_char == '/':
    result = first_num / second_num
else:
    print("Input maths character not recognised!")

print(first_num, maths_char, second_num, "=", result)

procedure_num(first_num, second_num)

