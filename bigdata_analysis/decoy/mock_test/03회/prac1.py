import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/train_insurance.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/test_insurance.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/03회/insurance_y_test.csv")

y_train = x_train.copy()["charges"]
x_train = x_train.drop(columns = "charges")

tmp = []
for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    print(b, len(a), i)
    if b == "object":
        tmp.append(i)

from sklearn.preprocessing import LabelEncoder as le

lle = le()
for i in tmp:
    x_train[i] = lle.fit_transform(x_train[i])
    x_test[i] = lle.fit_transform(x_test[i])


from sklearn.model_selection import train_test_split as tts

x, x_val , y, y_val = tts(x_train, y_train, random_state = 1234, test_size = 0.35)

from sklearn.ensemble import RandomForestRegressor as rf
from xgboost import XGBRegressor as xgb

rf_model = rf().fit(x,y)
xgb_model = xgb().fit(x,y)

rf_pred = rf_model.predict(x_val)
xgb_pred = xgb_model.predict(x_val)

from sklearn.metrics import mean_absolute_percentage_error as mape

rf_mape = mape(rf_pred, y_val)
xgb_mape = mape(xgb_pred, y_val)

print(rf_mape, xgb_mape)

pred = xgb_pred

obj = {"pred" : pred}
result = pd.DataFrame(obj)
result.to_csv("result.csv", index = False)

actual_pred = xgb_model.predict(x_test)
actual_score = mape(y_test, actual_pred)
print()
print(actual_score)
