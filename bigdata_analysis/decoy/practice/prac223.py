import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/영화_순위리스트.csv")

ge = df['장르']
bu = df["예산"]

th = bu[ge=="Thriller"]
co = bu[ge=="Comedy"]
dr = bu[ge=="Drama"]
ac = bu[ge=="Action"]

varr = [th.var(),co.var(),dr.var(),ac.var()]
nn = [len(th) , len(co) , len(dr), len(ac)]

answer = round(sum(np.subtract(nn,1) * varr) / (sum(nn) - 4) , 3)
print(answer)

from scipy.stats import bartlett as b

a = b(th, co, dr , ac)
answer = round(a[0] , 2)
print(answer)

