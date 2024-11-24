import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/job_change_X_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/job_change_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/job_change_y_train.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/job_change_y_test.csv")

# print(x_train.isna().sum())
# print()
# print(x_test.isna().sum())
# print()

cond = (x_train.isna().sum() > 2000)
tmp = x_train.columns[cond]

x_train = x_train.drop(columns = tmp , axis = 1)
x_test = x_test.drop(columns = tmp , axis = 1)

cond = (x_train.isna().sum() > 0)
tmp = x_train.columns[cond]

for i in tmp:
    mode1 = x_train[i].value_counts().idxmax()
    mode2 = x_test[i].value_counts().idxmax()
    # print(mode1, mode2)
    x_train[i] = x_train[i].fillna(mode1)
    x_test[i] = x_test[i].fillna(mode2)

tmp = []

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    print(b, len(a), i)
    c = x_test[i].unique()
    d = x_test[i].dtypes
    # print(d, len(c), i)
    # print(a,c)

    if b == "object":
        tmp.append(i)

id = y_test["enrollee_id"].copy()

x_train = x_train.drop(columns = ["enrollee_id","city"], axis = 1)
x_test = x_test.drop(columns = ["enrollee_id","city"], axis = 1)

y_train = y_train.drop(columns = "enrollee_id", axis = 1)
y_test = y_test.drop(columns = "enrollee_id", axis = 1)

print(x_train.info())

from sklearn.preprocessing import OneHotEncoder as oo

x_train_cate = x_train.select_dtypes("object").copy()
x_test_cate = x_test.select_dtypes("object").copy()

enc = oo(sparse_output = False, handle_unknown = 'ignore').fit(x_train_cate)

x_train_oo = enc.transform(x_train_cate)
x_test_oo = enc.transform(x_test_cate)

x_train_ = x_train.select_dtypes(exclude = "object").copy()
x_test_ = x_test.select_dtypes(exclude = "object").copy()

x_train = np.concatenate([x_train_, x_train_oo], axis = 1)
x_test = np.concatenate([x_test_, x_test_oo], axis = 1)

y_train = np.ravel(y_train)

from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train, random_state = 1234, 
                            test_size = 0.2, stratify = y_train)

from sklearn.ensemble import RandomForestClassifier as rf
from xgboost import XGBClassifier as xgb
from lightgbm import LGBMClassifier as lgb

rff = rf()
rf_model = rff.fit(x,y)
rf_pred = rf_model.predict(x_val)

xg = xgb(n_estimators = 500, max_depth = 6)
xg_model = xg.fit(x,y)
xg_pred = xg_model.predict(x_val)
# print(rf_pred)

lg = lgb(n_estimators = 500, max_depth = 6)
lg_model = lg.fit(x,y)
lg_pred = lg_model.predict(x_val)

from sklearn.metrics import auc, roc_curve

a,b,c = roc_curve(y_val, lg_pred)
rf_score = auc(a,b)
print(rf_score)

actual_pred =  lg_model.predict(x_test)
a,b,c = roc_curve(y_test, actual_pred)
rf_score = auc(a,b)
print(rf_score)