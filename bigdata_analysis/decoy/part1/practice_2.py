import pandas as pd
data = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

a = data['Length'].rank(method='average') # 작은 순서로 나옴...
# b = list(data['Length'])

b = data['Length'][a <= 30].std()

print(round(b,3))




