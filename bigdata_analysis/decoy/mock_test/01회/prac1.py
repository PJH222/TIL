import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/iris.csv")

# print(df)

wid = df["Sepal.Width"]
stdd = wid.std()
cond = ((wid >= wid.mean() + stdd * 3) | (wid <= wid.mean() - stdd * 3))

answer = wid[cond]
# print(answer)
# print(answer.sum())
# print(np.where(wid < wid.mean() - stdd * 3 , 1 , 0))


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/mtcars1.csv")

# print(df)

dis = pd.DataFrame()
dis["disp"] = df["disp"]
# print(dis)

dis['rank'] = dis.rank(method = "min", ascending = False)
# print(dis)

rank = dis['rank']
a = dis[rank < 20]
answer = round(a['disp'].std() , 2)
# print(answer)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/Cars93.csv")

# # print(df.shape)
# answer1 = df.shape[0]
# print(answer1)

# answer2 = sum(df.isna().sum() > 0)
# print(answer2)

# answer3 = sum(df.isna().sum())
# print(answer3)

# col = df.columns[df.isna().sum() >= 10]
# tmp = df[col].copy().dropna()
# answer4 = len(tmp)
# print(answer4)

# answer5 = sum(df.index[df.isna().sum(axis = 1) >= 2])
# print(answer5)
# print()
# answer = answer1 + answer2 + answer3 + answer4 + answer5
# print(answer)


# x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/titanic3_X_train.csv")
# x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/titanic3_X_test.csv")
# y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/titanic3_y_train.csv")
# y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/titanic3_y_test.csv")

# id = x_test['ID'].copy()

# # print(x_train.isna().sum(), x_train.shape)
# # print(x_test.isna().sum(), x_test.shape)
# # tmp = []

# # for i in x_train.columns:
# #     a = len(x_train[i].unique())
# #     b = x_train[i].dtype
# #     c = x_train[i].isna().sum()
# #     if b == "object":
# #         tmp.append(i)

# # id, cabin은 제거하고, age는 제거

# x_train = x_train.drop(columns = ["ID",'age','cabin','name','ticket'])
# x_test = x_test.drop(columns = ["ID",'age','cabin','name','ticket'])

# a = x_train['fare'].value_counts().idxmax()
# b = x_train['embarked'].value_counts().idxmax()

# x_train['fare'] = x_train['fare'].fillna(a)
# x_train['embarked'] = x_train['embarked'].fillna(b)
# x_test['embarked'] = x_test['embarked'].fillna(b)

# y_train = y_train["survived"]

# tmp = []

# for i in x_train.columns:
#     a = len(x_train[i].unique())
#     b = x_train[i].dtype
#     c = x_train[i].isna().sum()
#     # print(b,c,a,i)
#     if b == "object":
#         tmp.append(i)

# from sklearn.preprocessing import LabelEncoder as le

# lle = le()

# for i in tmp:
#     a = lle.fit(x_train[i])
#     x_train[i] = a.transform(x_train[i])
#     x_test[i] = a.transform(x_test[i])

# # print(x_test.info())
# # print(tmp)


# from sklearn.model_selection import train_test_split as tts

# x , x_val, y , y_val = tts(x_train, y_train, test_size = 0.2, random_state = 1234 , stratify = y_train)

# # print(x.shape,x_val.shape, y.shape, y_val.shape)

# from sklearn.ensemble import RandomForestClassifier as rff
# from xgboost import XGBClassifier as xgg

# rf , xg = rff() , xgg()
# rf_model , xg_model = rf.fit(x,y) , xg.fit(x,y)
# rf_pred , xg_pred = rf_model.predict(x_val) , xg_model.predict(x_val)

# from sklearn.metrics import f1_score as f1

# rf_score , xg_score = f1(y_val , rf_pred) , f1(y_val, xg_pred)
# # print(rf_score, xg_score)

# pred = xg_model.predict(x_test)

# obj = {'ID' : id , "survived" : pred}
# result = pd.DataFrame(obj)

# result.to_csv("result.csv", index = False)

# actual_y = y_test['survived']

# score = f1(actual_y , pred)
# # print(score)

# pred = rf_model.predict(x_test)

# score = f1(actual_y , pred)
# # print(score)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/Cars93.csv")
df = df[['Type','Price']]
df = df.dropna()

ty = df["Type"]
pr = df["Price"]

a2 = pr[ty == "Small"]
a1 = pr[ty == "Large"]

answer = round(a1.mean() - a2.mean(), 2)
# print(answer)

from scipy.stats import ttest_rel, ttest_ind, t 

a = ttest_ind(a1,a2)

# print(a)

# 검정통계량 = 점추정량 / 표준오차

# x = a[0]
# y = answer
# x = answer / er
# er = answer / a[0]
# answer = round(er , 2)
# print(answer)

# a = t.interval(0.95,len(a1) + len(a2) - 2, loc = a[0], scale = er)
# print(a)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/01회/dices.csv")

answer = 1/6 * 500
print(int(answer))

sc = df['scale']
# print(sc.value_counts())
tmp = [167, 197, 91, 29, 7 , 9]
tmp1 = [1/6,1/6,1/6,1/6,1/6,1/6 ]

for i in range(6):
    tmp1[i] = tmp1[i] * 500

from scipy.stats import chisquare, chi2_contingency

a = chisquare(tmp, tmp1)
# print(a)

# a = chi2_contingency(tmp, tmp1)
# print(a)

answer = int(a[0])
print(answer)

pval = a[1]
if pval < 0.0001:
    answer = 0
    print("기각")
else:
    answer = pval
    if answer < 0.05:
        print("기각")
    else:
        print("채택")
print(answer)