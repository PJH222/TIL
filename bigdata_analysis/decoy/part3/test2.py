# 1번
#
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit_Five.csv")
#
# # print(da)
# #     BP_change    Dose Treatment lbl_Animal
# # 0        0.50    6.25   Control         R1
# # 1        4.50   12.50   Control         R1
#
# bp = da['BP_change'].copy()
# tr = da['Treatment'].copy()
#
# mdl = bp[tr=="MDL"].reset_index(drop=True)
# con = bp[tr=="Control"].reset_index(drop=True)
#
# tmp1 = (mdl - con).mean()
# answer_a = round(tmp1, 2)
# print(answer_a)
#
# from scipy.stats import ttest_rel
#
# stat, pval = ttest_rel(mdl, con)
# print(round(stat, 2))
#
# pval = round(pval, 3)
# print(pval)
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")

# 2번

# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/mtcars2.csv")
#
# hp = da['hp'].copy()
# am = da['am'].copy()
#
# a1 = hp[am == 1]
# a0 = hp[am == 0]
#
# ratioo = a1.var() / a0.var()
# print(round(ratioo , 2))
#
# print(round(ratioo, 2))
#
# from scipy.stats import f
#
# pval = 1 - f.cdf(ratioo , len(a1) - 1, len(a0) - 1)
# pval = round(pval, 3)
# print(pval)
#
#
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")












# 3번

# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/고객_등급리스트.csv")
#
# seg, reg = da['Segment'] , da['Region']
#
# ct = pd.crosstab(seg, reg)
# # print(ct)
#
# from scipy.stats import chi2_contingency
#
# stat, pval, dof, aa = chi2_contingency(ct)
# print(round(aa[1,2] , 2))
#
# print(int(stat))
#
# pval = round(pval, 3)
# print(pval)
#
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")


# 4 번
# import pandas as pd
# from scipy.stats import shapiro
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# pri = da['Price'].copy().dropna()
#
# aa = round(pri.mean() , 2)
# print(aa)
#
# stat, pval = shapiro(pri)
#
# # print(stat)
# print(round(stat,2))
#
# pval = round(pval, 4)
#
# if pval < 0.0001:
#     pval = 0
#
# print(pval)
#
# if pval < 0.1:
#     print("기각")
# else:
#     print("채택")



# 5 번

# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# from scipy.stats import pearsonr
#
# rpm = da['Rev_per_mile'].copy()
# hor = da['Horsepower'].copy()
#
# stat, pval = pearsonr(rpm,hor)
# rho = round(stat, 3)
#
# print(rho)
#
# import numpy as np
#
# tt = rho / np.sqrt( (1 - rho ** 2)/(len(rpm) - 2)  )
# tt = round(tt , 2)
# print(tt)
#
# pval = round(pval , 4)
# if pval < 0.0001:
#     pval = 0
#
# print(pval)
#
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")


# 6번
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/USArrests.csv")
#
# # print(da.columns) ['Murder', 'Assault', 'UrbanPop', 'Rape']
# from sklearn.decomposition import PCA
# # print(da.columns)
# ass = da['Assault'].copy()
#
# pca = PCA(n_components = 4)
# pca.fit_transform(da)
#
# model = pca.components_
# print(round(model[0,1] , 3))
#
# aa = pca.fit_transform(da)[33]
# print(round(aa[0],3))
#
# var_ratio = pca.explained_variance_ratio_
# print(round(var_ratio[0],2))


# 7번
# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# coll = ['Rev_per_mile','Weight','Length','EngineSize','Price']
#
# da = da[coll].copy().dropna() # 필요한 애들만 결측치 제거
#
# y = da['Price'].copy() # 타겟
# x = da[['Rev_per_mile','Weight','Length','EngineSize']].copy() # 변수
#
# import statsmodels.api as sm
# x = sm.add_constant(x) # 이걸 해줘야 선형회귀 할 수 있음... (상수항 결합을 위해 필요함)
# aa = sm.OLS(y,x) # OLS 객체생성
#
# result = aa.fit() # 학습
# print(result.summary()) # 요약문 출력
#
# print(0.424)





# 7번
# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# coll = ['Rev_per_mile','Weight','Length','EngineSize','Price']
# df = da[coll].copy().dropna()
#
# y = df['Price']
# x = df[['Rev_per_mile','Weight','Length','EngineSize']]
#
# import statsmodels.api as sm
# x = sm.add_constant(x)
# aa = sm.OLS(y,x) #객체
#
# model = aa.fit() # 학습
# # print(model.summary())
# # print(0.396)
# #
# # print(0.0023)
# #
# # print(0.158)
# bb = model.conf_int(alpha=0.05)
# print(bb)
# # print(0.005)
# print(0.005406)



