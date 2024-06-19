import pandas as pd

X_train = pd.read_csv("titanic3_X_train.csv")
X_test = pd.read_csv("titanic3_X_test.csv")
y_train = pd.read_csv("titanic3_y_train.csv")
y_test = pd.read_csv("titanic3_y_test.csv")

# print(X_train.isna().sum())
# print(X_train['age'])
col = ['age', 'cabin','ID','name','ticket']

ID = X_test['ID']
X_train, X_test = X_train.drop(columns = col), X_test.drop(columns = col)
# print(X_test.isna().sum())
# print(X_train.info())
#  0   pclass    785 non-null    int64
#  1   sex       785 non-null    object
#  2   sibsp     785 non-null    int64
#  3   parch     785 non-null    int64
#  4   fare      784 non-null    float64
#  5   embarked  784 non-null    object

# for i in X_train.columns:
#     a = X_train[i].unique()
#     print(i,":", len(a))
# print(X_train['embarked']) # embarked와 sex는 숫자로 대체 할 것

for i in ['embarked','fare']:
    if X_train[i].dtypes == "object":
        mostt = X_train[i].value_counts().idxmax()
        X_train[i] = X_train[i].fillna(mostt)
    else:
        avgg = X_train[i].mean()
        X_train[i] = X_train[i].fillna(avgg)

    if X_test[i].dtypes == "object":
        mostt = X_test[i].value_counts().idxmax()
        X_test[i] = X_test[i].fillna(mostt)
    else:
        avgg = X_test[i].mean()
        X_test[i] = X_test[i].fillna(avgg)

# print(X_train.info()) # sex, embarked 숫자로 변환하기


# print(X_train['sex'].value_counts())
tmp = {"male" : 1, "female" : 0, "F" : 0}
X_train['sex'] = X_train['sex'].map(tmp)
X_test['sex'] = X_test['sex'].map(tmp)


for i in ['embarked']:
    idx = 0
    tmp = {}
    aa = X_train[i].unique()
    for j in aa:
        tmp[j] = idx
        idx += 1
    else:
        X_train[i] = X_train[i].map(tmp)

for i in ['sex' , 'embarked']:
    idx = 0
    tmp = {}
    aa = X_test[i].unique()
    for j in aa:
        tmp[j] = idx
        idx += 1
    else:
        X_test[i] = X_test[i].map(tmp)

for i in ['survived']:
    idx = 0
    tmp = {}
    aa = y_train[i].unique()
    for j in aa:
        tmp[j] = idx
        idx += 1
    else:
        y_train[i] = y_train[i].map(tmp)

for i in ['survived']:
    idx = 0
    tmp = {}
    aa = y_test[i].unique()
    for j in aa:
        tmp[j] = idx
        idx += 1
    else:
        y_test[i] = y_test[i].map(tmp)



from sklearn.model_selection import train_test_split

# print(y_train)
y_train = y_train['survived']
y_test = y_test['survived']

x_tre, x_val, y_tre, y_val = train_test_split(
    X_train, y_train,
    random_state = 2022,
    stratify = y_train,
    test_size = 0.15
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import f1_score


rf = RandomForestClassifier(n_estimators = 500, random_state = 2022, max_depth = 5)

dt = DecisionTreeClassifier(random_state = 2020)

ada = AdaBoostClassifier(dt, random_state= 2020, learning_rate = 0.2, n_estimators=500)
bag = BaggingClassifier(dt, random_state=2020 , n_estimators=500)
xgb = XGBClassifier(random_state = 2020, n_estimators=500, max_depth = 5)
lgbm = LGBMClassifier(random_state = 2020, n_estimators=500, max_depth = 5,num_leaves=10)

pre_model = [rf,ada,bag,xgb,lgbm]
model_name = ['rf','ada','bag','xgb','lgbm']
model = []
score = []
idx = 0

for i in pre_model:
    modell = i.fit(x_tre,y_tre)
    model.append([modell,model_name[idx]])
    scoree = modell.predict(x_val)
    # score.append([scoree,model_name[idx]])
    f11 = round(f1_score(y_val,scoree) * 100 , 3)
    score.append([f11,model_name[idx]])

    idx += 1

print(sorted(score, key=lambda x : x[0],reverse=True))

modelll = model[4][0]

y_score = modelll.predict(X_test)
obj = {'ID' : ID, "survived" : y_score}
result = pd.DataFrame(obj)
result.to_csv("result.csv", index=False)

idx = 0
actual = []
for i in model:
    actual_score = i[0].predict(X_test)
    f11 = round(f1_score(y_test,actual_score)*100 ,3)
    actual.append([f11,model_name[idx]])
    idx += 1

print(sorted(actual,key = lambda x:x[0], reverse=True))
