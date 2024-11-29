import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/mtcars2.csv")

# a = int(df.shape[0] * 0.8)
# train = df.iloc[:a]

# tmp = train['disp'].median()

# before = train['disp'].std()

# train['disp'] = train['disp'].fillna(tmp)
# after = train['disp'].std()

# answer = round(abs(after - before) , 3)
# print(answer)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/gehan.csv")

# upl = df['time'].mean() + df['time'].std() * 1.5
# lpl = df['time'].mean() - df['time'].std() * 1.5

# ti = df['time']
# cond = ((ti >= upl) | (ti <= lpl))
# print(ti[cond].sum())

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/stroke_X_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/stroke_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/stroke_y_train.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/02회/stroke_y_test.csv")

print(x_train)
id = x_test.copy()['id']

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtype
    c = x_train[i].isna().sum()
    print(b,len(a),i,c)

# id 버리기

x_train = x_train.drop(columns = 'id' , axis = 1)
x_test = x_test.drop(columns = 'id' , axis = 1)

y_train = y_train.drop(columns = 'id' , axis = 1)
y_test = y_test.drop(columns = 'id' , axis = 1)

print(x_train.head())

tmp = []

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtype
    c = x_train[i].isna().sum()
    d = x_train[i].value_counts()
    # print(i,d)
    if b == "object":
        tmp.append(i)

from sklearn.preprocessing import LabelEncoder as le

lle = le()

for i in tmp:
    a = lle.fit(x_train[i])
    x_train[i] = a.transform(x_train[i])
    x_test[i] = a.transform(x_test[i])


from sklearn.model_selection import train_test_split as tts

x , x_val , y , y_val = tts(x_train, y_train, random_state = 1234 , test_size = 0.2 , stratify = y_train)


from sklearn.ensemble import RandomForestClassifier as rff
from xgboost import XGBClassifier as xgg
from lightgbm import LGBMClassifier as lgg
from sklearn.metrics import accuracy_score as ass

rf , xg , lg = rff() , xgg() , lgg()
rf_model , xg_model, lg_model = rf.fit(x,y), xg.fit(x,y) , lg.fit(x,y)
rf_pred, xg_pred, lg_pred = rf_model.predict(x_val) ,xg_model.predict(x_val),lg_model.predict(x_val)
rf_score , xg_score , lg_score = ass(y_val , rf_pred) , ass(y_val , xg_pred) , ass(y_val , lg_pred)
print(rf_score , xg_score , lg_score)

pred = xg_model.predict(x_test)
obj = {'id' : id , "stroke" : pred}
result = pd.DataFrame(obj)

result.to_csv("result.csv" , index = False)

reault_score = ass(pred , y_test)
print(reault_score)

