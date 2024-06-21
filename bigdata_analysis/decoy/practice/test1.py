import pandas as pd
import numpy as np

da = pd.read_csv("영화_순위리스트.csv")

from scipy.stats import bartlett

# print(da.columns) 장르 예산

gen = da['장르']
bud = da['예산']

thr = bud[gen == 'Thriller']
com = bud[gen == 'Comedy']
dra = bud[gen == 'Drama']
act = bud[gen == "Action"]

varr = [thr.var(), com.var(), dra.var(), act.var()]
dff = [len((thr)), len(com),len(dra),len(act)]

N = len(da)

result = (1 / (N - 4)) * sum(np.subtract(dff,1)*varr)

answer = np.log(result)
print(round(answer,3))

bb = bartlett(thr,com,dra,act)
print(bb)