import pandas as pd

#DataFrame: A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.

dataframe = pd.DataFrame({'Yes':[50,100], 'No': [30,20]})

print(dataframe)

dataframe2= pd.DataFrame({'Sentence':['I liked it', 'It was awful'],'Meaning':['Pretty Good','bland']})

print(dataframe2)

dataframe3= pd.DataFrame({'Sentence':['I liked it', 'It was awful'],'Meaning':['Pretty Good','bland']},index=['Product A','Product B'])

print(dataframe3)
