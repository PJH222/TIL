import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/mtcars.csv")

# print(df.columns) disp, hp, drat , wt

import statsmodels.api as sm

df = df[['disp','hp','drat','wt','mpg']] 

corr = df.corr()['mpg']
print(corr)

y = df["mpg"]
x = df[['disp','hp','drat','wt']]
x = sm.add_constant(x)

a = sm.OLS(y,x).fit()
print(a.summary())

answer = round(7.5366 , 3)
print(answer)

answer = round(0.838 , 3)
print(answer)

answer = round(0.0038 , 3)
print(answer)


