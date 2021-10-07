#################################Home Learning Task 4

#Create a CSV file of 15 holiday destinations for a website 
#(1)Add in a column of destinations
#(2)Add in a column that shows feedback score out of 10 for that destination
#(3)Add in a column for average hotel star rating for those destinations 
#(4)Add in a column for number of all-inclusive hotels within each destination
#(5)Add in the most visited city in each destination

#(1)How many rows and columns are there in your file?

import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
DataFrame = pd.read_csv('Destinations.csv')
DataFrame.shape

#(2)Print row 3-8 ( using iloc/loc).

import pandas as pd
DataFrame = pd.read_csv("Destinations.csv")
print(DataFrame.iloc[2:8])

#(3)Find the mean number of all-inclusive hotels across all destinations.

import pandas as pd
DataFrame = pd.read_csv("Destinations.csv")
DataFrame["Hotel all-inclusive"].mean()

#(4)Find the lowest scoring destination.

import pandas as pd
DataFrame = pd.read_csv("Destinations.csv")
DataFrame["Feedback Score"].min()

#(5)Find the highest scoring destination.

import pandas as pd
DataFrame = pd.read_csv("Destinations.csv")
DataFrame["Feedback Score"].max()

#(6)Find all the destinations where there are more than 9 all-inclusive hotels. 

import pandas as pd
DataFrame = pd.read_csv("Destinations.csv")
f_filter = DataFrame["Hotel all-inclusive"]>9

f_filter

#(7)Filter the data by score above 8. 

import pandas as pd
DataFrame = pd.read_csv("Destinations.csv")
above8 = DataFrame["Feedback Score"]>8
above8

#(8)Filter the data score below 2 ( I need to know if these destinations should be removed or there is a problem) 

print(DataFrame,)
lower2 = DataFrame["Feedback Score"]<2
lower2

#Extension 
#(1)Is there a correlation between number of all-inclusive hotels and score?
#(2)Create a data visualisation diagram to show destination and highest scores?

import pandas as pd
DataFrame = pd.read_csv("Destinations.csv")

from sklearn.cluster import KMeans
from sklearn import datasets
import numpy as np
import matplotlib_inline as plt
from sklearn.datasets import load_iris
iris = datasets.load_iris()

DataFrame=pd.read_csv("Destinations.csv")
DataFrame.head(15)

DataFrame.plot.scatter(x="Hotel all-inclusive", y="Feedback Score")

columns= ["Hotel all-inclusive", "Most Visited City", "Feedback Score"]
DataFrame[columns].plot.area()

DataFrame.groupby("Destination ").mean().plot.bar()
