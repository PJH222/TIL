
# 1번
# import pandas as pd

# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit_Five.csv")
#
# # print(da.columns) ['BP_change', 'Dose', 'Treatment', 'lbl_Animal']
#
# # print(da)
# #     BP_change    Dose Treatment lbl_Animal
# # 0        0.50    6.25   Control         R1
# # 1        4.50   12.50   Control         R1
#
# tre = da['Treatment'].copy()
# bp = da['BP_change'].copy()
#
# mdl = bp[tre == "MDL"].reset_index(drop=True)
# con = bp[tre == "Control"].reset_index(drop=True)
#
# answer_a = (mdl - con).mean()
# print(round(answer_a, 2))
#
# from scipy.stats import ttest_rel
#
# stat, pval = ttest_rel(mdl, con)
#
# answer_b = round(stat, 2)
# print(answer_b)
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
# # print(da)
# #      mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
# # 0   21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
# # 1   21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
# # print(da.columns)
# # ['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear','carb']
#
# hp = da['hp'].copy()
# am = da['am'].copy()
#
# am1 = hp[am == 1]
# am0 = hp[am == 0]
#
# answer_a = round(am1.var() / am0.var() , 2)
# print(answer_a)
#
# from scipy.stats import f
# print(answer_a)
#
# pval = 1 - f.cdf(answer_a, len(am1) - 1, len(am0) - 1)
# pval = round(pval, 3)
# print(pval)
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
# # print(da.columns) ['Customer_ID', 'ID', 'Name', 'Age', 'City', 'State', 'Region','Segment']
# reg, seg = da['Region'], da['Segment']
#
# ct = pd.crosstab(reg,seg)
#
# from scipy.stats import chi2_contingency
#
# stat, pval, dof, df = chi2_contingency(ct)
# # print(aa)
# answer_a = round(df[2,1] , 2)
# print(answer_a)
#
# answer_b = int(stat)
# print(answer_b)
#
# pval = round(pval, 3)
# print(pval)
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")



# 4번

# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# pri = da['Price'].copy().dropna()
# answer_a = round(pri.mean(), 2)
# print(answer_a)
#
# from scipy.stats import shapiro
#
# stat, pval = shapiro(pri)
# # print(aa)
#
# answer_b = round(stat, 2)
# print(answer_b)
#
# pval = round(pval , 4)
#
# if pval < 0.0001:
#     pval = 0
#
# print(pval)
#
# if  pval < 0.1:
#     print("기각")
# else:
#     print("채택")


# 5번
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# # print(da.columns) 'Rev_per_mile', 'Horsepower'
#
# rpm = da['Rev_per_mile'].copy()
# hp = da['Horsepower'].copy()
#
# from scipy.stats import pearsonr
#
# stat, pval = pearsonr(rpm,hp)
# # print(aa)>???
# rho = round(stat, 3)
# print(rho)
#
# import numpy as np
#
# tt = rho / np.sqrt( (1 - rho**2)/(len(hp) - 2) )
# answer_b = round(tt, 2)
# print(answer_b)
#
# pval = round(pval, 4)
# if pval < 0.0001:
#     pval = 0
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
# # 차원 축소
# # print(da.columns) ['Murder', 'Assault', 'UrbanPop', 'Rape']
# from sklearn.decomposition import PCA
#
# ass = da['Assault']
#
# pca = PCA()
# pca.fit_transform(da)
#
# aa = pca.components_
# print(round(aa[0,1] , 3))
#
# ass34 = pca.fit_transform(da)[33]
# print(round(ass34[0] , 3))
#
# result = pca.explained_variance_ratio_
# print(round(result[0] , 2))
#
# print(3)




# 7번
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# dropna_col = ['Rev_per_mile','Weight','Length','EngineSize','Price']
#
# dff = da[dropna_col].copy().dropna()
#
# y = dff['Price']
# x = dff[['Rev_per_mile','Weight','Length','EngineSize']]
#
# import statsmodels.api as sm
#
# x = sm.add_constant(x)
#
# aa = sm.OLS(y,x)
# result = aa.fit()
#
# print(result.summary())
#
# print(0.396)
# print(0.0023)
# print(0.158)
#
# conff = result.conf_int(alpha=0.05)
# print(conff)
#
# print(0.005406)


# 8 번

# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/job.csv")
#
# da['x2'] = da['x2'].map({"M":1,"F":0})
# y = da['y']
# x = da[['x1','x2','x3']]
#
# import statsmodels.api as sm
#
# x = sm.add_constant(x)
# aa = sm.GLM(y,x,family=sm.families.Binomial())
# result = aa.fit()
#
# print(result.summary())
# print(-0.8077)
#
# import numpy as np
# print(np.exp(-0.1575 ))
#
# prob = result.predict()[8]
# print(prob)








# 9 번
import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/영화_순위리스트.csv")

# print(da.columns) ['번호', '홍보비', '제작비', '예산', '영화길이_분', '남자_주연_배우_순위', '여_주연_배우_순위',
#        '디렉터_순위', '프로듀서_순위', '비평가_순위', '트레일러_뷰수', '3D_가능여부', '트위터_해시태그_수', '장르',
#        '배우_평균_나이']

bud = da['예산']
gen = da['장르']

thr = bud[gen == "Thriller"]
com = bud[gen == "Comedy"]
dra = bud[gen == "Drama"]
act = bud[gen == "Action"]

varr = [thr.var(), com.var(), dra.var(), act.var()] # s**2
nums = [len(thr),len(com),len(dra),len(act)] # n

import numpy as np

log_sp2 = np.log(sum(np.subtract(nums, 1) * varr) / (sum(nums) - len(varr)))

print(log_sp2)

from scipy.stats import bartlett

stat, pval = bartlett(thr,com,dra,act)
# print(aa)


