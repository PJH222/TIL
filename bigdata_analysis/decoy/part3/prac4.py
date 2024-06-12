import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

# pri=da['Price'].copy().dropna()
# avgg = pri.mean()
#
# print("a번 정답 :", avgg)
#
# from scipy.stats import shapiro
# statss, pval = shapiro(pri)
# print("b번 정답 :", statss)
#
# print("c번 정답 :", int(round(pval,4)),"기각")



# a번)
a = da['Price'].isna().sum()
print(a)

pri = da['Price'].copy().dropna()
print("a번 정답 :", round(pri.mean(),2))

# b번)
from scipy.stats import shapiro
aa, bb = shapiro(pri)
print("b번 정답 :", round(aa,2))

# c번)
print("c번 정답 :", int(round(bb, 4)), "기각")

