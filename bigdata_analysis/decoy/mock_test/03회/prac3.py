import pandas as pd
import numpy as np
import time

aaa = time.time()
x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/Airline_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/Airline_test.csv")
y_train = x_train.copy()["Satisfaction"]
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/06회/Airline_y_test.csv")
x_train = x_train.drop(columns = "Satisfaction", axis=1)
# 결측치 없음
# print(x_train.isna().sum())
# print(x_test.isna().sum())
# print(y_train.isna().sum())

tmp = []

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    # print(b,len(a),i)
    # 제거 대상 없음
    if b== "object":
        tmp.append(i)

from sklearn.preprocessing import LabelEncoder as le
lle = le()

for i in tmp:
    # lle.fit(x_train[i])
    # x_train[i] = lle.transform(x_train[i])
    # x_test[i] = lle.transform(x_test[i])
    x_train[i] = lle.fit_transform(x_train[i])
    x_test[i] = lle.fit_transform(x_test[i])

y_train = y_train.map({"Yes" : 1, "No" : 0})


from sklearn.model_selection import train_test_split as tts

x,x_val,y,y_val = tts(x_train, y_train, random_state=1234, test_size=0.2, stratify = y_train)

from sklearn.ensemble import RandomForestClassifier as rf
from xgboost import XGBClassifier as xgb

# rff = rf(n_estimators = 600, max_depth = 6)
xg = xgb(n_estimators = 600, max_depth = 6)

# rf_model = rff.fit(x,y)
xgb_model = xg.fit(x,y)

# rf_pred = rf_model.predict(x_val)
xgb_pred = xgb_model.predict(x_val)


from sklearn.metrics import f1_score as f1

# rf_score = f1(y_val, rf_pred)
xgb_score = f1(y_val, xgb_pred)

print(xgb_score)

pred = xgb_model.predict(x_test)

obj = {"pred" : pred}
result = pd.DataFrame(obj)
tmp = pred.copy()
# print(result)
result["pred"] = result["pred"].map({1 : "Satisfied", 0 : "Not Satisfied"})
# print(result)

result.to_csv("result.csv", index = False)
# print(y_test)
y_test["Satisfaction"] = y_test["Satisfaction"].map({"Satisfied" : 1, "Not satisfied" : 0})
# print(y_test)
# y_test = y_test.fillna(0)
actual_score = f1(y_test["Satisfaction"], pred)
print(actual_score)


bbb = time.time()
print()
ac = bbb - aaa
print(round(ac,4),"초")