#source: https://mlcourse.ai/book/topic01/topic01_pandas_data_analysis.html

#A DataFrame can be sorted by the value of one of the variables (i.e columns). 
# For example, we can sort by Total day charge (use ascending=False to sort in descending order):

import pandas as pd

data = pd.read_csv("winemag-data-130k-v2.csv")

print(data.info())

#sorting : sort_values(by ="",ascending = False) --incase I want it to be descending 
#and in case of ascending i can skip ascending

df  = data.sort_values(by = "price", ascending=False)
print(df)

#We can also sort by multiple columns:

df1 = data.sort_values(by = ["price","points"], ascending=[True,False]).head()
print(df1)

