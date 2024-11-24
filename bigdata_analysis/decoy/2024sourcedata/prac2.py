import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/2024sourcedata/6_x_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/2024sourcedata/6_x_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/2024sourcedata/6_y_train.csv")

tmp = []

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes

    if b == "object":
        tmp.append(i)

    # print(b,len(a),i)

# carID 삭제 필요
carID = x_test["carID"].copy()
x_train = x_train.drop(columns = "carID", axis = 1)
x_test = x_test.drop(columns = "carID", axis = 1)
y_train = y_train.drop(columns = "carID", axis = 1)

# print(y_train)

from sklearn.preprocessing import LabelEncoder as le

lle = le()

for i in tmp:
    lle.fit(x_train[i])
    x_train[i] = lle.transform(x_train[i])
    x_test[i] = lle.transform(x_test[i])


y_train = np.ravel(y_train)

from sklearn.model_selection import train_test_split as tts

x , x_val, y , y_val = tts(x_train, y_train, test_size = 0.2, random_state = 1234)


from sklearn.ensemble import RandomForestRegressor as rf
from xgboost import XGBRegressor as xgb

rff , xg = rf() , xgb()
rff_model , xg_model = rff.fit(x,y) , xg.fit(x,y)
rff_pred , xg_pred = rff_model.predict(x_val), xg_model.predict(x_val)


from sklearn.metrics import root_mean_squared_error as rmse

rf_score, xg_score = rmse(y_val, rff_pred), rmse(y_val, xg_pred)

print(round(rf_score, 5) , round(xg_score, 5))

pred = xg_model.predict(x_test)

obj = {"carID" : carID, "price" : pred}
result = pd.DataFrame(obj)
result.to_csv("result.csv", index = False)

