import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/영화_순위리스트.csv")

# bp = df["BP_change"]
# tr = df["Treatment"]

# mdl = bp[tr == "MDL"]
# con = bp[~ (tr == "MDL")]

# # print(mdl, con)

# answer = round(mdl.mean() - con.mean() , 2)
# print(answer)

# from scipy.stats import ttest_rel

# a = ttest_rel(mdl, con)
# print(a)

# answer = round(a[0] , 2)
# print(answer)

# answer = round(a[1] , 3)
# print(answer)

# if answer < 0.05:
#     print("기각")
# else:
#     print("채택")

# am = df["am"]
# hp = df["hp"]

# am11 = hp[am == 1]
# am00 = hp[am == 0]

# result = am11.var() / am00.var()
# answer = round(result, 2)
# print(answer)

# from scipy.stats import f

# pval = 1 - f.cdf(result , len(am11) - 1 , len(am00) - 1)
# # print(pval)
# answer = round(pval, 3)

# print(answer)

# if answer < 0.05:
#     print("기각")
# else:
#     print("채택")

# from scipy.stats import chi2_contingency as ch

# seg , reg = df["Segment"] , df["Region"]

# tb = pd.crosstab(seg , reg)
# # print(tb)

# a = ch(tb)
# print(a)
# print()
# answer = round(a[3][1,2] , 2)
# print(answer)

# answer = int(a[0])
# print(answer)

# answer = round(a[1] , 3)
# print(answer)
# if answer < 0.05:
#     print("기각")
# else:
#     print("채택")

# from scipy.stats import shapiro as sh

# pri = df["Price"]
# pri = pri.copy().dropna()

# answer = round(pri.mean() , 2)
# print(answer)

# a = sh(pri)

# answer = round(a[0] , 2)
# print(answer)

# answer = round(a[1] , 4)
# if answer < 0.0001:
#     answer = 0
#     print("기각")
# else:
#     if answer < 0.1:
#         print("기각")
#     else:
#         print("채택")

# print(answer)

# print(df.columns) Horsepower Rev_per_mile

# rev = df["Rev_per_mile"]
# hp = df["Horsepower"]

# from scipy.stats import pearsonr as pr

# a = pr(rev,hp)

# answer = round(a[0] , 3)
# print(answer)

# result = (answer) / ((1 - answer**2)/(len(rev) - 2))**0.5
# answer = round(result, 2)
# print(result)

# if a[1] < 0.0001:
#     answer = 0
#     print("기각")
# else:
#     if a[1] < 0.05:
#         answer = round(a[1] , 4)
#         print("기각")
#     else:
#         print("채택")

# print(answer)

# from sklearn.decomposition import PCA as p

# mur, ass , urb , rap = df["Murder"] , df["Assault"], df["UrbanPop"], df["Rape"]

# a = p(n_components = 4)
# model = a.fit_transform(df)
# # print(df.columns)
# answer = round(a.components_[0,1] , 3)
# print(answer)

# answer = round(model[33 , 0] , 3)
# print(answer)

# answer = pd.Series(a.explained_variance_ratio_)
# print(round(answer[0] , 2))

# import statsmodels.api as sm

# print(df.columns) Rev_per_mile Weight Length EngineSize

# tmp = ["Rev_per_mile", "Weight" ,"Length" ,"EngineSize", "Price"]
# dff = df[tmp]

# dff = dff.dropna()

# y = dff["Price"]
# x = dff.copy().drop(columns = "Price" , axis = 1)
# x = sm.add_constant(x)

# tmp = sm.OLS(y,x)
# model = tmp.fit()
# print(model.summary())

# answer = 0.396
# print(answer)

# answer = 0.0023
# print(answer)

# answer = 0.158
# print(answer)

# answer = 0.005
# print(answer)

# df["x2"] = df["x2"].map({"M" : 1, "F" : 0})

# import statsmodels.api as sm

# y = df["y"]
# x = df.copy().drop(columns = "y", axis = 1)
# x = sm.add_constant(x)

# tmp = sm.GLM(y,x,family = sm.families.Binomial())
# aa = tmp.fit()

# print(aa.summary())

# answer = round( -0.8077,3)
# print(answer)

# answer = round( np.exp(-0.1575) , 3)
# print(answer)

# result = aa.predict()[8]

# if result < 0.7:
#     print(1)
# else:
#     print(0)

from scipy.stats import bartlett as b

# print(df.columns) 예산 장르

bud = df["예산"]
gen = df["장르"]

thr = bud[gen == "Thriller"]
com = bud[gen == "Comedy"]
dra = bud[gen == "Drama"]
act = bud[gen == "Action"]

varr = [thr.var(),com.var(),dra.var(),act.var()]
n_df = [len(thr) ,len(com),len(dra),len(act)]

sp2 = sum(np.subtract(n_df , 1) * varr) / (sum(n_df) - 4)
answer = round(np.log(sp2), 3)
print(answer)

a = b(thr,com,dra,act)
print(a)

answer = round(a[0], 2)
print(answer)

answer = round(a[1] , 4)
print(answer)
if answer < 0.1:
    print("기각")
else:
    print("채택")
