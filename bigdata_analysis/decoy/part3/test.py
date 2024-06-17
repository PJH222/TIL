# 1번

# import pandas as pd

# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit_Five.csv")
#
# # print(da.columns) ['BP_change', 'Dose', 'Treatment', 'lbl_Animal']
# # print(da)
# #     BP_change    Dose Treatment lbl_Animal
# # 0        0.50    6.25   Control         R1
# # 29      18.00  200.00   Control         R5
# # ...
# # 30       1.25    6.25       MDL         R1
# # 31       0.75   12.50       MDL         R1
#
# bp = da['BP_change']
# tre = da['Treatment']
#
# mdl = bp[tre == "MDL"].reset_index(drop=True)
# conn = bp[tre == "Control"].reset_index(drop=True)
#
# result = (mdl - conn).mean()
# answer_a = round(result, 2)
# print(answer_a)
#
#
# from scipy.stats import ttest_rel
#
# stat,pval = ttest_rel(mdl,conn)
# answer_b = round(stat,2)
# print(answer_b)
#
# answer_c1 = round(pval, 3)
# print(answer_c1)
#
# if answer_c1 < 0.05:
#     print("기각")
# else:
#     print("채택")




# 2번

# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/mtcars2.csv")

# print(da)
#      mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
# 0   21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
# 1   21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
#
# amm = da['am']
# hpp = da['hp']
#
# a1 = hpp[amm == 1]
# a0 = hpp[amm == 0]
#
# ratioo = a1.var() / a0.var()
# answer_a = round(ratioo, 2)
# print(answer_a)
#
# from scipy.stats import f
#
# result = 1 - f.cdf(ratioo, len(a1) - 1, len(a0) - 1)
# print(round(result, 2))


# 2번 다시
# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/mtcars2.csv")

# print(da.columns) ['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
# 
# am = da['am']
# hp = da['hp']
# 
# a1 = hp[am == 1].reset_index(drop = True)
# a0 = hp[am == 0].reset_index(drop = True)
# 
# var_ratio = a1.var() / a0.var()
# answer_a = round(var_ratio, 2)
# print(answer_a)
# 
# answer_b = round(var_ratio, 2)
# print(answer_b)
# 
# from scipy.stats import f
# 
# result = 1 - f.cdf(var_ratio, len(a1) - 1, len(a0) - 1)
# answer_c = round(result, 3)
# 
# print(answer_c)
# if answer_c < 0.05:
#     print("기각")
# else:
#     print("채택")




# 3 번

# import pandas as pd
# import numpy as np
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/고객_등급리스트.csv")

# print(da.columns) ['Customer_ID', 'ID', 'Name', 'Age', 'City', 'State', 'Region', 'Segment']
#
# reg = da['Region'].copy()
# seg = da['Segment'].copy()
#
# aa = pd.crosstab(seg, reg)
#
# from scipy.stats import chi2_contingency
#
# stat, pval, df, bb = chi2_contingency(aa)
# result_a = bb[1,2]
# answer_a = round(result_a , 2)
# print(answer_a)
#
# answer_b = int(stat)
# print(answer_b)
#
# answer_c = round(pval, 3)
# print(answer_c)
#
# if answer_c < 0.05:
#     print("기각")
# else:
#     print("채택")


# 3번 다시
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/고객_등급리스트.csv")
#
# seg, reg = da['Segment'], da['Region']
#
# ctt = pd.crosstab(seg, reg)
#
# from scipy.stats import chi2_contingency
#
# stat, pval, df, result = chi2_contingency(ctt)
# answer_a = round(result[1,2], 2)
# print(answer_a)
#
# answer_b = int(stat)
#
# answer_c = round(pval,3)
# print(answer_b , answer_c)
# if answer_c < 0.05:
#     print("기각")
# else:
#     print("채택")


# 4번
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# from scipy.stats import shapiro
#
# pri = da['Price'].copy().dropna()
# result = pri.mean()
# answer_a = round(result, 2)
# print(answer_a)
#
# stat, pval = shapiro(pri)
# print(round(stat, 2))




# 4 번 다시
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# pri = da['Price'].copy().dropna()
#
# answer_a = round(pri.mean() , 2)
# print("a번 정답", answer_a)
#
# from scipy.stats import shapiro
#
# stat, pval = shapiro(pri)
# print("b번 정답", round(stat, 2))
#
# if round(pval, 4) <0.0001:
#     pval = 0
# print(pval)
#
# if pval < 0.1:
#     print("기각")
# else:
#     print("채택")




# 5 번
# import pandas as pd
#
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# rev, hor = da['Rev_per_mile'], da['Horsepower']
#
# from scipy.stats import pearsonr
#
# stat, pval = pearsonr(rev,hor)
# rho = round(stat, 3)
# print(rho)
#
# import numpy as np
#
# aa = rho / np.sqrt( (1 - rho**2 ) / (len(rev) - 2) )
# print(round(aa,2))
#
# bb = round(pval, 4)
# if bb < 0.0001:
#     bb = 0
# print(bb)
#
# if bb < 0.05:
#     print("기각")
# else:
#     print("채택")


# 5번 다시
# import pandas as pd
# da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
#
# rev, hor = da['Rev_per_mile'], da['Horsepower']
#
# from scipy.stats import pearsonr
#
# stat, pval = pearsonr(rev, hor)
# rho = round(stat, 3)
# print(rho)
#
# import numpy as np
#
# tt = rho / np.sqrt( (1 - rho**2)/( len(rev) - 2) )
# answer_b = round(tt,2)
# print(answer_b)
#
# if pval < 0.0001:
#     pval = 0
# print(pval)
#
# if pval < 0.05:
#     print("기각")
# else:
#     print("채택")


# 1번

import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit_Five.csv")

# print(da)
#     BP_change    Dose Treatment lbl_Animal
# 0        0.50    6.25   Control         R1
# 1        4.50   12.50   Control         R1

bp = da['BP_change'].copy()
tr = da['Treatment'].copy()

mdl = bp[tr=="MDL"].reset_index(drop=True)
con = bp[tr=="Control"].reset_index(drop=True)

tmp1 = (mdl - con).mean()
answer_a = round(tmp1, 2)
print(answer_a)

from scipy.stats import ttest_rel

stat, pval = ttest_rel(mdl, con)
print(round(stat, 2))

pval = round(pval, 3)
print(pval)
if pval < 0.05:
    print("기각")
else:
    print("채택")


