# 라이브러리 임포트
from cProfile import label
from turtle import color

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
# print(df_seoul)
# sr_one = df_seoul.loc['경기도']
# print(sr_one)
# 데이터 전처리 완료

# 1970~2017년까지 문자열로 리스트 생성
col_years = list(map(str, range(1970, 2018)))
# 각 4개의 도를 선택해서 데이터 추출 / 연도 지정 
df4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'], col_years]

# 캔버스의 크기 지정. 와이드하게 긴 사각형의 형태.
fig = plt.figure(figsize=(20,10))
# 2행 2열의 첫번째부터 순서대로 Axe객체 생성
axe1 = fig.add_subplot(2,2,1) 
axe2 = fig.add_subplot(2,2,2)
axe3 = fig.add_subplot(2,2,3)
axe4 = fig.add_subplot(2,2,4)

'''
각 Axe객체에 plot 함수로 그래프를 출력한다.
x축은 기간, y축은 각 전출지의 전체 데이터를 설정한다.
나머지는 그래프의 마커, 컬러, 두께 등을 설정한다.
'''
axe1.plot(col_years, df4.loc['충청남도',:], marker='o', markerfacecolor='green',
          markersize=10, color='olive', linewidth=2, label='서울->충남')
axe2.plot(col_years, df4.loc['경상북도',:], marker='*', markerfacecolor='blue',
          markersize=10, color='skyblue', linewidth=2, label='서울->경북')
axe3.plot(col_years, df4.loc['강원도',:], marker='.', markerfacecolor='red',
          markersize=10, color='magenta', linewidth=2, label='서울->강원')
axe4.plot(col_years, df4.loc['전라남도',:], marker='+', markerfacecolor='orange',
          markersize=10, color='black', linewidth=2, label='서울->전남')
# 범례 설정
axe1.legend(loc='best')
axe2.legend(loc='upper left')
axe3.legend(loc='lower right')
axe4.legend(loc='lower left')

# 타이틀 설정
axe1.set_title('서울 -> 충남 인구 이동', size=15)
axe2.set_title('서울 -> 경북 인구 이동', size=15)
axe3.set_title('서울 -> 강원 인구 이동', size=15)
axe4.set_title('서울 -> 전남 인구 이동', size=15)

# x축 눈금 및 회전설정
axe1.set_xticklabels(col_years, rotation=90)
axe2.set_xticklabels(col_years, rotation=60)
axe3.set_xticklabels(col_years, rotation=120)
axe4.set_xticklabels(col_years, rotation=250)

plt.show()