# 7번
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# coll = ['Rev_per_mile','Weight','Length','EngineSize','Price']
# df = da[coll].copy().dropna()
#
# y = df['Price']
# x = df[['Rev_per_mile','Weight','Length','EngineSize']]
#
# import statsmodels.api as sm
# x = sm.add_constant(x)
# model = sm.OLS(y,x)
#
# result = model.fit()
# # print(result.summary())
# #
# # print(0.396)
# #
# # print(0.0023)
#
# bb = result.conf_int(alpha=0.05)
# print(bb)
#
# print()




# 7 번

# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# coll = ['Rev_per_mile','Weight','Length','EngineSize','Price']
#
# df = da[coll].copy().dropna()
#
# y = df['Price']
# x = df[['Rev_per_mile','Weight','Length','EngineSize']]
#
# import statsmodels.api as sm
#
# x = sm.add_constant(x)
#
# aa = sm.OLS(y,x)
# model = aa.fit()
#
# print(model.summary())
#
# print(0.396)
# print(0.0023)
# print(0.158)




# 8번
# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/job.csv")
#
# da['x2'] = da['x2'].map({"M" : 1 , "F" : 0})
#
# import statsmodels.api as sm
#
# y = da['y']
# x = da[['x1','x2','x3']]
# x = sm.add_constant(x)
#
# aa = sm.GLM(y,x, family=sm.families.Binomial())
# model = aa.fit()
# # print(model.summary())
# # print(-0.808)
#
# import numpy as np
#
# # print(round(np.exp(-0.1573), 3))
#
# prob = model.predict(x)[8]
# print(round(prob , 4))
# bb = round(prob , 4)
# if bb > 0.7:
#     print(1)
# else:
#     print(0)





# 8 번
# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/job.csv")
#
# da['x2'] = da['x2'].map({"M" : 1,'F' : 0})
#
# # 로지스틱 회귀
# y = da['y']
# x = da[['x1','x2','x3']]
#
# import statsmodels.api as sm
#
# x = sm.add_constant(x)
#
# aa = sm.GLM(y,x,family = sm.families.Binomial())
# result = aa.fit()
#
# print(result.summary())
#
# print(round(-0.8077 , 3))
#
# import numpy as np
#
# print(round(np.exp(-0.1575),3))
#
# prob = result.predict()[8]
# answer = round(prob,4)
# # print(round(prob,4))
# print(answer)
# if answer > 0.7:
#     print(1)
# else:
#     print(0)




# 8번
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/job.csv")
# da['x2'] = da['x2'].map({'M':1,'F':0})
#
# y = da['y'].copy()
# x = da[['x1','x2','x3']].copy()
#
# import statsmodels.api as sm
#
# x = sm.add_constant(x)
# aa = sm.GLM(y,x,family=sm.families.Binomial())
# result = aa.fit()
#
# print(result.summary())
#
# print(-0.8077)
#
# import numpy as np
# print(np.exp(-0.1575))
#
# prob = result.predict()[8]
# prob = round(prob, 4)
#
# if prob > 0.7:
#     print(1)
# else:
#     print(0)


# 9 번
#
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/영화_순위리스트.csv")
#
# from scipy.stats import bartlett
#
# print(da.columns)
#
# gen = da['장르']
# bud = da['예산']
#
# thr = bud[gen == "Thriller"].reset_index(drop=True)
# com = bud[gen == "Comedy"].reset_index(drop=True)
# dra = bud[gen == "Drama"].reset_index(drop=True)
# act = bud[gen == "Action"].reset_index(drop=True)
#
# varr = [thr.var(),com.var(),dra.var(),act.var()]
# doff = [len(thr), len(com),len(dra), len(act)]
#
# import numpy as np
# res = np.log(sum(np.subtract(doff, 1) * varr) / (sum(doff) - len(varr)))
#
# print(round(res,3))
#
# stat, pval = bartlett(thr,com,dra,act)
# print(round(stat , 2))
#
# print(pval)



# 9 번
import pandas as pd
da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/영화_순위리스트.csv")

from scipy.stats import bartlett

print(da.columns)
gen = da['장르'].copy()
bud = da['예산'].copy()

thr = bud[gen == "Thriller"]
com = bud[gen == "Comedy"]
dra = bud[gen == "Drama"]
act = bud[gen == "Action"]

varr = [thr.var(), com.var(), dra.var(), act.var()]
nums = [len(thr) - 1,len(com)-1,len(dra)-1,len(act)-1 ]
import numpy as np
res = np.log(sum(np.subtract(nums, 0) * varr) / sum(nums))

print(round(res,3))

aa = bartlett(thr,com,dra,act)
print(aa)















