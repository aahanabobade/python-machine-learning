"""
Pandas is a powerful Python library that makes it easy to analyze data. 
It is especially useful for working with data stored in table formats such as .csv, .tsv, or .xlsx. With Pandas, you can easily load, process, and analyze data using SQL-like commands. 
When used in conjunction with Matplotlib and Seaborn, Pandas provides a wealth of opportunities for visualizing and analyzing tabular data.


The core data structures in Pandas are Series and DataFrames. 
A Series is a one-dimensional indexed array of a single data type, while a DataFrame is a two-dimensional table where each column contains data of the same type. 
Think of a DataFrame as a collection of Series objects. 
DataFrames are ideal for representing real-world data, with each row representing an instance (such as an observation) and each column representing a feature of that instance.

"""

import pandas as pd

data = pd.read_csv("winemag-data-130k-v2.csv")

print(data.head())
print(data.shape) #(129971 rows, 14 columns)
print(data.columns) 

print(data.info()) 

#bool, int64, float64 and object are the data types of our features. 
# data["title"]=data["title"].astype("int64")

"""
The describe method shows basic statistical characteristics of each numerical feature (int64 and float64 types): number of non-missing values, mean, standard deviation, range, median, 0.25 and 0.75 quartiles.
"""
print(data.describe())


#In order to see statistics on non-numerical features, one has to explicitly indicate data types of interest in the include parameter.
print(data.describe(include="object"))

"""
For categorical (type object) and boolean (type bool) features we can use the value_counts method. 
Let’s take a look at the distribution of Churn:
"""
data["description"].value_counts()

#To calculate fractions, pass normalize=True to the value_counts function.
data["description"].value_counts(normalize=True)

