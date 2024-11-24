import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/영화_순위리스트.csv")

gen = df["장르"]
bud = df["예산"]

thi = bud[gen == "Thriller"]
com = bud[gen == "Comedy"]
dra = bud[gen == "Drama"]
act = bud[gen == "Action"]

tmp = [thi, com, dra , act]

var = [thi.var(), com.var(), dra.var(), act.var()]
nn = [len(thi), len(com) , len(dra) , len(act)]

summ = sum(nn)
k = 4

log_sp2 = np.log(sum(np.subtract(nn , 1) * var) / (summ - k))
answer = round(log_sp2, 3)
print(answer)

from scipy.stats import bartlett 

a = bartlett(thi , com , dra , act)
answer = round(a[0] , 2)
print(answer)

