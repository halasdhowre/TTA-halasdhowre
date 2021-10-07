#################################Home Learning Task 5

#Go to: https://archive.ics.uci.edu/ml/datasets.php
#(1)Select a dataset.
#(2)Then create a data dashboard using Altair
#(3)Then create a markdown cell explain why you have decided on the design choices, what influenced 
#your decisions and what insights have you found from the data.
#(4)Aim to have linking charts

from pandas.core.frame import DataFrame
import altair as alt 
import pandas as pd

DataFrame = pd.read_csv("buddymove_holiday.csv")

DataFrame.head()

bars = alt.Chart(DataFrame).mark_bar().encode(
                                 x = "Nature",
                                 y ="Picnic"
                                 )
bars

brush=alt.selection_interval()

bars = alt.Chart(DataFrame).mark_bar().encode(
                                 x = "Nature",
                                 y ="Picnic"
                                 ).interactive()       

bars

well = alt.Chart(DataFrame).mark_point().encode(
                                 x = "Nature",
                                 y ="Picnic"   
                                 ).add_selection(brush)                                
well 