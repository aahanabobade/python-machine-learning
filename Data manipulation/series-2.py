import pandas as pd

#series: A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. 
# And in fact you can create one with nothing more than a list:

series1 = pd.Series([1,2,3,4,5])

print(series1)

"""
A Series is, in essence, a single column of a DataFrame. 
So you can assign row labels to the Series the same way as before, using an index parameter. 
However, a Series does not have a column name, it only has one overall name:
"""

series2 = pd.Series([30,10,50], index = ['day 1 sales','day 2 sales','day 3 sales'],name ='product a')

print(series2)

"""
The Series and the DataFrame are intimately related. 
It's helpful to think of a DataFrame as actually being just a bunch of Series "glued together". 


"""