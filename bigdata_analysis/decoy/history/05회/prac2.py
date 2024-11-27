import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_test.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/05회/carprice_y_test.csv")

y_train = x_train.copy()['price']
x_train = x_train.drop(columns = 'price' , axis = 1)

tmp = []

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    print(b, len(a), i)
    if b == 'object':
        tmp.append(i)

from sklearn.preprocessing import LabelEncoder as le

lle = le()
# model = lle.fit(x_train)
for i in tmp:
    model = lle.fit(x_train[i])
    x_train[i] = lle.transform(x_train[i])
    x_test[i] = lle.transform(x_test[i])


from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train , random_state = 1234 , test_size = 0.2)


from sklearn.ensemble import RandomForestRegressor as rf
from xgboost import XGBRegressor as xg

rff, xgg = rf() , xg()
rf_model , xg_model = rff.fit(x,y) , xgg.fit(x,y)
rf_pred , xg_pred = rf_model.predict(x_val) , xg_model.predict(x_val)

from sklearn.metrics import root_mean_squared_error as rmse

rf_score = rmse(y_val , rf_pred)
print(rf_score)

xg_score = rmse(y_val, xg_pred)
print(xg_score)

pred = xg_model.predict(x_test)

obj = {"pred" : pred}
result = pd.DataFrame(obj)
result.to_csv("result.csv" , index = False)

real_score = rmse(y_test, pred)
print(real_score)

