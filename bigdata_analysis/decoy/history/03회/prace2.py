import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/economics.csv")
# a = int(df.shape[0] * 0.7) 
# print(a)
# train = df.iloc[:a]
# a = int(train['pce'].quantile(0.25))
# print(a)

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/Hitters.csv")
# ye = df['Years']
# cond1 = (ye == 10)
# df = df[cond1]
# hm = df['HmRun']
# menn = hm.mean()
# cond2 = (hm > menn)

# answer = df[cond2].shape[0]
# print(answer)

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/msleep.csv")

# print(df.isna().sum().idxmax())

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/job_change_X_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/job_change_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/job_change_y_train.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/history/03회/job_change_y_test.csv")

id = x_test["enrollee_id"]

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtype
    c = x_train[i].isna().sum()
    # print(b , len(a) , i , c)

cond = (x_train.isna().sum() > 1000)
tmp = (x_train.columns[cond])

x_train = x_train.drop(columns = tmp , axis = 1)
x_test = x_test.drop(columns = tmp, axis = 1)

y_train = y_train.drop(columns = 'enrollee_id' , axis = 1)
y_test = y_test.drop(columns = 'enrollee_id' , axis = 1)

cond = (x_train.isna().sum() > 0)
tmp = (x_train.columns[cond])
    
for i in tmp:
    mode = x_train[i].value_counts().idxmax()
    x_train[i] = x_train[i].fillna(mode)
    x_test[i] = x_test[i].fillna(mode)

x_train = x_train.drop(columns = 'enrollee_id' , axis = 1)
x_test = x_test.drop(columns = 'enrollee_id' , axis = 1)

# print(x_train.isna().sum())
# print(x_test.isna().sum())
tmp = []

for i in x_train.columns:
    # a = x_train[i].unique()
    b = x_train[i].dtype
    # c = x_train[i].isna().sum()
    # print(b , len(a) , i , c)
    if b == "object":
        tmp.append(i)


from sklearn.preprocessing import LabelEncoder as le

lle = le()

# print(x_train.shape)
for i in tmp:
    tmp2 = pd.concat([x_train[i] , x_test[i]] , axis = 0)
    # print(tmp2)
    a = lle.fit(tmp2)
    x_train[i] = a.transform(x_train[i])
    x_test[i] = a.transform(x_test[i])

# print(x_train.info())

# print(x_train.info() , x_test.info())


from sklearn.model_selection import train_test_split as tts

x , x_val, y , y_val = tts(x_train, y_train, random_state = 1234 , test_size = 0.2 , stratify = y_train)

from sklearn.ensemble import RandomForestClassifier as rff
from xgboost import XGBClassifier as xgg
from lightgbm import LGBMClassifier as lgg
from sklearn.metrics import auc, roc_curve

rf , xg , lg = rff() , xgg() , lgg()
rf_model , xg_model , lg_model = rf.fit(x,y) , xg.fit(x,y) , lg.fit(x,y)
rf_pred , xg_pred , lg_pred = rf_model.predict_proba(x_val)[:,1], xg_model.predict_proba(x_val)[:,1],lg_model.predict_proba(x_val)[:,1]

a,b,c = roc_curve(y_val , rf_pred)
rf_auc = auc(a,b)
print(rf_auc)

a,b,c = roc_curve(y_val , xg_pred)
rf_auc = auc(a,b)
print(rf_auc)

a,b,c = roc_curve(y_val , lg_pred)
rf_auc = auc(a,b)
print(rf_auc)

real = lg_model.predict_proba(x_test)[:,1]
real_predict = np.where(real > 0.5 , 1 , 0)
obj = {'enrollee_id' : id , "target" : real_predict , "target_prob" : real}
result = pd.DataFrame(obj)

result.to_csv("result.csv" , index = False)

a,b,c = roc_curve(y_test , real)
tmp = auc(a,b)
print(tmp)

