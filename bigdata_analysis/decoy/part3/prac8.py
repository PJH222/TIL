import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/job.csv")

da['x2'] = da['x2'].map({"M" : 1 , "F" : 0})

y = da['y']
x = da[['x1','x2','x3']]

import statsmodels.api as sm

x = sm.add_constant(x)

model = sm.GLM(y,x,family = sm.families.Binomial())
result = model.fit()

print(result.summary())

answer_a = round(-0.8077, 3)
print(answer_a)

import numpy as np

odds_ratio = round(np.exp(-0.1575), 3)
answer_b = odds_ratio
print(answer_b)

aa = result.predict(x)[8]
print(aa)

if aa >= 0.7:
    print(1)
else:
    print(0)

