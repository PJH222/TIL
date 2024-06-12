import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Rabbit_Five.csv")
# da = pd.read_csv("C:\Users\asd\TIL\bigdata_analysis\decoy\practice\Rabbit_Five.csv", encoding="cp949")

# from scipy.stats import ttest_rel
#
# #     BP_change    Dose Treatment lbl_Animal
# # 0        0.50    6.25   Control         R1
# # 1        4.50   12.50   Control         R1
# # ...
# # 30       1.25    6.25       MDL         R1
# # 31       0.75   12.50       MDL         R1
#
# bp = da['BP_change']
# trea = da['Treatment']
#
# bp_trea = bp[trea=="MDL"].reset_index(drop=True)
# bp_con = bp[trea=="Control"].reset_index(drop=True)
#
# avgg = (bp_trea - bp_con).mean()
# result = round(avgg,2)
# # print(result)
# # 진짜 말그대로 평균차를 구하는 것임
#
# a = ttest_rel(bp_trea, bp_con)
# print(a[0])
#
# stat = a.statistic
# stat = round(stat, 2)
# print(stat,round(a[0],2))
#
# print(round(a[1],3))
# print("기각")

# print(da)
bp = da['BP_change']
tre = da["Treatment"]

mdl = da['BP_change'][tre=="MDL"].reset_index()
con = da['BP_change'][tre=="Control"].reset_index()
# print(mdl)
aa = (mdl['BP_change'] - con['BP_change']).mean()

answer = round(aa, 2)
# print(answer)

from scipy.stats import ttest_rel

a = ttest_rel(mdl['BP_change'],con['BP_change'])
# print(round(a[0],2))

b = a[1]
print(round(b,3))
print("기각")