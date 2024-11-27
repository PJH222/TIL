import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/airquality.csv")
new_df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/airquality_new.csv")

col = ['Solar.R','Wind','Temp','Ozone']
df = df[col]
df = df.dropna()

import statsmodels.api as sm

y = df["Ozone"]
x = df.drop(columns = "Ozone" , axis = 1)
x = sm.add_constant(x)

a = sm.OLS(y,x)
b = a.fit()

# print(b.summary())

answer = round(0.0637 , 2)
print(answer)

answer = round(2.234 , 2)
print(answer)

new_df = new_df[col]
new_df = new_df.drop(columns = "Ozone" , axis = 1)
new_df = sm.add_constant(new_df)

c = b.get_prediction(new_df)
# print(c.summary_frame().iloc[9])

answer = round(91.763178 , 2)
print(answer)


