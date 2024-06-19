import pandas as pd

X_train = pd.read_csv("BlackFriday_X_train.csv")
X_test = pd.read_csv("BlackFriday_X_test.csv")
y_train = pd.read_csv("BlackFriday_y_train.csv")
y_test = pd.read_csv("BlackFriday_y_test.csv")


del_col = ['Product_Category_2','Product_Category_3','User_ID','Product_ID']
X_train, X_test = X_train.drop(columns=del_col), X_test.drop(columns=del_col)

need_to_change_col = []

for i in X_train.columns:
    a = X_train[i].unique()
    idx = 0
    tmp = {}
    for j in a:
        tmp[j] = idx
        idx += 1
    X_train[i] = X_train[i].map(tmp)

for i in X_train.columns:
    a = X_test[i].unique()
    idx = 0
    tmp = {}
    for j in a:
        tmp[j] = idx
        idx += 1
    X_test[i] = X_test[i].map(tmp)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import mean_absolute_error as MAE

y_train = y_train['Purchase']
y_test = y_test['Purchase']

x_tra, x_val , y_tra ,y_val = train_test_split(
    X_train, y_train,
    # stratify = y_train,
    random_state = 2022,
    test_size = 0.2
)

rf = RandomForestClassifier(n_estimators = 500, max_depth = 5, random_state = 2232)
ada = AdaBoostClassifier(n_estimators = 500, learning_rate = 0.5, random_state = 2232)
bag = BaggingClassifier(n_estimators = 500, random_state = 2232)

xgb = XGBClassifier(n_estimators = 500, learning_rate = 0.5, random_state = 2232)
lgbm = LGBMClassifier(n_estimators = 500, learning_rate = 0.5, random_state = 2232)

pre_model = [rf,lgbm]
model_name = ['rf','lgbm']
answer = []
idx = 0

import time

for i in pre_model:
    startt = time.time()
    print(model_name[idx])
    aa = i.fit(x_tra,y_tra)
    pred = aa.predict(x_val)
    score = MAE(y_val, pred)
    answer.append([model_name[idx], score])
    idx += 1
    endd = time.time()
    print(endd - startt, "초")
    print()

print(answer)


