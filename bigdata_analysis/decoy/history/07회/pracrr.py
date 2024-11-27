import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/mtcars.csv")


import statsmodels.api as sm

col = ['disp','hp','drat','wt','mpg']

print(df[col].corr())

answer = round(-0.867659 , 3)
print(answer)


y = df["mpg"]
x = df[col].drop(columns = "mpg", axis = 1) 
x = sm.add_constant(x)

a = sm.OLS(y,x).fit()
# print(a.summary())

answer = round(0.838 , 3)
print(answer)

answer = round(0.0038 , 3)
print(answer)
