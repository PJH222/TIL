import pandas as pd
data = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")

data['RPM'] = (data['RPM'].fillna(data['RPM'].mean()))

data['Wheelbase'] = (data['Wheelbase'] - data['Wheelbase'].mean()) / data['Wheelbase'].std() * (-36)
data['str_RPM'] = (data['RPM'] - data['RPM'].mean()) / data['RPM'].std()

data['result'] = data['Wheelbase'] - data['str_RPM']

result = data['result'].std()
answer = round(result,3)
print(answer)