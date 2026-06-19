import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def sub_addr(x, i):
    x2 = x.split()
    # 주소 분할 시 인덱스 에러 방지를 위한 안전장치 추가
    if len(x2) > i:
        return x2[i].strip()
    return ""

input_file = "../resData/치킨집가공.csv"  
df_chicken1 = pd.read_csv(input_file)
print(df_chicken1.info())
print(df_chicken1.head())

df_chicken1 = df_chicken1.dropna(axis=0)

df_chicken1 = df_chicken1.rename(
    columns={'소재지전체주소': 'addr', '사업장명': 'biznm'}, inplace=False)
print(df_chicken1.info())
print(df_chicken1.head())

df_chicken1['addr2'] = df_chicken1['addr'].apply(lambda x: sub_addr(x, 1))
print(df_chicken1['addr2'].head(20))

df_chicken1['addr3'] = df_chicken1['addr'].apply(lambda x: sub_addr(x, 2))  
print(df_chicken1['addr3'].head(20))

df_chicken2 = df_chicken1[df_chicken1['addr2'] == '종로구']

# groupby 후 컬럼명이 겹치지 않도록 미리 count로 변경하는 것이 깔끔함.
df_chicken3 = df_chicken2.groupby('addr3')[['addr']].count()
df_chicken3 = df_chicken3.rename(columns={'addr': 'count'}, inplace=False)

df_chicken3 = df_chicken3.sort_values(by='count', ascending=False)
print(df_chicken3.head())

df_chicken3['name'] = df_chicken3.index
print(df_chicken3.head())

# [수정] 경고(Warning) 방지를 위해 .copy()를 추가.
df_chicken4 = df_chicken3.head(30).copy()
print(df_chicken4)

plt.style.use('ggplot')
font_name = font_manager.FontProperties(fname="../resData/malgun.ttf").get_name()
rc('font', family=font_name)

axe = plt.subplot()

# f-string 방식으로 깔끔하게 처리
df_chicken4["label"] = df_chicken4['name'] + "\n(" + df_chicken4['count'].astype(str) + ")"

# 트리맵 그리기
axe = squarify.plot(sizes=df_chicken4['count'], label=df_chicken4['label'], alpha=.8)

plt.axis('off')
# saveFiles 폴더가 없으면 에러가 날 수 있으므로 저장 전 폴더 생성 확인 필요
import os
os.makedirs('../saveFiles', exist_ok=True)

plt.savefig('../saveFiles/chicken04.png', dpi=300, bbox_inches='tight')
plt.show()