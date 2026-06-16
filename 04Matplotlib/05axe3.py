# 라이브러리 임포트
from cProfile import label
from turtle import color

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

'''
map 함수를 통해 1970~2017까지의 문자열로 구성된 리스트를 생성.
map의 첫번째 인수가 str함수이므로 범위만큼 반복하면서 호출하게 된다.
'''
col_years = list(map(str, range(1970, 2018)))
print(col_years)
# 서울에서 각 3개의 도로 전출한 데이터 추출. 기간은 1970~2017로 설정
df3 = df_seoul.loc[['충청남도','경상북도','강원도'], col_years]

# 스타일 설정 및 Ave 객체 1개 생성
# 그래프 스타일 지정하기 : ggplot과 같은 스타일은 URL참조
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('ggplot')

# 캔버스 크기 지정
fig = plt.figure(figsize=(20, 5))
# 2행 1열중 첫번째 Axe 객체 생성(즉 캔버스를 위/아래 방향으로 분할)
'''
1개의 그래프에서 3개의 꺽은 선을 추가한다.
x축은 기간, y축은 각 도의 전체기간을 선택해서 설정한다.
'''
axe = fig.add_subplot(1, 1, 1)
# Axe 갹체에 plot함수로 그래프 생성
axe.plot(col_years, df3.loc['충청남도',:], marker='o', markerfacecolor='green',
          markersize=10, color='olive', linewidth=2, label='서울 -> 충남')
axe.plot(col_years, df3.loc['경상북도',:], marker='*', markerfacecolor='blue',
          markersize=10, color='skyblue', linewidth=2, label='서울 -> 경북')
axe.plot(col_years, df3.loc['강원도',:], marker='.', markerfacecolor='red',
          markersize=10, color='magenta', linewidth=2, label='서울 -> 강원')
# 범례, 타이틀, 라벨, 텍스트의 기울기 등 설정 
axe.legend(loc='best')
# 타이틀 및 라벨 설정
axe.set_title('서울->충남, 경북, 강원 인구이동', size=20)
axe.set_xlabel('기간', size=12)
axe.set_ylabel('이동인구수', size=12)
# 각 축의 눈금라벨 크기 설정
axe.tick_params(axis='x', labelsize=10, rotation=90)
axe.tick_params(axis='y', labelsize=20)

plt.show()