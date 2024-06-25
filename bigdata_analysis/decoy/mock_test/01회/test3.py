import pandas as pd

da = pd.read_csv("dices.csv")

print(1/6 * 500)

from scipy.stats import chisquare as ch

aa = da['scale'].value_counts()

# tb = pd.crosstab(aa)
print(ch(aa))

