import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/2024sourcedata/x_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/2024sourcedata/x_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/2024sourcedata/y_train.csv")

# cust_id , 환불금액 제거
tmp1 = []

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    # print(b, len(a), i)
    if b == "object":
        tmp1.append(i)

cust_id = x_test["cust_id"].copy()

tmp = ["cust_id", "환불금액"]

x_train = x_train.drop(columns = tmp , axis = 1)
x_test = x_test.drop(columns = tmp , axis = 1)
y_train = y_train.drop(columns = "cust_id", axis = 1)
from sklearn.preprocessing import LabelEncoder as le

lle = le()

for i in tmp1:
    lle.fit(x_train[i])
    x_train[i] = lle.transform(x_train[i])
    x_test[i] = lle.transform(x_test[i])

y_train = np.ravel(y_train)

from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train, 
                            random_state = 1234 , 
                            test_size = 0.2)

from sklearn.ensemble import RandomForestClassifier as rf
from xgboost import XGBClassifier as xgb
from lightgbm import LGBMClassifier as lgb

rff, xg , lg = rf() , xgb() , lgb()
rf_model, xg_model, lg_model = rff.fit(x,y) , xg.fit(x,y) , lg.fit(x,y)
rf_pred , xg_pred , lg_pred = rf_model.predict_proba(x_val)[:,1],xg_model.predict_proba(x_val)[:,1],lg_model.predict_proba(x_val)[:,1]


from sklearn.metrics import roc_curve, auc

a,b,c = roc_curve(y_val , rf_pred)
rf_score = auc(a,b)

a,b,c = roc_curve(y_val, xg_pred)
xg_score = auc(a,b)

a,b,c = roc_curve(y_val, lg_pred)
lg_score = auc(a,b)

print(rf_score , xg_score , lg_score)

pred = rf_model.predict_proba(x_test)[:,1]

obj = {"cust_id" : cust_id, "gender" : pred}
result = pd.DataFrame(obj)
result.to_csv("result.csv", index = False)
