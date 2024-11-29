import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/02회/USArrests.csv")

# print(df.info())

# ur = df["UrbanPop"]
# mu = df["Murder"]
# ass = df["Assault"]

# df["summ"] = df["Assault"] / (df["Murder"] + df["Assault"])

# cond1 = (df["summ"] >= 0.05)
# cond2 = (ur >= 60)

# semi_answer = df[cond1]
# answer = semi_answer[cond2]

# print(answer.shape)

# answer = answer.shape[0]
# print(answer)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/02회/CO2.csv")
# print(df)

# df["Type"] = df["Type"].str.replace("/","")

# ty = df["Type"]
# co = df["conc"]

# cond1 = (ty == "Mississippi")
# cond2 = (co // 100 == 5)

# cond3 = co.astype('string').str.endswith('5')

# print(df[cond1 & (cond2 | cond3)].shape[0])


# x_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/02회/BlackFriday_X_train.csv")
# x_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/02회/BlackFriday_X_test.csv")
# y_train = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/02회/BlackFriday_y_train.csv")
# y_test = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/02회/BlackFriday_y_test.csv")

# y_train = y_train["Purchase"]
# y_test = y_test["Purchase"]

# # print(x_train.info())

# tmp2 = []
# for i in x_train.columns:
#     a = x_train[i].unique()
#     b = x_train[i].dtype
#     c = x_train[i].isna().sum()
#     if b == 'object':
#         tmp2.append(i)

#     # print(b,len(a), i , c)

# # Product_Category_2, Product_Category_3,User_ID,  Product_ID 은 제거

# tmp = ['Product_Category_2', 'Product_Category_3','User_ID',  'Product_ID']

# x_train = x_train.drop(columns = tmp , axis = 1)
# x_test = x_test.drop(columns = tmp , axis = 1)


# tmp2 = []
# for i in x_train.columns:
#     a = x_train[i].unique()
#     b = x_train[i].dtype
#     c = x_train[i].isna().sum()
#     if b == 'object':
#         tmp2.append(i)


# from sklearn.preprocessing import LabelEncoder as le

# lle = le()

# for i in tmp2:
#     a = lle.fit(x_train[i])
#     x_train[i] = a.transform(x_train[i])
#     x_test[i] = a.transform(x_test[i])


# from sklearn.model_selection import train_test_split as tts

# x , x_val, y , y_val = tts(x_train, y_train, test_size = 0.2, random_state = 1234)


# from sklearn.ensemble import RandomForestRegressor as rff
# from xgboost import XGBRegressor as xgg

# rf, xg = rff() , xgg()
# rf_model , xg_model = rf.fit(x,y), xg.fit(x,y)
# rf_pred , xg_pred = rf_model.predict(x_val), xg_model.predict(x_val)

# from sklearn.metrics import mean_absolute_error as mae

# rf_score, xg_score = mae(y_val, rf_pred), mae(y_val, xg_pred)

# print(rf_score, xg_score)

# pred = rf_model.predict(x_test)
# obj = {"Purchase" : pred}
# result = pd.DataFrame(obj)

# result.to_csv("result.csv", index = False)

# score = mae(y_test , pred)
# print(score)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/02회/survey.csv")
# df = df[['성별','1번문항']]

# # print(df)

# ge = df['성별']
# pr = df['1번문항']

# tb = pd.crosstab(ge, pr)
# # print(tb)

# from scipy.stats import chi2_contingency as ch

# a = ch(tb)
# print(a[3])
# answer = 87
# print(answer)

# answer = int(a[0])
# print(answer)

# answer = round(a[1] , 4)
# if answer < 0.05:
#     print("기각")
# else:
#     print("채택")
# print(answer)

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/mock_test/02회/Cars93.csv")

ori = df["Origin"]
pri = df["Max_Price"]

# print(ori.value_counts(), pri)

tmp1 = pri[ori == "USA"]
tmp2 = pri[~ (ori == "USA")]

answer1 = round(tmp2.mean() - tmp1.mean() , 2)
print(answer1)


from scipy.stats import ttest_ind as tt

a = tt(tmp2 , tmp1, equal_var = False)

answer2 = round(answer1 / a[0] , 2)
print(answer2)

answer3 = round(a[0] , 4)
print(answer3)
pval = round(a[1] , 4)
if pval < 0.05:
    print("기각")
else:
    print("채택")
print(pval)

