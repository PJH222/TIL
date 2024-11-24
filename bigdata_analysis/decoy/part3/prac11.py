import pandas as pd
import numpy as np


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit_Five.csv")

# print(df)

cond = (df["Treatment"] == "Control")

mdl = df[~ cond]["BP_change"]
control = df[cond]["BP_change"]

result = mdl.mean() - control.mean()
answer = round(result, 2)
# print(answer)


from scipy.stats import ttest_rel

a = ttest_rel(mdl, control)

stat = a.statistic
answer2 = round(stat , 2)
# print(answer2)

pval = round(a.pvalue,3)
# print(pval)

# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/mtcars2.csv")

# print(df)

cond1 = (df["am"] == 1)

am11 = df[cond1]
am00 = df[~ cond1]

s1 = am11["hp"].var()
s2 = am00["hp"].var()

answer = round(s1 / s2 , 2)
# print(answer)


from scipy.stats import f

stat = round(s1/s2, 2)
# print(round(stat , 2))

df1, df2 = len(am11) - 1 , len(am00)

pval = 1 - f.cdf(stat , dfn = df1 , dfd = df2)
pval = round(pval , 3)
# print(pval)
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/고객_등급리스트.csv")

from scipy.stats import chi2_contingency as ch

tb = pd.crosstab(df["Segment"] , df["Region"])

chi2, pval, df, expected = ch(tb)

# print(chi2, pval, df, expected)

answer = round(expected[1,2] , 2)
# print(answer)

# print(int(chi2))

pval = round(pval , 3)
# print(pval)

# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit_Five.csv")

cond = (df["Treatment"] == "Control")

control = df[cond]["BP_change"]
mdl = df[~cond]["BP_change"]

answer = round(mdl.mean() - control.mean() , 2)
# print(answer)

# print(answer)

stat = round(-3.6691820392905843, 2)
# print(stat)

from scipy.stats import ttest_rel

a = ttest_rel(mdl, control)

# print(a)

pval = round(0.0009743112823987295 , 3)
# print(pval)

# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")




df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/mtcars2.csv")

# print(df)
cond = (df["am"] == 0)

am0 = df[cond]["hp"]
am1 = df[~cond]["hp"]

s1 = am1.var()
s2 = am0.var()

answer = round(s1 / s2 , 2)
# print(answer)
# print()

# print(answer)
# print()

from scipy.stats import f

df1 , df2 = len(am0) - 1 , len(am1) - 1

pval = 1 - f.cdf(answer, dfn = df2, dfd = df1)

pval = round(pval, 3)
# print(pval)

# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")



df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/고객_등급리스트.csv")

tb = pd.crosstab(df["Segment"],df["Region"])

from scipy.stats import chi2_contingency as ch

a = ch(tb)
# print(a)

answer = round(a[3][1,2], 2)
# print(answer)

answer = int(9.488312197551783)
# print(answer)

answer = round(0.1479205256846858, 3)
# print(answer)

# if answer < 0.05:
#     print("기각")
# else:
#     print("채택")

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

answer = round(df["Price"].mean(), 2)
# print(answer)

from scipy.stats import shapiro as sh

a,b = sh(df["Price"].dropna())
# print(a , b)

answer = round(a , 2)
# print(answer)
# answer()

b = round(b , 4)
# if b < 0.0001:
#     answer = 0
#     print(answer)    
# else:
#     answer = b
#     print(b)

# if answer < 0.1:
#     print("기각")
# else: 
#     print("채택")


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

from scipy.stats import pearsonr as p

rev = df["Rev_per_mile"]
hp = df["Horsepower"]

a = p(hp, rev)
# print(a)
answer = round(a[0], 3)
# print(answer)

b = answer / ((1-answer**2)/(len(hp) - 2))**0.5
answer = round(b , 2)
# print(answer)

answer = round(a[1] , 4)

# if answer < 0.0001:
#     answer = 0
#     print(answer)
#     print("기각")
# else:
#     if answer < 0.05:
#         print(answer)
#         print("기각")
#     else:
#         print(answer)
#         print("채택")

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/USArrests.csv")

from sklearn.decomposition import PCA

pca = PCA(n_components = 4)
pca.fit_transform(df)

# print(df.columns)

a = pca.components_
b = a.T

answer = round(a[0,1],3)
# print(answer)

score = pca.fit_transform(df)[33]
answer = round(score[0], 3)
# print(answer)

ratio = pd.Series(pca.explained_variance_ratio_)
answer = round(ratio[0] , 2)

# print(answer)


df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")


import statsmodels.api as sm

tmp = ["Price" ,'Rev_per_mile','Weight','Length','EngineSize']
dff = df[tmp].copy().dropna()

y = dff["Price"]
x = dff.copy().drop(columns = "Price" , axis = 1)
x = sm.add_constant(x)

model = sm.OLS(y,x)
result = model.fit()

print(result.summary())

answer = 0.396
print(answer)

answer = 0.0023
print(answer)

answer = 0.158
print(answer)

answer = 0.005
print(answer)