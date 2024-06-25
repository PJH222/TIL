import pandas as pd

da = pd.read_csv("Cars93.csv")

# print(da['Origin'].value_counts()) USA non-USA

from scipy.stats import ttest_ind, ttest_rel

ori = da['Origin']
pri = da['Max_Price']

m0 = pri[ori == "USA"]
m1 = pri[ori != "USA"]

print(abs(m0.mean() - m1.mean()))

stat , pval = ttest_ind(m0, m1,equal_var = False)

# 검정 = 추정 / 오차

aa = abs(m0.mean() - m1.mean()) / stat
print(aa)

