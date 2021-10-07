#
name <- "username"
name <- "Hala Shakib Dhowre"
print(name)

#
name <- readline("Enter your name:")
hello <- paste("Welcome", name, "!")

#
Title <-"Women in Data"
Type <- paste ("Type of title:", typeof(title))
print(type)

pi <- 3.1415
dozen <-12L
print(paste("Type of pi:", typeof(pi)))
print(paste("Type of dozen:" typeof(dozen)))
flag <- T
print(paste("is flag logical:", is logical(flag)))

#
info <-list(21, 61.2, "L", TRUE)
info <- list(age=21, weight=61.2, name="Lisa", female=TRUE)

X <- c(1, 2, 3, 4, 5)
Y <- c(21, 5, 7, 9, 5)
plot(x, y, type="o")

###################Home Learning Task R_1
#(1)Write a R program to take input from the user (name and age) and display the values. 

name <- readline("Enter name:")
age <- readline("Enter age:")
hello <- paste("Welcome", name, "you are now", age, "nex year you will be a year older")
print(Hello)
day <- list(age=41, Weight="67", name="Joey", female="True")
print(day)

#(2)Write a R program to get the details of the objects in memory.
#Hint: how do you list all the local variables?

name <- "R";
numbers=c(13,29,32,46,52,60,71,87,98,101)
print(numbers)
print("Details of the objects in memory:")
print(numbers.str())
  
#(3)Write a R program to create a sequence of numbers from 20 to 50 and find the mean of numbers from 20 
#to 60 and sum of numbers from 51 to 91.

Hello <- print("Sequence of numbers from 20 to 50:")
print(seq(20,50))

print ("Mean of numbers 20 to 60:")
print(mean(20:60))

print("Sum of numbers from 51 to 91:")
print(sum(51:91))

#(4)Write a R program to create a vector which contains 10 random integer values between -50 and +50

vector <- values(-50:50, 10, replace=TRUE)
print("Content of the vector:)
print("10 random integer values between -50 and +50:")
print(vector)

