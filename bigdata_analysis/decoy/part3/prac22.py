import pandas as pd
import numpy as np

x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_X_train.csv")
x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_y_train.csv")

for i in x_train.columns:
    a = x_train[i].unique()
    b = x_train[i].dtypes
    # print(i," ",len(a)," ",b)

idd = x_test['ID'].copy()

x_train = x_train.drop(columns = ['ID','Name'])
x_test = x_test.drop(columns = ['ID','Name'])
y_train = y_train.drop(columns = 'ID')

print(x_train.shape, y_train.shape)

from sklearn.model_selection import train_test_split as tts

X , X_val , Y , Y_val = tts(x_train,y_train,
                            random_state = 1234, 
                            test_size = 0.2, 
                            stratify = y_train)

print(X.shape, Y.shape)

from sklearn.ensemble import RandomForestClassifier as rf

rff = rf()
model_rf = rff.fit(X,Y)

score_rf = model_rf.predict_proba(X_val)[:,1]

from sklearn.metrics import roc_curve, auc

fpr,tpr,threshold = roc_curve(Y_val, score_rf, pos_label="Yes")
auc_rf = auc(fpr,tpr)
print(auc_rf)

y_score = model_rf.predict_proba(x_test)[:,1]

obj = {'ID' : idd, 
       'prob_Private' : y_score}
result = pd.DataFrame(obj)

result.to_csv("1234.csv", index = False)

y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_y_test.csv")
y_test = y_test.drop(columns = 'ID')

fpr, tpr, treshold = roc_curve(y_test ,y_score,pos_label = 'Yes' )
a = auc(fpr, tpr)
print(a)
