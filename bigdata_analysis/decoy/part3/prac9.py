import pandas as pd

da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/영화_순위리스트.csv")

# a)
genn = da['장르']
budd = da['예산']

# print(genn.value_counts())
thril = budd[genn == "Thriller"]
comm = budd[genn == "Comedy"]
draa = budd[genn == "Drama"]
actt = budd[genn == "Action"]

varr = [thril.var(), comm.var(), draa.var(), actt.var()]
nums = [len(thril), len(comm), len(draa), len(actt)]

import numpy as np

log_sp2 = np.log( sum(np.subtract(nums, 1) * varr) / (sum(nums) - len(varr)))
answer_a = round(log_sp2, 3)

print(answer_a)

from scipy.stats import bartlett

stat, pval = bartlett(thril,comm,draa,actt)
print(round(stat,2))

print(round(pval,4))
if pval < 0.1:
    print("기각")
else:
    print("채택")

