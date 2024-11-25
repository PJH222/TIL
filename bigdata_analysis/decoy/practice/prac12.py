import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/asd/TIL/bigdata_analysis/decoy/practice/영화_순위리스트.csv")

# print(df.columns)['번호', '홍보비', '제작비', '예산', '영화길이_분', '남자_주연_배우_순위', '여_주연_배우_순위',
#        '디렉터_순위', '프로듀서_순위', '비평가_순위', '트레일러_뷰수', '3D_가능여부', '트위터_해시태그_수', '장르',
#        '배우_평균_나이']

gen, bud = df["장르"], df["예산"]

thr = bud[gen == "Thriller"]
com = bud[gen == "Comedy"]
dra = bud[gen == "Drama"]
act = bud[gen == "Action"]

varr = [thr.var(), com.var(), dra.var(), act.var()]
n_df = [len(thr) , len(com) , len(dra) , len(act)]

sp2 = sum(np.subtract(n_df,1) * varr) / (sum(n_df) - 4)
log_sp2 = np.log(sp2)
# print(log_sp2)
answer = round(log_sp2, 3)
print(answer)

from scipy.stats import bartlett

a = bartlett(thr, com, dra, act)
print(a)
answer = round(a[0] , 2)
print(answer)

answer = round(a[1] , 4)
if answer < 0.1:
    print("기각")
else:
    print("채택")

    