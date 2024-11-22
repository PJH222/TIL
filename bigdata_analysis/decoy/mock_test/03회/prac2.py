import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/Flight_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/Flight_test.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/07회/Flight_y_test.csv")

y_train = x_train.copy()["price"]
x_train = x_train.copy().drop(columns = "price")

# 결측치 없음
x_train = x_train.drop("flight", axis = 1)
x_test = x_test.drop("flight", axis = 1)

# print(x_train.head())
col = []
for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    # print(b, len(a), i)
    if b == "object":
        col.append(i)


from sklearn.preprocessing import LabelEncoder as le

lle = le()

for i in col:
    x_train[i] = lle.fit_transform(x_train[i])
    x_test[i] = lle.fit_transform(x_test[i])

# print(x_train.head())

from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train, random_state = 1234, test_size = 0.2)


from sklearn.ensemble import RandomForestRegressor as rf
from xgboost import XGBRegressor as xgb

rf_model = rf().fit(x,y)
xgb_model = xgb().fit(x,y)

rf_pred = rf_model.predict(x_val)
xgb_pred = xgb_model.predict(x_val)


from sklearn.metrics import root_mean_squared_error as mse

rf_rmse = mse(y_val, rf_pred)
xgb_rmse = mse(y_val, xgb_pred)

print()
print(rf_rmse, xgb_rmse)

pred = xgb_model.predict(x_test)
obj = {"pred" : pred}
result = pd.DataFrame(obj)

result.to_csv("result.csv", index = False)

score = mse(y_test, pred)
print(score)

