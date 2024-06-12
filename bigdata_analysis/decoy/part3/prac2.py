import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/mtcars2.csv")

#      mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
# 0   21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
# 1   21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
# 2   22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
# amm = da['am']
#
# am0 = da['hp'][amm == 0].reset_index(drop=True)
# am1 = da['hp'][amm == 1].reset_index(drop=True)
#
# a0 = am0.var()
# a1 = am1.var()
#
# answer = round(a1 / a0 , 2)
# result = a1 / a0
# print("a 정답:",answer)
# print("b 정답:",answer)
#
# from scipy.stats import f
#
# df1, df2 = len(am0) - 1, len(am1) - 1
# pval = 1 - f.cdf(result, dfn = df2, dfd = df1) # <<<< 이거 분명 실수해서 틀릴 것 같다.... 주의해라...
# print(pval)
# print("기각 씨발아")



#      mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
# 0   21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
# 1   21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
# 2   22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
am = da['am']
hp = da['hp']

am1 = da['hp'][am == 1].reset_index(drop=True)
am0 = da['hp'][am == 0].reset_index(drop=True)

a11 = am1.var()
a00 = am0.var()

result = a11 / a00
answer = round(result, 2)
print("a번 정답 :",answer)

var_ratio = answer
print("b번 정답 :", var_ratio)
print()

from scipy.stats import f

pval = 1 - f.cdf(result,dfn=am1.shape[0] - 1, dfd=am0.shape[0] - 1 )
answer = round(pval, 3)
print("c번 정답 :",answer)
print("기각")

