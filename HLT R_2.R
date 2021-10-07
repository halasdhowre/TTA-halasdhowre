
####################Home Learning Task R_2 Compulsory Task

#Imagine the following scenario:
#You are a data analyst at an organisation. 
#You have been given a data set and asked to create a meaningful data visualisation using this data. 
#Using the ggplot in-built data sets in RStudio and the qplot
#function, get your creative juices flowing and create a meaningful 
#and impactful data visualization using your preferred data set.

install.packages("ggplot2")
library(ggplot2)
data(package = "ggplot2")
ggplot2::mpg                         
ggplot(data=msleep, x=weight, y=height, geom="point", colour=class)
ggplot(msleep, aes(x, y, colour)) + geom_point()



####################Home Learning Task R_2 Additional Tasks(A)

#(1)Write an R program to create three vectors a, b, c with 5 integers. 
#Combine the three vectors to become a 3×5 matrix where each column represents a vector. 
#Print the content of the matrix. Plot a graph and label correctly.

x <-c(5,7,9)
y <-c(2,4,8)
z <-c(1,3,6)
m <-cbind(x,y,z)
print("Content of the said matrix:")
print(m)
ggplot(m, aes(x, y, z)) + geom_line()

#(2)Write a R program to create a Data frames which contain details of 5 employees and display the details. 
#(Name, Age, Role and Length of service). 

employees_name <- c("Parker","Strange","T'Challa","Bruce","Loki")
employees_age <- c(16,45,32,45,1009)
employees_sex <- c("male", "male", "male", "male", "male")
employees_role <- c("intern","MD","King","PhD","DemiGod")
employees_lengh <- c(8,10,8,15,1009)
frame <- data.frame(employees_name,employees_age,employees_sex,employees_role,employees_lengh)
print(frame)

####################Home Learning Task R_2 Optional Challenge

#(1)Write a R program to get the first 10 Fibonacci numbers.

Fibonacci <- numeric(10)
Fibonacci[1] <- Fibonacci[2] <- 1
for (i in 3:10) Fibonacci[i] <- Fibonacci[i - 2] + Fibonacci[i - 1]
print("First 10 Fibonacci numbers:")
print(Fibonacci)

#(2)Write a R program to print the numbers from 1 to 100 
# and print "Fizz" for multiples of 3, print "Buzz" for 
#multiples of 5, and print "FizzBuzz" for multiples of both.

for (n in 1:100) {
  if (n %% 3 == 0 & n %% 5 == 0) {print("FizzBuzz")}
  else if (n %% 3 == 0) {print("Fizz")}
  else if (n %% 5 == 0) {print("Buzz")}
  else print(n)
}
