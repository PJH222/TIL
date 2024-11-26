import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/airquality.csv")
df_new = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/airquality_new.csv")

# # print(df.columns) ['Ozone', 'Solar.R', 'Wind', 'Temp']

# import statsmodels.api as sm

# x = df[['Solar.R', 'Wind', 'Temp']]
# y = df['Ozone']

# x = sm.add_constant(x)

# a = sm.OLS(y,x).fit()

# print(a.summary())

# answer = round(0.0637 , 2)
# print(answer)

# answer = round(2.234,2)
# print(answer)

# x_new = df_new[['Solar.R', 'Wind', 'Temp']]

# x_new = sm.add_constant(x_new)
# a_new = a.get_prediction(x_new)

# print(a_new.summary_frame().iloc[9])
# print()

# df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/cancer.csv")

# print(df.value_counts())
# print(df.isna().sum())

# a = [964 , 627 , 328 , 81]
# b = [0.05, 0.05, 0.1, 0.8]

# for i in range(4):
#     b[i] = b[i] * sum(a)

# answer = a[3]
# print(answer)

# from scipy.stats import chisquare as ch

# a = ch(a , b)
# answer = int(round(a[0] ,0 ))

# print(answer)


# answer = int(round(a[1] , 0))
# print(answer)

# print(df.columns)

import statsmodels.api as sm

col = ['Solar.R','Wind','Temp']

y = df["Ozone"]
x = df[col]
x = sm.add_constant(x)

model = sm.OLS(y,x).fit()
print(model.summary())

answer = round(0.0637 , 2)
print()
print(answer)


answer = round(2.234 , 2)
print()
print(answer)


x = df_new[col]
x = sm.add_constant(x)

a = model.get_prediction(x)
# print(a.summary_frame().iloc[9])

answer = round(91.763178 , 2)
print(answer)