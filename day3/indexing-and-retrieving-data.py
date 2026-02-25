#source: https://mlcourse.ai/book/topic01/topic01_pandas_data_analysis.html


#A DataFrame can be indexed in a few different ways.

#To get a single column, you can use a DataFrame['Name'] construction. 
import pandas as pd
import numpy as np
data = pd.read_csv("winemag-data-130k-v2.csv")

meann = data["price"].mean()

print(meann)

"""
Boolean indexing with one column is also very convenient. 
The syntax is df[P(df['Name'])], where P is some logical condition that is checked for each element of the Name column. 
The result of such indexing is the DataFrame consisting only of the rows that satisfy the P condition on the Name column.
"""
#df[(df["Churn"] == 0) & (df["International plan"] == "No")]["Total intl minutes"].max()
#[(df["Churn"] == 0) & (df["International plan"] == "No")] --- P(SHOWS CONDITION)

np.float64(35.363389129985535)

#What are the average values of numerical features for churned users?

#Here we’ll resort to an additional method select_dtypes to select all numeric columns.

#df.select_dtypes(include=np.number)[df["Churn"] == 1].mean()


"""
DataFrames can be indexed by column name (label) or row name (index) or by the serial number of a row. 
The loc method is used for indexing by name, while iloc() is used for indexing by number.
"""
print(data.loc[0:6,"country":"province"])

print(data.iloc[0:5,0:3])

#If we need the first or the last line of the data frame, we can use the df[:1] or df[-1:] construction:

print(data[-1:])