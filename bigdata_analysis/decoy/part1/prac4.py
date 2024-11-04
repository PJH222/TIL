import pandas as pd
import numpy as np

exam1 = pd.read_csv('C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv')

weight = exam1['Weight']
weight_std = (weight - min(weight)) / (max(weight) - min(weight))
print(weight_std)

var_over = weight_std[weight_std > 0.5].var()
var_under = weight_std[weight_std < 0.5].var()

diff = abs(var_over - var_under)
print(round(diff,3))




