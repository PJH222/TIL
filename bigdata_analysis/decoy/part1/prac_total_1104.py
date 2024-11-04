import pandas as pd
import numpy as np

exam1 = pd.read_csv('C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv')

# wheel = exam1['Wheelbase']

# meann = wheel.mean()
# std_15 = wheel.std() * 1.5
# std_20 = wheel.std() * 2
# std_25 = wheel.std() * 2.5

# a0 = meann - std_15
# a1 = meann + std_15

# b0 = meann - std_20
# b1 = meann + std_20

# c0 = meann - std_25
# c1 = meann + std_25

# answer1 = wheel[(wheel > a0) & (wheel < a1)].mean()
# answer2 = wheel[(wheel > b0) & (wheel < b1)].mean()
# answer3 = wheel[(wheel > c0) & (wheel < c1)].mean()

# answer = meann * 3 - answer1 - answer2 - answer3
# print(round(answer,4))


exam1['rank'] = exam1['Length'].rank(method = 'average')

