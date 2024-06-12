import pandas as pd

data = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/Cars93.csv")
aa, bb = data.copy(), data.copy()

aa['Price'] = data['Price'].fillna(aa['Price'].mean())
bb['Price'] = data['Price'].fillna(bb['Price'].median())

avg_minmax = aa[['Max_Price', 'Min_Price']].mean(axis=1) # 왜시발 합의 평균이라고 안적어놨냐 존나짜증나네 진짜...
# print(avg_minmax)
# print()
# print((aa['Max_Price'] + aa['Min_Price'])/2)

sub_aa = aa[aa['Price'] < avg_minmax]
origin_aa = sub_aa.groupby('Origin')['Price'].sum()

q3_bb = bb['Min_Price'].quantile(0.75)

bb2 = bb[bb['Price'] < q3_bb ]
origin_bb = bb2.groupby('Origin')['Price'].sum()

print(int(max(origin_aa + origin_bb)))
