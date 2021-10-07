#################################Home Learning Task 3

#Q1
#Write a program that allows you to enter 4 numbers and stores them in a file called “Numbers”
#• 3
#• 45
#• 83
#• 21
#Have a go at ‘w’ ‘r’ ‘a’

file_1 = open("GitHub/TTA-halasdhowre/Submitted HLT/Numbers.txt", "r")
print(file_1.read())
file_1.close()

#Q2
#Write a program to ask a student for their percentage mark and convert this to a grade.

def mark_grade (precentage):
    print("Hello, to findout your grade follow the instructions:")
    name= input("Please enter your name:")
    percentage=int(input("Please Enter your percentage mark:"))
    if percentage <30 or percentage <= 39:
        print("Unfortunatly,", name +" ,you have not passed this module:" "grade: Fail")
    elif percentage > 39 and percentage <49:
        print(name +" ,you have have passed the module:" "grade: Pass")
    elif percentage >=50 and percentage <69:
        print(name+",you have passed the module:" "grade: Merit")
    elif percentage >=70 and percentage <= 100:
        print("Excellent", name+", you have succesfully passed the module:""grade: Distinction")
    else:
        print("Error")
    return name

x = mark_grade("name")
print(x)


#Q3
#(1)Create a 1D array of numbers from 0 to 9

import numpy as np
array = np.array([0,1,2,3,4,5,6,7,8,9])
print(array)

#(2)Create a 3×3 NumPy array of all Boolean value Trues

array = np.array([True, False, True, 3, 2, False, 5, True, 9])
new_array = array.reshape(3,3)
print(new_array)

#(3)Extract all odd numbers from array of 1-10

array = np.array([1,2,3,4,5,6,7,8,9])
array[array % 2 == 1]

#(4)Replace all odd numbers in an array of 1-10 with the value -1

array = np.array([1,2,3,4,5,6,7,8,9])
array[array % 2 == 1] = -1

#(5)Convert a 1D array to a 2D array with 2 rows

array = np.array([0,1,2,3,4,5,6,7,8,9])
print('1D Numpy array:')
print(array)
array_2d = np.reshape(array, (2, 5))
print('2D Numpy array:')
print(array_2d)

#(6)Create two arrays a and b, stack these two arrays vertically use the np.dot and np.sum to calculate totals

a=np.array([3,7,9])
b=np.array([2,1,8])
c=np.dot(a,b)
sum=np.sum(c)
print(c)




