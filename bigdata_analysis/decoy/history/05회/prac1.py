import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_test.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_y_test.csv")
y_train = x_train.copy()["price"]
x_train = x_train.drop(columns = "price", axis = 1)

tmp = []

for i in x_train.columns:
    if x_train[i].dtypes == "object":
        tmp.append(i)
        # 라벨인코딩 대상리스트

from sklearn.preprocessing import LabelEncoder as le

lle = le()

for i in tmp:
    lle.fit(x_train[i])
    x_train[i] = lle.transform(x_train[i])
    x_test[i] = lle.transform(x_test[i])

from sklearn.model_selection import train_test_split as tts

x, x_val , y , y_val = tts(x_train, y_train, random_state = 1234, test_size = 0.2)


from sklearn.ensemble import RandomForestRegressor as rf
from xgboost import XGBRegressor as xgb

rff = rf()
xg = xgb()

rf_model = rff.fit(x,y)
xgb_model = xg.fit(x,y)

rf_pred = rf_model.predict(x_val)
xgb_pred = xgb_model.predict(x_val)

from sklearn.metrics import root_mean_squared_error as rmse

rf_rmse = rmse(y_val, rf_pred)
xgb_rmse = rmse(y_val, xgb_pred)

print(rf_rmse, xgb_rmse)

actual_pred = xgb_model.predict(x_test)

# print(actual_pred)

obj = {"pred" : actual_pred}
result = pd.DataFrame(obj)

result.to_csv("result.csv", index = False)

actual_score = rmse(y_test, actual_pred)
print("실제 점수 : ",actual_score)
