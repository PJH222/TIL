import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/airquality.csv")
df_new = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/airquality_new.csv")

tmp = df[['Solar.R','Wind','Temp','Ozone']]

import statsmodels.api as sm

y = tmp['Ozone']
x = tmp.drop(columns = "Ozone" , axis = 1)
x = sm.add_constant(x)

model = sm.OLS(y,x).fit()
print(model.summary())

answer = round(0.0637 , 2)
print(answer)

answer = round(0.028 , 2)
print(answer)

# print(df_new)
y = df_new['Ozone']
x = df_new[['Solar.R','Wind','Temp']]
x = sm.add_constant(x)



pred = model.get_prediction(x)
print(pred.summary_frame().iloc[8])

answer = round(94.694921,2)
print(answer)

