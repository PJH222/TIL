import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/weatherAUS_X_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/weatherAUS_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/weatherAUS_y_train.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/weatherAUS_y_test.csv")

# print(x_train.shape, x_test.shape)

print(x_train.isna().sum())
print()
print(x_test.isna().sum())

cond = (x_train.isna().sum() > 6000)
tmp = x_train.columns[cond] # 제거대상

x_train = x_train.drop(columns = tmp, axis = 1)
x_test = x_test.drop(columns = tmp, axis = 1)

# print(x_train.isna().sum())
# print(x_test.isna().sum())

# cond = (x_test.isna().sum() > 100)
# tmp = x_test.columns[cond]

# x_train = x_train.drop(columns = tmp , axis = 1)
# x_test = x_test.drop(columns = tmp, axis = 1)
# print(x_train.columns, x_test.columns)
# print()
# print()
for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    # print(b,len(a), i)

date = x_test["Date"]
# print(144)
x_train = x_train.drop('Date', axis = 1)
x_test = x_test.drop('Date', axis = 1)
y_train = y_train.drop("Date", axis=1)

x_train_num = x_train.select_dtypes(exclude = "object")
x_train_num = x_train_num.fillna(x_train_num.mean())

x_test_num = x_test.select_dtypes(exclude = "object")
x_test_num = x_test_num.fillna(x_test_num.mean())

x_train_cate = x_train.select_dtypes("object")

for i in x_train_cate.columns:
    x_train_cate[i] = x_train_cate[i].fillna(x_train_cate[i].value_counts().idxmax())

x_test_cate = x_test.select_dtypes("object")

for i in x_test_cate.columns:
    x_test_cate[i] = x_test_cate[i].fillna(x_test_cate[i].value_counts().idxmax())

# print(x_train.shape, x_test.shape)

# print(x_train.isna().sum() , x_test.isna().sum())

from sklearn.preprocessing import LabelEncoder as le
# print(1535)
lle = le()
for i in x_train_cate:
    x_train_cate[i] = lle.fit_transform(x_train_cate[i])
    x_test_cate[i] = lle.fit_transform(x_test_cate[i])

x_train = pd.concat([x_train_cate, x_train_num], axis = 1)
x_test = pd.concat([x_test_cate,x_test_num], axis = 1) # 이거도 순서 똑같이 맞춰줘야한다...
# print(x_train.shape, x_test.shape)
y_train = np.ravel(y_train)
y_train = lle.fit_transform(y_train)

print(x_train.dtypes)
print(x_train.head())
# print(y_train)
# y_train = np.ravel(y_train)
# print(1)
from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train, test_size = 0.2, random_state=1234 , stratify = y_train)

from sklearn.ensemble import RandomForestClassifier as rf

rff = rf()
rf_model = rff.fit(x,y)
rf_pred = rf_model.predict_proba(x_val)[:,1]
# print(2)
# print((x_train.columns), (x_test.columns))
from sklearn.metrics import auc, roc_curve

a,b,c = roc_curve(y_val, rf_pred)
rf_score = auc(a,b)
print(rf_score)

actual_pred = rf_model.predict_proba(x_test)[:,1]
obj = {"Date" : date, "RainTomorrow_Prob" : actual_pred}
result = pd.DataFrame(obj)

result.to_csv("result.csv", index = False)
# print(y_test)
y_test = y_test["RainTomorrow"]
a,b,c  = roc_curve(y_test, actual_pred, pos_label = "Yes")
actual_score = auc(a,b)
print(actual_score)
