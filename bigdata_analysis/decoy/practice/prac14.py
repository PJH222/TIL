import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/StudentsPerformance.csv")
df["gender"] = df["gender"].map({"male" : 1, "female" : 0})
df = pd.get_dummies(df , columns = ["race"], drop_first = True)
# print(tmp)



# df = df.copy().drop(columns = "gender", axis = 1)

for i in df.columns:
    a = df[i].dtypes
    if a == "bool":
        df[i] = df[i].map({True : 1 , False : 0})

train = df.copy().iloc[0:800]
test = df.copy().iloc[800:1000]


print(train, test)

y_train = train["gender"]
x_train = train.drop(columns = "gender", axis = 1)

import statsmodels.api as sm

# print(x_train, y_train)

# x_train = sm.add_constant(x_train)
a = sm.GLM(y_train, x_train, family = sm.families.Binomial()).fit()


# print(a.summary())

answer = (round(np.exp(0.3770) , 2))
# print(answer)

answer = 466.94
# print(answer)



x_test = test.copy().drop(columns = "gender", axis = 1)

y_pred = a.predict(x_train)
print(y_pred)

