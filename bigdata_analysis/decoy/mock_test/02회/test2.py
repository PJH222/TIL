import pandas as pd

X_train = pd.read_csv("BlackFriday_X_train.csv")
X_test = pd.read_csv("BlackFriday_X_test.csv")
y_train = pd.read_csv("BlackFriday_y_train.csv")
y_test = pd.read_csv("BlackFriday_y_test.csv")

# print(X_train.info())
# col = X_train.columns[:5]
# print(X_train[col])

# print(X_train.isna().sum()) # 'Product_Category_2', 'Product_Category_3', 결측치가 많아서 drop해야 함.

del_col = ['Product_Category_2', 'Product_Category_3', 'User_ID', 'Product_ID']

X_train, X_test = X_train.drop(columns = del_col), X_test.drop(columns = del_col)


for i in X_train.columns:
    a = X_train[i].unique()
    # print(i)
    # print(i, ":",sorted(a)) # 'User_ID', 'Product_ID' drop할 것
    # print(X_train[i].value_counts())
    # print()

# 진짜로 원핫인코딩말고는 방법이 없는건가???
# print(X_train.info())
for i in X_train.columns:
    if X_train[i].dtypes == "int64":
        X_train[i] = X_train[i].astype('object')

    if X_test[i].dtypes == "int64":
        X_test[i] = X_test[i].astype('object')

from sklearn.model_selection import train_test_split

# print(X_train.info())
print(y_train)
y_train = y_train.drop(columns = 'User_ID')
# y_train = y_train['']으로 해버리면, df에서 시리즈로 변환되어벌임...

X_tra , X_val, y_tra , y_val = train_test_split(
    X_train, y_train, random_state=2022, test_size = 0.3
)

print(X_tra.shape, X_val.shape, y_tra.shape)

X_tra_col = X_tra.select_dtypes('object').copy()
X_test_col = X_test.select_dtypes('object').copy()
X_val_col = X_val.select_dtypes('object').copy()

from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(sparse_output=False).fit(X_tra_col)

X_tra_ohe = enc.transform(X_tra_col)
X_test_ohe = enc.transform(X_test_col)
X_val_ohe = enc.transform(X_val_col)

# print(X_tra_ohe)

import numpy as np

X_TEST = X_test_ohe
X_TRAIN = X_tra_ohe
X_VAL = X_val_ohe

y_TRAIN = y_tra.values.ravel()
y_VAL = y_val.values.ravel()

# print(X_TEST.shape, X_TRAIN.shape)

from sklearn.ensemble import BaggingClassifier as bag, AdaBoostClassifier as ada, RandomForestClassifier as rf
from sklearn.tree import DecisionTreeClassifier as dt
from xgboost import XGBClassifier as xgb
from lightgbm import LGBMClassifier as lgbm
from sklearn.metrics import mean_absolute_error as MAE

bagg = bag(dt(max_depth=5),random_state = 2024)
adaa = ada(dt(max_depth=5), random_state = 2024, learning_rate = 0.5)
rff = rf(max_depth=5 , random_state= 2024)
xgbb = xgb(max_depth = 5, random_state=2022)
lgbmm = lgbm(max_depth = 5, random_state=2022)

model_list = [bagg,adaa,lgbmm]
model_name = ['bag','ada','lgbm']
answer = []
idx = 0
for i in model_list:
    print(f"{model_name[idx]}","를 모델링 중입니다.")
    modeling = i.fit(X_TRAIN,y_TRAIN)
    score = modeling.predict(X_VAL)
    mae = MAE(y_VAL, score)
    answer.append([model_name[idx], mae])
    idx += 1

print(answer)