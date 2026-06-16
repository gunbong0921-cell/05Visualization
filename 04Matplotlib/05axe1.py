# 라이브러리 임포트
from cProfile import label

import pandas as pd
import matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트매니저 임포트
# 한글깨짐처리 Start
from matplotlib import font_manager, markers, rc
# 한글폰트 경로 설정
font_path = "../resData/malgun.ttf"
# 폰트 파일의 이름을 속성으로 지정
font_name = font_manager.FontProperties(fname=font_path).get_name()
# 폰트 적용
rc('font', family=font_name)
# 한글깨짐처리 end

# 데이터프레임 만들기
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine='openpyxl', header=0)
# df = df.fillna(method='ffill') 
df = df.ffill()
print(df.head())

# 서울에서 경기로 전출할 데이터만 추출
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)
sr_one = df_seoul.loc['경기도']
# print(sr_one)
# 데이터 전처리 완료

# 그래프 스타일 지정하기 : ggplot과 같은 스타일은 URL참조
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('ggplot')

'''
여러개의 Axe객체를 생성하여 서로 다른 그래프를 표현할 수 있다.
figure() 함수로 캔버스(그래프의 틀)을 만든 후 figsize 옵션으로 크기를
지정한다. 크기는 비율로 지정할 수 있다.
add_subplot() 함수로 캔버스를 분할한다. 여기서 분할된 틀을 Axe객체라고
한다.
'''
# 그래프의 비율 설정
fig = plt.figure(figsize=(10, 10))
# 2행 1열중 첫번째 Axe 객체 생성(즉 캔버스를 위/아래 방향으로 분할)
axe1 = fig.add_subplot(2, 1, 1)
# 두번째 Axe 객체 생성
axe2 = fig.add_subplot(2, 1, 2)

'''
marker : 마커를 표시한 선 그래프를 그려준다. 마커의 종류에는 o, *, +, . 등이 있다.
markerfacecolor : 마커의 배경색
color : 마커의 색깔
'''
axe1.plot(sr_one, 'o', markersize=10)
axe2.plot(sr_one, marker='*', markersize=10, markerfacecolor='green', 
          color='olive', linewidth=2, label='서울->경기')

# 범례
axe2.legend(loc='best')
# Y축의 범위 
axe1.set_ylim(50000, 800000)
axe2.set_ylim(50000, 800000)
# X축의 눈금 라벨 및 텍스트의 회전 각도 설정
axe1.set_xticklabels(sr_one.index, rotation=70)
axe2.set_xticklabels(sr_one.index, rotation=-75)

plt.show()