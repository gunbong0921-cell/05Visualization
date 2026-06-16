# 라이브러리 임포트
from cProfile import label

from numpy import size
import pandas as pd
import matplotlib.pyplot as plt

# 한글깨짐 처리를 위해 폰트매니저 임포트
# 한글깨짐처리 Start
from matplotlib import font_manager, markers, rc
from pyparsing import line
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

# 캔버스 크기 지정
fig = plt.figure(figsize=(20, 5))
# 2행 1열중 첫번째 Axe 객체 생성(즉 캔버스를 위/아래 방향으로 분할)
axe1 = fig.add_subplot(2, 1, 1)
# Axe 갹체에 plot함수로 그래프 생성
axe1.plot(sr_one, marker='o', markersize=10, markerfacecolor='orange',
          color='olive', linewidth=2, label='서울->경기')
# 범례
axe1.legend(loc='best')
# y축 범위
axe1.set_ylim(50000, 800000)
# 타이틀 및 라벨 설정
axe1.set_title('서울 -> 경기 인구 이동', size=20)
axe1.set_xlabel('기간', size=12)
axe1.set_ylabel('이동인구수', size=12)
axe1.set_xticklabels(sr_one.index, rotation=75)
axe1.tick_params(axis='x', labelsize=20)
axe1.tick_params(axis='y', labelsize=10)

plt.show()
