import pandas as pd

X_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/weatherAUS_X_train.csv")
X_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/weatherAUS_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/weatherAUS_y_train.csv")
y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/weatherAUS_y_test.csv")



tmp = (X_train.isna().sum() > 600)
col = X_train.columns[tmp]
X_train,X_test = X_train.drop(columns=col) , X_test.drop(columns=col)

# print(X_train.info())

# 결측치 채우기

for i in X_train.columns:
    idx = 0
    tmp = {}
    if X_train[i].dtype == 'object':
        mostt = max(X_train[i].value_counts().idxmax())
        X_train[i] = X_train[i].fillna(mostt)

    else:
        avgg = X_train[i].mean()
        X_train[i] = X_train[i].fillna(avgg)

for i in X_test.columns:
    idx = 0
    tmp = {}
    if X_test[i].dtype == 'object':
        mostt = max(X_test[i].value_counts().idxmax())
        X_test[i] = X_test[i].fillna(mostt)

    else:
        avgg = X_test[i].mean()
        X_test[i] = X_test[i].fillna(avgg)

# object 형태 카테고리

Datee = X_test['Date'].copy()

for i in X_train.columns:
    idx = 0
    tmp = {}
    if X_train[i].dtype == 'object':
        uniq = X_train[i].unique()
        for j in uniq:
            tmp[j] = idx
            idx += 1
        X_train[i] = X_train[i].map(tmp)

for i in X_test.columns:
    idx = 0
    tmp = {}
    if X_test[i].dtype == 'object':
        uniq = X_test[i].unique()
        for j in uniq:
            tmp[j] = idx
            idx += 1
        X_test[i] = X_test[i].map(tmp)

for i in y_train.columns:
    idx = 0
    tmp = {}
    if y_train[i].dtype == 'object':
        uniq = y_train[i].unique()
        for j in uniq:
            tmp[j] = idx
            idx += 1
        y_train[i] = y_train[i].map(tmp)

for i in y_test.columns:
    idx = 0
    tmp = {}
    if y_test[i].dtype == 'object':
        uniq = y_test[i].unique()
        for j in uniq:
            tmp[j] = idx
            idx += 1
        y_test[i] = y_test[i].map(tmp)


y_train = y_train['RainTomorrow']

# print(X_test)

from sklearn.model_selection import train_test_split

x_tre, x_val, y_tre, y_val = train_test_split(
    X_train, y_train,
    random_state = 2022,
    stratify = y_train,
    test_size = 0.2
)


from sklearn.metrics import auc, roc_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

score = []
model = []

rf = RandomForestClassifier(n_estimators = 500,
                            random_state = 2022,
                            max_depth = 5)
model_rf = rf.fit(x_tre,y_tre)
model.append(model_rf)

score_rf = model_rf.predict_proba(x_val)[:,1]
score.append(score_rf)
a,b,c = roc_curve(y_val,score_rf)
auc_rf = round(auc(a,b)*100 , 3)
answer = []
answer.append([auc_rf, "랜덤포레스트"])

dt = DecisionTreeClassifier(random_state=2022, max_depth = 5)

ada = AdaBoostClassifier(dt, n_estimators = 500, learning_rate = 0.5)
model_ada = ada.fit(x_tre, y_tre)
model.append(model_ada)
score_ada = model_ada.predict_proba(x_val)[:,1]
score.append(score_ada)
a,b,c = roc_curve(y_val,score_ada)
auc_ada = round(auc(a,b)*100 , 3)
answer.append([auc_ada,"ADA"])

bag = BaggingClassifier(dt, n_estimators = 500)
model_bag = bag.fit(x_tre,y_tre)
model.append(model_bag)
score_bag = model_bag.predict_proba(x_val)[:,1]
score.append(score_bag)
a,b,c = roc_curve(y_val,score_bag)
auc_bag = round(auc(a,b) * 100, 3)
answer.append([auc_bag,"bagging"])

xgb = XGBClassifier(n_estimators=500)
model_xgb = xgb.fit(x_tre,y_tre)
model.append(model_xgb)
score_xgb = model_xgb.predict_proba(x_val)[:,1]
score.append(score_xgb)
a,b,c = roc_curve(y_val,score_xgb)
auc_xgb = round(auc(a,b) * 100 , 3)
answer.append([auc_xgb,"XGB"])

lgbm = LGBMClassifier(n_estimators=500)
model_lgbm = lgbm.fit(x_tre,y_tre)
model.append(model_lgbm)
score_lgbm = model_lgbm.predict_proba(x_val)[:,1]
score.append(score_lgbm)
a,b,c = roc_curve(y_val,score_lgbm)
auc_lgbm = round(auc(a,b) * 100, 3)
answer.append([auc_lgbm,"LGBM"])

y_test_score = []

idxx = 0

scoree = []

y_test = y_test['RainTomorrow']

for i in range(len(model)):
    y_score = model[i].predict_proba(X_test)[:,1]
    a, b, c = roc_curve(y_test, y_score)
    auc_score = round(auc(a, b) * 100, 3)
    y_test_score.append([auc_score, answer[i][1]])


# for i in score:
#     a, b, c = roc_curve(y_test, scoree[idxx])
#     auc_score = round(auc(a, b) * 100, 3)
#     y_test_score.append([auc_score,answer[idxx][1]])
#     idxx += 1

print("train 결과 :",answer)
print("test 결과  :",y_test_score)




