import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_X_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_y_train.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_y_test.csv")

# 결측치 없음
# print(x_train.isna().sum())
# print(y_train.isna().sum())
# print(x_test.isna().sum())

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    # print(len(a) , b , i)

# ID, Name 제거
idd = x_test['ID'].copy()
tmp = ['ID','Name']

x_train = x_train.drop(columns = tmp)
x_test = x_test.drop(columns = tmp)
y_train = y_train.drop(columns= 'ID')

from sklearn.model_selection import train_test_split as tts

x , x_val , y, y_val = tts(x_train,y_train,random_state = 1234, test_size = 0.2, stratify = y_train)

# print(x.shape, y.shape)

from sklearn.ensemble import RandomForestClassifier as rf

rff = rf()
rf_model = rff.fit(x,y)
rf_score = rf_model.predict_proba(x_val)[:,1]


from sklearn.metrics import auc, roc_curve

a , b, c = roc_curve(y_val , rf_score, pos_label='Yes')
rf_score = auc(a,b)
print(rf_score)


actual = rf_model.predict_proba(x_test)[:,1]

obj = {"ID" : idd, "prob_Private" : actual}
result = pd.DataFrame(obj)

result.to_csv("result.csv",index = False)

a,b,c = roc_curve(y_test['Private'], actual, pos_label = "Yes")
answer = auc(a,b)

print(answer)





