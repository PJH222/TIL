import pandas as pd
import numpy as np
da = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

rev , hor = da['Rev_per_mile'], da['Horsepower']

from scipy.stats import pearsonr

rho , pval = pearsonr(rev,hor)
rho1 , pval1 = pearsonr(hor, rev) # 뒤 바뀌어도 상관없다
result = round(rho,3)
print(result)


tt = rho/np.sqrt((1 - rho ** 2)/(len(rev) - 2 ))
print(round(tt,2))





