import pandas as pd

X_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_X_train.csv")
X_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_X_test.csv")
y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_y_train.csv")

# print(X_train.isna().sum(), X_test.isna().sum()) # 결측치는 존재하지 않는다.

# print(X_train.columns)

for i in X_train.columns:
    a = X_train[i].unique()
    # print(i," : ",len(a))
    # 현재 ID와 Name은 결과에 영향을 주는 요소가 아니므로 drop 한다.

X_test_ID = X_test['ID'].copy()

X_train = X_train.drop(columns = ['ID','Name'])
X_test = X_test.drop(columns = ['ID','Name'])
y_train = y_train['Private']

from sklearn.model_selection import train_test_split

x_tr , x_val , y_tr, y_val = train_test_split(
    X_train, y_train,
    random_state = 2022,
    stratify = y_train,
    test_size = 0.2
)

from sklearn.metrics import auc, roc_curve
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

rf = RandomForestClassifier(
    n_estimators = 500,
    random_state = 2022
)

model_rf = rf.fit(x_tr,y_tr)
score_rf = model_rf.predict_proba(x_val)[:,1]
a,b,c = roc_curve(y_val, score_rf,pos_label='Yes')
auc_rf = auc(a,b)
print(auc_rf, "rf")



dt = DecisionTreeClassifier(max_depth = 3)

ada = AdaBoostClassifier(dt, n_estimators = 500, random_state = 2022, learning_rate = 0.5)
model_ada = ada.fit(x_tr,y_tr)
score_ada = model_ada.predict_proba(x_val)[:,1]

a,b,c = roc_curve(y_val, score_ada, pos_label='Yes')
auc_ada = auc(a,b)
print(auc_ada, "ada")

bag = BaggingClassifier(dt, n_estimators = 500, random_state=2022)
model_bag = bag.fit(x_tr,y_tr)

score_bag = model_bag.predict_proba(x_val)[:,1]
a,b,c = roc_curve(y_val, score_bag, pos_label='Yes')
auc_bag = auc(a,b)
print(auc_bag, "bag")

final_score = model_ada.predict_proba(X_test)[:,1]

obj = {"ID" : X_test_ID, "prob_Private" : final_score}
result = pd.DataFrame(obj)

result.to_csv("result.csv", index = False)

answer = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/College_y_test.csv")
actual = answer['Private']


a,b,c = roc_curve(actual, final_score, pos_label='Yes')
final_scorre = auc(a,b)
print("ada, 최종 점수",final_scorre)

a,b,c = roc_curve(actual, model_rf.predict_proba(X_test)[:,1], pos_label='Yes')
final_scorre = auc(a,b)
print("rf, 최종 점수",final_scorre)

a,b,c = roc_curve(actual, model_bag.predict_proba(X_test)[:,1], pos_label='Yes')
final_scorre = auc(a,b)
print("bag, 최종 점수",final_scorre)



