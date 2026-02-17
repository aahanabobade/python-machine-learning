#Reading data files

"""
Being able to create a DataFrame or Series by hand is handy. 
But, most of the time, we won't actually be creating our own data by hand. 
Instead, we'll be working with data that already exists.

"""
"""
Data can be stored in any of a number of different forms and formats. 
By far the most basic of these is the humble CSV file. 
When you open a CSV file you get something that looks like this:

Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11

So a CSV file is a table of values separated by commas. 
Hence the name: "Comma-Separated Values", or CSV.

"""
"""
We'll use the pd.read_csv() function to read the data into a DataFrame. This goes thusly:
"""
import pandas as pd

wine_review = pd.read_csv("winemag-data-130k-v2.csv")

#We can use the shape attribute to check how large the resulting DataFrame is:

print(wine_review.shape) #output: (129971, 14)

"""
We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
"""

print(wine_review.head())

"""
The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. 
For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically. 
To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.

"""

wine_review1 = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

print(wine_review1.head())


