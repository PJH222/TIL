import pandas as pd

train = pd.read_csv("train_insurance.csv")
test = pd.read_csv("test_insurance.csv")
y_test = pd.read_csv("insurance_y_test.csv")
y_test = y_test['test'].copy().astype("int64")

# print(train)
y_train = train['charges'].copy().astype("int64")
X_train = train.copy().drop('charges',axis = 1)
X_test = test.copy()

# print(X_train.isna().sum()) # 결측치 없음

for i in X_train.columns:
    if X_train[i].dtype == 'object':
        a = X_train[i].unique()
        idx = 0
        tmp = {}
        for j in a:
            tmp[j] = idx
            idx += 1
        X_train[i] = X_train[i].map(tmp)
        X_test[i] = X_test[i].map(tmp)

from sklearn.model_selection import train_test_split

X_tr , X_val , y_tr, y_val = train_test_split(
    X_train,y_train,random_state = 23
)

from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.metrics import mean_absolute_percentage_error as MAPE

rff = rf()
model = rff.fit(X_tr,y_tr)
pred = model.predict(X_val)
score = MAPE(y_val,pred)

obj = {'pred' : pred}
result = pd.DataFrame(obj)
result.to_csv("result.csv")

real_pred = model.predict(X_test)
real_score = MAPE(y_test, real_pred)

print(score , real_score)