import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/stroke_X_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/stroke_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/stroke_y_train.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/stroke_y_test.csv")

id = x_test["id"].copy()
tmp = []

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    # print(b , len(a), i)
    if b == "object":
        tmp.append(i)

# id 제거 필요
x_train = x_train.drop(columns = "id" , axis = 1)
x_test = x_test.drop(columns = "id" , axis = 1)
y_train = y_train.drop(columns = "id" , axis = 1)
y_test = y_test.drop(columns = "id" , axis = 1)
# print(y_train)

from sklearn.preprocessing import LabelEncoder as le

lle = le()

for i in tmp:
    lle.fit(x_train[i])
    x_train[i] = lle.transform(x_train[i])
    x_test[i] = lle.transform(x_test[i])

y_train = np.ravel(y_train)
from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train, random_state = 1234 , 
                            test_size = 0.2 , stratify = y_train)


from sklearn.ensemble import RandomForestClassifier as rf
from xgboost import XGBClassifier as xgb
from lightgbm import LGBMClassifier as lgb

rff, xg, lg = rf(n_estimators = 500, max_depth = 7) , xgb(n_estimators = 500, max_depth = 7) , lgb(n_estimators = 300)
rf_model, xg_model, lg_model = rff.fit(x,y), xg.fit(x,y), lg.fit(x,y)
rf_pred, xg_pred, lg_pred = rf_model.predict(x_val), xg_model.predict(x_val), lg_model.predict(x_val)

from sklearn.metrics import accuracy_score as ass
rf_score, xg_score, lg_score = ass(y_val, rf_pred) , ass(y_val, xg_pred) , ass(y_val, lg_pred)

print()
print()
print()

print(round(rf_score,5),round(xg_score,5),round(lg_score,5))

actual = xg_model.predict(x_test)

obj = {"id" : id , "stroke" : actual}
result = pd.DataFrame(obj)
result.to_csv("result.csv", index = False)




