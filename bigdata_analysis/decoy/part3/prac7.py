import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

coll = ['Rev_per_mile','Length','EngineSize','Weight','Price']

data = da[coll].copy().dropna()

y = data['Price']
x = data[['Rev_per_mile','Length','EngineSize','Weight']]

import statsmodels.api as sm
x = sm.add_constant(x)

model = sm.OLS(y,x)
result = model.fit()

# print(result.summary())
answer_a = 0.396
answer_b = 0.0023
answer_c = 0.158
answer_d = 0.005

